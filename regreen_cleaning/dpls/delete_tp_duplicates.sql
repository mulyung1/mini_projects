CREATE OR REPLACE FUNCTION delete_tp_dpls(plot_ide INTEGER)
RETURNS TEXT AS $$ 

DECLARE
    tp_entr_ids INT[];
    tp_cohort_ids INT[];
    trm_ids INT[];
    us_ids INT[];
    mn_ids INT[];
    planting_area_type_ids INT[];
    pl_points_ids INT[];
    pl_polygons_ids INT[];

    found_fmnr BOOLEAN;
    found_tables TEXT[] := ARRAY[]::TEXT[];

BEGIN
    SELECT
        array_agg(DISTINCT tp_en.id),
        array_agg(DISTINCT tp_ch.id),
        array_agg(DISTINCT trm.id),
        array_agg(DISTINCT tp_us.id),
        array_agg(DISTINCT tp_mn.id),
        array_agg(DISTINCT pat.id),
        array_agg(DISTINCT plp.id),
        array_agg(DISTINCT plpl.id)
    INTO
        tp_entr_ids,
        tp_cohort_ids,
        trm_ids,
        us_ids,
        mn_ids,
        planting_area_type_ids,
        pl_points_ids,
        pl_polygons_ids
    FROM
        respi_tree_planting_entry tp_en 
        JOIN respi_cohort tp_ch ON tp_ch.tp_entry_id = tp_en.id
        JOIN respi_tree_measurement trm ON trm.cohort_id = tp_ch.id
        JOIN respi_tp_tree_usage tp_us ON tp_us.cohort_id=tp_ch.id
        JOIN respi_tp_management_practices tp_mn ON tp_mn.cohort_id=tp_ch.id
        JOIN respi_tp_plantingarea_type pat ON pat.cohort_id=tp_ch.id
        JOIN respi_plot_points plp ON plp.plot_id = tp_en.plot_id
        JOIN respi_plot_polygon plpl ON plpl.plot_id = tp_en.plot_id
    WHERE
        tp_en.plot_id = plot_ide;

    --check that the data is complete
    IF  tp_entr_ids IS NULL OR 
        tp_cohort_ids IS NULL OR 
        trm_ids IS NULL OR 
        us_ids IS NULL OR
        mn_ids IS NULL OR
        planting_area_type_ids IS NULL OR 
        pl_points_ids IS NULL OR 
        pl_polygons_ids IS NULL THEN


        --does the plot id exist in respi_fmnr_entry
        SELECT EXISTS(
            SELECT 1 FROM respi_fmnr_entry WHERE plot_id = plot_ide
        ) INTO found_fmnr;

        IF found_fmnr THEN
            found_tables := array_append(found_tables, 'respi_fmnr_entry');
        END IF;

        IF cardinality(found_tables) = 0 THEN
            RETURN format('Plot_id %s seems to be missing. It was NOT found in respi_fmnr_entry either.', plot_ide);
        ELSE
            RETURN format('Please use the delete_fmnr_dpls function for plot_id %s, It was found in the respi_fmnr_entry table ', plot_ide);
        END IF;      
        
    
    END IF;

    --the real work
    --print arrays for debugging
    RAISE NOTICE 'tp entry ids = %', tp_entr_ids;
    RAISE NOTICE 'tp cohort ids = %', tp_cohort_ids;
    RAISE NOTICE 'tree measurement ids = %', trm_ids;
    RAISE NOTICE 'usage ids = %', us_ids;
    RAISE NOTICE 'management ids = %', mn_ids;
    RAISE NOTICE 'planting area type ids = %', planting_area_type_ids;
    RAISE NOTICE 'plot points ids = %', pl_points_ids;
    RAISE NOTICE 'plot polygons ids = %', pl_polygons_ids;

    --delete operation
    DELETE FROM respi_tree_planting_entry WHERE id = ANY(tp_entr_ids);
    DELETE FROM respi_cohort WHERE id = ANY(tp_cohort_ids);
    DELETE FROM respi_tree_measurement WHERE id = ANY(trm_ids);
    DELETE FROM respi_tp_tree_usage WHERE id = ANY(us_ids);
    DELETE FROM respi_tp_management_practices WHERE id = ANY(mn_ids);
    DELETE FROM respi_tp_plantingarea_type WHERE id = ANY(planting_area_type_ids);
    DELETE FROM respi_plot_points WHERE id = ANY(pl_points_ids);
    DELETE FROM respi_plot_polygon WHERE id = ANY(pl_polygons_ids);
    DELETE FROM respi_plots WHERE id = plot_ide;

    RETURN format(
      'Succesfully deleted details for plot id %s: %s entries, %s species, %s measurements, %s usages, %s management practices, %s planting area types, %s plot points, %s plot polygons',
      plot_ide,
      cardinality(tp_entr_ids),
      cardinality(tp_cohort_ids),
      cardinality(trm_ids),
      cardinality(us_ids),
      cardinality(mn_ids),
      cardinality(planting_area_type_ids),
      cardinality(pl_points_ids),
      cardinality(pl_polygons_ids)
    );

END;
$$ LANGUAGE plpgsql;


    