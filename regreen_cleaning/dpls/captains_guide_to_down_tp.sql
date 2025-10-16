do $$
declare
    rec record;
    tp_entry record;
    tp_species record;
    tp_usages record;
    tp_mgmts record;
    tp_measurements record;
    tp_planting_area record;
    plot_points record;
    plot_polygons record;
    loot record;
    crops record;
begin
    for rec in (
       with duplicates as (
            select *, count(*) over (partition by name) as kount,
            row_number() over (partition by name order by name) as dup_rank
            from respi_plots -- order by recorded_dte desc
            )
            select dpls.id as plot_id, dpls.recorded_dte, dpls.name as plot_name, dpls.estimated_size, dpls.calculated_size, dpls.photo_url, dpls.plot_ownership_type, dpls.dup_rank, ent.id as tp_entry_id 
            from duplicates dpls inner join respi_tree_planting_entry ent on ent.plot_id=dpls.id where kount > 1 and dup_rank > 1 and ent.id is not null
    ) loop

        raise notice 'Processing plot_id: %, plot_name: %, dup_rank: %', rec.plot_id, rec.plot_name, rec.dup_rank;
        
        --get the tree measurements associated with the plot
        for tp_measurements in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as tp_entry_id, ent.recorded_dte as tp_entry_recorded_dte, ent.    collector_id, ent.project_id, ch.id as tp_species_id, ch.local_name, ch.scientific_name, msm.id as tree_measurement_id, msm.recorded_dte as measurement_recorded_date, msm.latitude, msm.longitude, msm.photo_url 
            from 
                respi_plots plt inner join respi_tree_planting_entry ent on ent.plot_id=plt.id inner join respi_cohort ch on ch.tp_entry_id=ent.id inner join respi_tree_measurement msm on msm.cohort_id=ch.id 
            where 
                ent.plot_id=rec.plot_id and ch.id is not null
            
        loop
            raise notice 'TP Measurements...%', tp_measurements;
            -- delete associated tp_measurements
            delete from respi_tree_measurement where id=tp_measurements.tree_measurement_id;        
        end loop;
        
        --get the managements associated with the plot
        for tp_mgmts in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as tp_entry_id, ent.recorded_dte as tp_entry_recorded_dte, ent.collector_id, ent.project_id, ch.id as cohort_id, ch.local_name, ch.scientific_name, mnm.id as tp_management_id, mnm.recorded_dte as tp_management_recorded_date, mnm.management_practies 
            from 
                respi_plots plt inner join respi_tree_planting_entry ent on ent.plot_id=plt.id inner join respi_cohort ch on ch.tp_entry_id=ent.id inner join respi_tp_management_practices mnm on mnm.cohort_id=ch.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'TP Managements...%', tp_mgmts;
            -- delete associated tp_managements
            delete from respi_tp_management_practices where id=tp_mgmts.tp_management_id;        
        end loop;
        
        --get the usages associated with the tp_species
        for tp_usages in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as tp_entry_id, ent.recorded_dte as tp_entry_recorded_dte, ent.project_id, ch.id as cohort_id, ch.local_name, ch.scientific_name, usg.id as tp_tree_usage_id, usg.recorded_dte as tp_tree_usage_recorded_date, usg.tree_usage 
            from 
                respi_plots plt inner join respi_tree_planting_entry ent on ent.plot_id=plt.id inner join respi_cohort ch on ch.tp_entry_id=ent.id inner join respi_tp_tree_usage usg on usg.cohort_id=ch.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'TP Usages...%', tp_usages;
            -- delete associated tp_usages
            delete from respi_tp_tree_usage where id=tp_usages.tp_tree_usage_id;        
        end loop;

        --get the tree planting area type
        for tp_planting_area in 
            select 
                ch.*,tpe.*, tpa.id as tpa_id 
            from 
                respi_cohort ch inner join respi_tree_planting_entry tpe on tpe.id=ch.tp_entry_id inner join respi_tp_plantingarea_type tpa on tpa.cohort_id=ch.id 
            where 
                tpe.plot_id=rec.plot_id
        loop
            raise notice 'TP planting area type...%', tp_planting_area;
            --delete the associated planting area types
            delete from respi_tp_plantingarea_type where id=tp_planting_area.tpa_id;    
        end loop;

        --get the species associated with the tp_entry
        for tp_species in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as tp_entry_id,  ent.project_id, ent.plot_id, ch.id as cohort_id, ch.local_name, ch.scientific_name 
            from 
                respi_plots plt inner join respi_tree_planting_entry ent on ent.plot_id=plt.id inner join respi_cohort ch on ch.tp_entry_id=ent.id
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'TP Species...%', tp_species;
            -- delete associated tp_species
            delete from respi_cohort where id=tp_species.cohort_id;
        end loop;

        --get the tp_entry associated with the plot
        for tp_entry in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.estimated_size, plt.calculated_size, plt.photo_url, plt.plot_ownership_type, ent.id as tp_entry_id,  ent.project_id, ent.plot_id 
            from 
                respi_plots plt inner join respi_tree_planting_entry ent on ent.plot_id=plt.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'TP Entry...%', tp_entry;
            -- delete associated tp_entry 
            delete from respi_tree_planting_entry where id=tp_entry.tp_entry_id;  
        end loop; 

        --get the plot points for this plot
        for plot_points in 
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, plp.id as plot_point_id, plp.latitude as plot_lat, plp.longitude as plp_lon 
            from 
                respi_plots plt inner join respi_plot_points plp on plp.plot_id=plt.id 
            where 
                plt.id=rec.plot_id
        loop
            raise notice 'Plot Points...%', plot_points;
            -- delete associated plot points
            delete from respi_plot_points where id=plot_points.plot_point_id;        
        end loop;

        --get the poly polygons for the plot
        for plot_polygons in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, plp.id as plot_polygon_id, plp.recorded_dte as plot_polygon_recorded_date, plp.actual_size 
            from 
                respi_plots plt inner join respi_plot_polygon plp on plp.plot_id=plt.id 
            where 
                plt.id=rec.plot_id
        loop
            raise notice 'Plot Polygons...%', plot_polygons;
            -- delete associated plot polygons
            delete from respi_plot_polygon where id=plot_polygons.plot_polygon_id;        
        end loop;

        --if land ownership type is referenced, delete the land ownership type
        for loot in --land ownership type
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, lot.id as land_ownership_type_id, lot.recorded_dte as lot_recorded_date, lot.ownership 
            from 
                respi_plots plt inner join respi_land_ownership_type lot on lot.plot_id=plt.id 
            where 
                plt.id=rec.plot_id
        loop
            raise notice 'Land Ownership Type...%', loot;
            -- delete associated land ownership type
            delete from respi_land_ownership_type where id=loot.land_ownership_type_id;        
        end loop;

        --if crops, delete them
        for crops in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, crps.id as crops_id, crps.recorded_dte as crops_recorded_date, crps.crop_name 
            from 
                respi_plots plt inner join respi_crops crps on crps.plot_id=plt.id 
            where 
                plt.id=rec.plot_id
        loop
            raise notice 'Crops...%', crops;
            -- delete associated crops
            delete from respi_crops where id=crops.crops_id;        
        end loop;

        --delete the plot
        delete from respi_plots where id=rec.plot_id;
    end loop;
end $$;