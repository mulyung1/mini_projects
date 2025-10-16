CREATE OR REPLACE FUNCTION delete_dpls(plot_ide INTEGER)
RETURNS TEXT AS $$
DECLARE 
    fmnr_entr_ids INT[];
    fmnr_specie_ids INT[];
    trm_ids INT[];
    us_ids INT[];
    mn_ids INT[];
    pl_points_ids INT[];
    pl_polygons_ids INT[];

    found_nursery BOOLEAN;
    found_rangeland BOOLEAN;
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
        fmnr_entr_ids, fmnr_specie_ids, trm_ids, us_ids, mn_ids, pl_points_ids, pl_polygons_ids
    FROM 
        respi_fmnr_entry en 
        JOIN respi_fmnr_species sp ON sp.fmnr_entry_id = en.id 
        JOIN respi_tree_measurement trm ON trm.fmnr_species_id = sp.id 
        JOIN respi_fmnr_tree_usage us ON us.fmnr_species_id = sp.id 
        JOIN respi_fmnr_management_practices mn ON mn.fmnr_species_id = sp.id 
        JOIN respi_plot_points plp ON plp.plot_id=en.plot_id 
        JOIN respi_plot_polygon plpl ON plpl.plot_id=en.plot_id 
    WHERE 
        en.plot_id = plot_ide;

    -- IF fmnr_entr_ids IS NULL OR fmnr_specie_ids IS NULL OR trm_ids IS NULL OR us_ids IS NULL OR mn_ids IS NULL OR pl_points_ids IS NULL OR pl_polygons_ids IS NULL THEN
    --     RETURN format('We are missing some data for plot_id %s', plot_ide);
    -- END IF;
    IF fmnr_entr_ids IS NULL OR fmnr_specie_ids IS NULL OR trm_ids IS NULL OR us_ids IS NULL OR mn_ids IS NULL OR pl_points_ids IS NULL OR pl_polygons_ids IS NULL THEN
        -- check the three other tables for the plot id
        SELECT EXISTS (SELECT 1 FROM respi_nursery_entry WHERE nursery_id = plot_ide) INTO found_nursery;
        SELECT EXISTS (SELECT 1 FROM respi_rangeland_entry WHERE plot_id = plot_ide) INTO found_rangeland;
        SELECT EXISTS (SELECT 1 FROM respi_tree_planting_entry WHERE plot_id = plot_ide) INTO found_tree_planting;

        -- --(use array_append)
        IF found_nursery THEN
            found_tables := array_append(found_tables, 'respi_nursery_entry');
        END IF;

        IF found_rangeland THEN
            found_tables := array_append(found_tables, 'respi_rangeland_entry');
        END IF;

        IF found_tree_planting THEN
            found_tables := array_append(found_tables, 'respi_tree_planting_entry');
        END IF;

        IF cardinality(found_tables) = 0 THEN
            RAISE NOTICE 'Plot % was NOT found in respi_nursery_entry, respi_rangeland_entry, or respi_tree_planting_entry.', plot_ide;
            RETURN format('We are missing some data for plot_id %s. Found in: none', plot_ide);
        ELSE
            RAISE NOTICE 'Plot % found in : %', plot_ide, array_to_string(found_tables, ', ');
            RETURN format('We are missing some data for plot_id %s. Found in: %s', plot_ide, array_to_string(found_tables, ', '));
        END IF;

    END IF;

    -- Print arrays for debugging:
    RAISE NOTICE 'fmnr entry ids = %', fmnr_entr_ids;
    RAISE NOTICE 'fmnr species ids = %', fmnr_specie_ids;
    RAISE NOTICE 'tree measurement ids = %', trm_ids;
    RAISE NOTICE 'usage ids = %', us_ids;
    RAISE NOTICE 'management ids = %', mn_ids;

    
    --delete logic...
    -- DELETE FROM respi_fmnr_management_practices WHERE id = ANY(mn_ids);
    -- DELETE FROM respi_fmnr_tree_usage WHERE id = ANY(us_ids);
    -- DELETE FROM respi_tree_measurement WHERE id = ANY(trm_ids);
    -- DELETE FROM respi_fmnr_species WHERE id = ANY(fmnr_specie_ids);
    -- DELETE FROM respi_fmnr_entry WHERE id = ANY(fmnr_entr_ids);
    -- DELETE FROM respi_plot_points WHERE id = ANY(pl_points_ids);
    -- DELETE FROM respi_plot_polygon WHERE id = ANY(pl_polygons_ids);
    -- DELETE FROM respi_plots WHERE id = plot_ide;

    -- RETURN format(
    --   'Succesfully completed deletion of plot %s: %s entries, %s species, %s measurements',
    --   plot_ide,
    --   array_length(fmnr_entr_ids,1),
    --   array_length(fmnr_specie_ids,1),
    --   array_length(trm_ids,1)
    -- );


    RETURN format(
      'Succesfully found details for plot %s: %s entries, %s species, %s measurements',
      plot_ide,
      array_length(fmnr_entr_ids,1),
      array_length(fmnr_specie_ids,1),
      array_length(trm_ids,1)
    );





END;
$$ LANGUAGE plpgsql;



