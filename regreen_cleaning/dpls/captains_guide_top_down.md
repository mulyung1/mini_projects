
## plot duplicates

this cursor helps
```sql
with duplicates as (
    select 
        *, count(*) over (partition by name) as kount,
        row_number() over (partition by name order by name) as dup_rank
    from respi_plots
    )
    select 
        id as plot_id, recorded_dte, name as plot_name, estimated_size, calculated_size, photo_url,plot_ownership_type, dup_rank
    from 
        duplicates 
    where 
        kount > 1 and dup_rank > 1;
```

## delete function -  fmnr records
```sql
do $$
declare --record variables. help us access row values via dot notation
    rec record;
    fmnr_entry record;
    fmnr_species record;
    fmnr_usages record;
    fmnr_mgmts record;
    fmnr_measurements record;
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
            select 
                dpls.id as plot_id, dpls.recorded_dte, dpls.name as plot_name, dpls.estimated_size, dpls.calculated_size, dpls.photo_url, dpls.plot_ownership_type, dpls.dup_rank, ent.id as fmnr_entry_id 
            from 
                duplicates dpls inner join respi_fmnr_entry ent on ent.plot_id=dpls.id
            where 
                kount > 1 and dup_rank > 1 and ent.id is not null
    ) loop

        raise notice 'Processing plot_id: %, plot_name: %, dup_rank: %', rec.plot_id, rec.plot_name, rec.dup_rank;
        
        --get the tree measurements associated with the plot
        for fmnr_measurements in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as fmnr_entry_id, ent.recorded_dte as fmnr_entry_recorded_dte, ent.    collector_id, ent.project_id, spcs.id as fmnr_species_id, spcs.     local_name, spcs.scientific_name, msm.id as tree_measurement_id, msm.recorded_dte as measurement_recorded_date, msm.latitude, msm.longitude, msm.photo_url 
            from 
                respi_plots plt 
                inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
                inner join respi_fmnr_species spcs on spcs.fmnr_entry_id=ent.id 
                inner join respi_tree_measurement msm on msm.fmnr_species_id=spcs.id 
            where 
                ent.plot_id=rec.plot_id and spcs.id is not null
            
        loop
            raise notice 'FMNR Measurements...%', fmnr_measurements;
            -- delete associated fmnr_measurements
            delete from respi_tree_measurement where id=fmnr_measurements.tree_measurement_id;        
        end loop;
        
        --get the managements associated with the plot
        for fmnr_mgmts in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as fmnr_entry_id, ent.recorded_dte as fmnr_entry_recorded_dte, ent.collector_id, ent.project_id, spcs.id as fmnr_species_id, spcs.local_name, spcs.scientific_name, mnm.id as fmnr_management_id, mnm.recorded_dte as fmnr_management_recorded_date, mnm.management_practies 
            from 
                respi_plots plt 
                inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
                inner join respi_fmnr_species spcs on spcs.fmnr_entry_id=ent.id 
                inner join respi_fmnr_management_practices mnm on mnm.fmnr_species_id=spcs.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'FMNR Managements...%', fmnr_mgmts;
            -- delete associated fmnr_managements
            delete from respi_fmnr_management_practices where id=fmnr_mgmts.fmnr_management_id;        
        end loop;
        
        --get the usages associated with the fmnr_species
        for fmnr_usages in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as fmnr_entry_id, ent.recorded_dte as fmnr_entry_recorded_dte, ent.project_id, spcs.id as fmnr_species_id, spcs.local_name, spcs.scientific_name, usg.id as fmnr_tree_usage_id, usg.recorded_dte as fmnr_tree_usage_recorded_date, usg.tree_usage 
            from 
                respi_plots plt 
                inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
                inner join respi_fmnr_species spcs on spcs.fmnr_entry_id=ent.id 
                inner join respi_fmnr_tree_usage usg on usg.fmnr_species_id=spcs.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'FMNR Usages...%', fmnr_usages;
            -- delete associated fmnr_usages
            delete from respi_fmnr_tree_usage where id=fmnr_usages.fmnr_tree_usage_id;        
        end loop;

        --get the species associated with the fmnr_entry
        for fmnr_species in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, ent.id as fmnr_entry_id,  ent.project_id, ent.plot_id, spcs.id as fmnr_species_id, spcs.local_name, spcs.scientific_name 
            from 
                respi_plots plt 
                inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
                inner join respi_fmnr_species spcs on spcs.fmnr_entry_id=ent.id
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'FMNR Species...%', fmnr_species;
            -- delete associated fmnr_species
            delete from respi_fmnr_species where id=fmnr_species.fmnr_species_id;
        end loop;

        --get the fmnr_entry associated with the plot
        for fmnr_entry in
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.estimated_size, plt.calculated_size, plt.photo_url, plt.plot_ownership_type, ent.id as fmnr_entry_id,  ent.project_id, ent.plot_id 
            from 
                respi_plots plt 
                inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
            where 
                ent.plot_id=rec.plot_id
        loop
            raise notice 'FMNR Entry...%', fmnr_entry;
            -- delete associated fmnr_entry 
            delete from respi_fmnr_entry where id=fmnr_entry.fmnr_entry_id;  
        end loop; 

        --get the plot points for this plot
        for plot_points in 
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, plp.id as plot_point_id, plp.latitude as plot_lat, plp.longitude as plp_lon 
            from 
                respi_plots plt 
                inner join respi_plot_points plp on plp.plot_id=plt.id 
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
                respi_plots plt 
                inner join respi_plot_polygon plp on plp.plot_id=plt.id 
            where 
                plt.id=rec.plot_id
        loop
            raise notice 'Plot Polygons...%', plot_polygons;
            -- delete associated plot polygons
            delete from respi_plot_polygon where id=plot_polygons.plot_polygon_id;        
        end loop;

        --if land ownership type is referenced, delete the land ownership type
        for loot in 
            select 
                plt.id as plot_id, plt.recorded_dte, plt.name as plot_name, plt.photo_url, lot.id as land_ownership_type_id, lot.recorded_dte as lot_recorded_date, lot.ownership 
            from 
                respi_plots plt 
                inner join respi_land_ownership_type lot on lot.plot_id=plt.id 
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
                respi_plots plt 
                inner join respi_crops crps on crps.plot_id=plt.id 
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
```































