CREATE OR REPLACE FUNCTION delete_fmnr_dpls(plot_ide INTEGER)
RETURNS TEXT AS $$

-- declare variables to hold the ids associated with plot_id input: child tables
DECLARE 
    fmnr_entr_ids INT[];
    fmnr_specie_ids INT[];
    trm_ids INT[];
    us_ids INT[];
    mn_ids INT[];
    pl_points_ids INT[];
    pl_polygons_ids INT[];

    found_tree_planting BOOLEAN;
    found_tables TEXT[] := ARRAY[]::TEXT[];


BEGIN
    SELECT
        array_agg(DISTINCT en.id),
        array_agg(DISTINCT sp.id),
        array_agg(DISTINCT trm.id),
        array_agg(DISTINCT us.id),
        array_agg(DISTINCT mn.id),
        array_agg(DISTINCT plp.id),
        array_agg(DISTINCT plpl.id)
    INTO
        fmnr_entr_ids, 
        fmnr_specie_ids, 
        trm_ids, 
        us_ids, 
        mn_ids, 
        pl_points_ids, 
        pl_polygons_ids
    FROM
        respi_fmnr_entry en
        JOIN respi_fmnr_species sp ON sp.fmnr_entry_id = en.id
        JOIN respi_tree_measurement trm ON trm.fmnr_species_id = sp.id
        JOIN respi_fmnr_tree_usage us ON us.fmnr_species_id = sp.id
        JOIN respi_fmnr_management_practices mn ON mn.fmnr_species_id = sp.id
        JOIN respi_plot_points plp ON plp.plot_id = en.plot_id
        JOIN respi_plot_polygon plpl ON plpl.plot_id = en.plot_id
    WHERE
        en.plot_id = plot_ide;
    
    --check that the data is complete
    IF  fmnr_entr_ids IS NULL OR 
        fmnr_specie_ids IS NULL OR 
        trm_ids IS NULL OR 
        us_ids IS NULL OR 
        mn_ids IS NULL OR 
        pl_points_ids IS NULL OR 
        pl_polygons_ids IS NULL  THEN
        
        --does this plot id exist in respi_tree_planting_entry
        SELECT EXISTS(
            SELECT 1 FROM respi_tree_planting_entry WHERE plot_id = plot_ide
        ) INTO found_tree_planting;

        IF found_tree_planting THEN
            found_tables := array_append(found_tables, 'respi_tree_planting_entry');
        END IF;

        IF cardinality(found_tables) = 0 THEN
            RETURN format('Plot_id %s seems to be missing. It was NOT found in respi_tree_planting_entry either.', plot_ide);
        ELSE
            RETURN format('Please use the delete_tp_dpls function for plot_id %s, It was found in the respi_tree_planting_entry table ', plot_ide);
        END IF;

    END IF;

    --print arrays for debugging:
    RAISE NOTICE 'fmnr entry ids = %', fmnr_entr_ids;
    RAISE NOTICE 'fmnr species ids = %', fmnr_specie_ids;
    RAISE NOTICE 'tree measurement ids = %', trm_ids;
    RAISE NOTICE 'usage ids = %', us_ids;
    RAISE NOTICE 'management ids = %', mn_ids;
    RAISE NOTICE 'plot points ids = %', pl_points_ids;
    RAISE NOTICE 'plot polygons ids = %', pl_polygons_ids;

    -- delete operation
    DELETE FROM respi_fmnr_management_practices WHERE id = ANY(mn_ids);
    DELETE FROM respi_fmnr_tree_usage WHERE id = ANY(us_ids);
    DELETE FROM respi_tree_measurement WHERE id = ANY(trm_ids);
    DELETE FROM respi_fmnr_species WHERE id = ANY(fmnr_specie_ids);
    DELETE FROM respi_fmnr_entry WHERE id = ANY(fmnr_entr_ids);
    DELETE FROM respi_plot_points WHERE id = ANY(pl_points_ids);
    DELETE FROM respi_plot_polygon WHERE id = ANY(pl_polygons_ids);
    DELETE FROM respi_plots WHERE id = plot_ide;


    RETURN format(
      'Succesfully deleted details for plot id %s: %s entries, %s species, %s measurements, %s usages, %s management practices, %s plot points, %s plot polygons',
      plot_ide,
      cardinality(fmnr_entr_ids),
      cardinality(fmnr_specie_ids),
      cardinality(trm_ids),
      cardinality(us_ids),
      cardinality(mn_ids),
      cardinality(pl_points_ids),
      cardinality(pl_polygons_ids)
    );



END;
$$ LANGUAGE plpgsql;

