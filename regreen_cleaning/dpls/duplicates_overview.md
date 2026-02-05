
# Duplicates - FMNR & TP
- all duplicates are based on 
    1. exactly same lat, lon, from `respi_tree_measurement` 
    2. for a plot occuring more than once.

- cohort_id >> `tp module`
- fmnr-species_id >> `fmnr module`

## Plot Duplicates
- Plots have dupicates(name based) but unique ids. e.g. '02993a44-12b0-48d2-8cbc-51d3792eb65e'
```sql
select 
    dpls.plot_id, 
    dpls.name, 
    dpls.crops,
    dpls.plot_row_no, 
    ent.recorded_dte, 
    ent.project_id,
    ent.id as tp_entry_id 
from (
    select 
        id as plot_id,  
        name, 
        crops, 
        row_number() over (partition by name) as plot_row_no 
    from respi_plots) dpls 
    left join respi_tree_planting_entry ent on ent.plot_id=dpls.plot_id 
    where 
        plot_row_no > 1 and 
        ent.project_id != 6  
    limit 300;

 plot_id |                 name                 |                                 crops                                 | plot_row_no |         recorded_dte          | project_id | tp_entry_id
---------+--------------------------------------+-----------------------------------------------------------------------+-------------+-------------------------------+------------+-------------
   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           2 | 2025-02-14 20:24:04.14025+03  |         49 |        4638
   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           3 | 2025-02-14 20:21:54.228783+03 |         49 |        4637
   10432 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           4 | 2025-02-14 20:11:33.438573+03 |         49 |        4636
   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           5 | 2025-02-14 20:10:50.854039+03 |         49 |        4635
    6036 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           2 | 2024-05-24 14:40:08.601475+03 |         57 |        2810
    6031 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           3 | 2024-05-24 14:37:15.411662+03 |         57 |        2805
```

## Measurement Duplicates
- These duplicated plots have repeating tree measurements 

```sql
select *
from (
    select
        trm.id as trm_id, 
        trm.latitude,
        trm.longitude,
        trm.accuracy,
        trm.rcc_cbh,
        row_number() over (
            partition by trm.latitude, trm.longitude
            order by trm.latitude desc, trm.longitude desc
        ) as row_number,
        trm.cohort_id,
        array_agg(trm.cohort_id) over (partition by ent.id) as cohort_ids_per_entry,
        ent.plot_id, plt.name,
        ch.tp_entry_id,
        trm.comment
    from respi_tree_measurement trm
    left join respi_cohort ch on ch.id = trm.cohort_id 
    left join respi_tree_planting_entry ent on ent.id=ch.tp_entry_id 
    left join respi_plots plt on plt.id = ent.plot_id
) 
where row_number > 1 and  name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1';


 trm_id | latitude  | longitude | accuracy | rcc_cbh | row_number | cohort_id |            cohort_ids_per_entry             | plot_id |                 name                 | tp_entry_id |                  comment
--------+-----------+-----------+----------+---------+------------+-----------+---------------------------------------------+---------+--------------------------------------+-------------+-------------------------------------------
  16595 | -1.299590 | 30.553325 |     6.50 |    0.90 |          2 |     10674 | {10668,10669,10670,10671,10672,10673,10674} |   10410 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4615 | Moderate survival rated planted in apiary
  16490 | -1.299590 | 30.553325 |     6.50 |    0.90 |          3 |     10569 | {10563,10564,10565,10566,10567,10568,10569} |   10384 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4591 | Moderate survival rated planted in apiary
  16588 | -1.299590 | 30.553325 |     6.50 |    0.90 |          4 |     10667 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | Moderate survival rated planted in apiary
  16574 | -1.299590 | 30.553325 |     6.50 |    0.90 |          5 |     10653 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | Moderate survival rated planted in apiary
  16547 | -1.299590 | 30.553325 |     6.50 |    0.90 |          6 |     10626 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | Moderate survival rated planted in apiary
  16560 | -1.299590 | 30.553325 |     6.50 |    0.90 |          7 |     10639 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | Moderate survival rated planted in apiary
  16566 | -1.299605 | 30.553887 |     0.68 |    1.20 |          2 |     10645 | {10640,10641,10642,10643,10644,10645,10646} |   10406 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4611 | high survival rate planted near by apiary
  16559 | -1.299605 | 30.553887 |     0.68 |    1.20 |          3 |     10638 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | high survival rate planted near by apiary
  16594 | -1.299605 | 30.553887 |     0.68 |    1.20 |          4 |     10673 | {10668,10669,10670,10671,10672,10673,10674} |   10410 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4615 | high survival rate planted near by apiary
  16587 | -1.299605 | 30.553887 |     0.68 |    1.20 |          5 |     10666 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | high survival rate planted near by apiary
  16546 | -1.299605 | 30.553887 |     0.68 |    1.20 |          6 |     10625 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | high survival rate planted near by apiary
  16573 | -1.299605 | 30.553887 |     0.68 |    1.20 |          7 |     10652 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | high survival rate planted near by apiary
  16586 | -1.299662 | 30.553655 |     7.44 |    0.60 |          2 |     10665 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | high growth rate
  16565 | -1.299662 | 30.553655 |     7.44 |    0.60 |          3 |     10644 | {10640,10641,10642,10643,10644,10645,10646} |   10406 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4611 | high growth rate
  16572 | -1.299662 | 30.553655 |     7.44 |    0.60 |          4 |     10651 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | high growth rate
  16558 | -1.299662 | 30.553655 |     7.44 |    0.60 |          5 |     10637 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | high growth rate
  16593 | -1.299662 | 30.553655 |     7.44 |    0.60 |          6 |     10672 | {10668,10669,10670,10671,10672,10673,10674} |   10410 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4615 | high growth rate
  16545 | -1.299662 | 30.553655 |     7.44 |    0.60 |          7 |     10624 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | high growth rate
  16585 | -1.300455 | 30.553559 |     1.67 |    3.00 |          2 |     10664 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | high survival and growth rate
  16557 | -1.300455 | 30.553559 |     1.67 |    3.00 |          3 |     10636 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | high survival and growth rate
  16487 | -1.300455 | 30.553559 |     1.67 |    3.00 |          4 |     10566 | {10563,10564,10565,10566,10567,10568,10569} |   10384 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4591 | high survival and growth rate
  16592 | -1.300455 | 30.553559 |     1.67 |    3.00 |          5 |     10671 | {10668,10669,10670,10671,10672,10673,10674} |   10410 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4615 | high survival and growth rate
  16571 | -1.300455 | 30.553559 |     1.67 |    3.00 |          6 |     10650 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | high survival and growth rate
  16544 | -1.300455 | 30.553559 |     1.67 |    3.00 |          7 |     10623 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | high survival and growth rate
  16570 | -1.300478 | 30.553588 |    14.83 |    1.60 |          2 |     10649 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | high survival and growth rate
  16543 | -1.300478 | 30.553588 |    14.83 |    1.60 |          3 |     10622 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | high survival and growth rate
  16486 | -1.300478 | 30.553588 |    14.83 |    1.60 |          4 |     10565 | {10563,10564,10565,10566,10567,10568,10569} |   10384 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4591 | high survival and growth rate
  16556 | -1.300478 | 30.553588 |    14.83 |    1.60 |          5 |     10635 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | high survival and growth rate
  16591 | -1.300478 | 30.553588 |    14.83 |    1.60 |          6 |     10670 | {10668,10669,10670,10671,10672,10673,10674} |   10410 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4615 | high survival and growth rate
  16584 | -1.300478 | 30.553588 |    14.83 |    1.60 |          7 |     10663 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | high survival and growth rate
  16484 | -1.300531 | 30.553982 |     5.49 |    0.90 |          2 |     10563 | {10563,10564,10565,10566,10567,10568,10569} |   10384 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4591 | high growth rate
  16554 | -1.300531 | 30.553982 |     5.49 |    0.90 |          3 |     10633 | {10636,10637,10638,10639,10633,10634,10635} |   10405 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4610 | high growth rate
  16568 | -1.300531 | 30.553982 |     5.49 |    0.90 |          4 |     10647 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | high growth rate
  16561 | -1.300531 | 30.553982 |     5.49 |    0.90 |          5 |     10640 | {10640,10641,10642,10643,10644,10645,10646} |   10406 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4611 | high growth rate
  16582 | -1.300531 | 30.553982 |     5.49 |    0.90 |          6 |     10661 | {10661,10662,10663,10664,10665,10666,10667} |   10409 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4614 | high growth rate
  16541 | -1.300531 | 30.553982 |     5.49 |    0.90 |          7 |     10620 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | high growth rate
  16542 | -1.300563 | 30.553803 |     7.27 |    0.80 |          2 |     10621 | {10626,10620,10621,10622,10623,10624,10625} |   10400 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4605 | low survival rate
  16569 | -1.300563 | 30.553803 |     7.27 |    0.80 |          3 |     10648 | {10647,10648,10649,10650,10651,10652,10653} |   10407 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4612 | low survival rate
  16562 | -1.300563 | 30.553803 |     7.27 |    0.80 |          4 |     10641 | {10640,10641,10642,10643,10644,10645,10646} |   10406 | 06a139a3-29a9-474a-8b94-479e9c8d6cc1 |        4611 | low survival rate

```

**Proposed solution**

- get all duplicates for one plot
- based on id, check if all duplicated plots have same number of duplicates
- choose one plot to retain
- the rest, delete tree and plot info(including plot ownership, planting area, crops...)

**Philosophy**
- we will not consider `TEST` project

**Why `ROW_NUMBER()`?**
- to assign a row number to every duplicate(partition) tree measurement(exact lat, lon)
- to delete only where row_number > 1 (skip first record)

**Why `PARTITION BY`?** 
- defines the `window` of rows for the function to work on(The function being `ROW_NUMBER()`)
- it returns every individual record in the query.
- 

**why `ARRAY_AGG()`?**
- allows us combine values from multiple rows(`many tree species in the same tp_entry`) into an array

https://www.geeksforgeeks.org/postgresql/postgresql-array_agg-function/

**why aggregate species(`cohort_id`)ids?**

- one entry can have many cohorts(Tree species) `1:M`
    - theres need to delete all trees before deleting an entry 
    - to achieve this, we aggregate trees based on entry

- one tp plot has 1 tp entry but 
    - one plot can have many entries `1:M`
        - fmnr entries
        - rangeland entries
        - etc...


### related tables to delete from

delete all rows in tables below based on `cohort_id` & `plot_id`
- respi_tp_management_practices - `cohort_id`
- respi_tree_measurement - `cohort_id`
- respi_tp_tree_usage - `cohort_id`
- respi_tp_plantingarea_type - `cohort_id`
- respi_cohort - `cohort_id`
- respi_tree_planting_entry - `plot_id`
- respi_crops - `plot_id`
- respi_land_ownership_type - `plot_id`
- respi_plot_points  - `plot_id`
- respi_plot_polygon  - `plot_id`
- respi_plots - `plot_id`


## delete function

```sql
CREATE OR REPLACE FUNCTION clean_dpls(plot_ide integer)
RETURNS void
LANGUAGE plpgsql
AS $$
DECLARE 
    r RECORD;
BEGIN
    FOR r IN
        SELECT *
        FROM (
            SELECT
                trm.id as trm_id, 
                trm.latitude,
                trm.longitude,
                trm.accuracy,
                trm.rcc_cbh,
                ROW_NUMBER() OVER (
                    PARTITION BY trm.latitude, trm.longitude
                    ORDER BY trm.latitude desc, trm.longitude desc
                ) AS row_number,
                trm.cohort_id, 
                ARRAY_AGG(trm.cohort_id) OVER (PARTITION BY ent.id) AS cohort_ids_per_entry,
                ent.plot_id, plt.name,
                ch.tp_entry_id,
                trm.comment
            FROM respi_tree_measurement trm
            LEFT JOIN respi_cohort ch ON ch.id = trm.cohort_id 
            LEFT JOIN respi_tree_planting_entry ent ON ent.id=ch.tp_entry_id 
            LEFT JOIN respi_plots plt ON plt.id = ent.plot_id
        ) 
        WHERE row_number > 1 AND plot_id=plot_ide --AND  name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1'     

    LOOP
        --delete tp_management_practices
        DELETE FROM respi_tp_management_practices WHERE cohort_id = ANY(r.cohort_ids_per_entry);

        --delete tp_measurement
        DELETE FROM respi_tree_measurement WHERE cohort_id = ANY(r.cohort_ids_per_entry);

        --delete tp_tree_usage
        DELETE FROM respi_tp_tree_usage WHERE cohort_id = ANY(r.cohort_ids_per_entry);

        --delete tp_planting area type
        DELETE FROM respi_tp_plantingarea_type WHERE cohort_id = ANY(r.cohort_ids_per_entry);

        --delete tp_species
        DELETE FROM respi_cohort WHERE id = ANY(r.cohort_ids_per_entry);
    END LOOP;

        --delete plot crops
        DELETE FROM respi_crops WHERE plot_id = plot_ide;

        --delete plot ownership type
        DELETE FROM respi_land_ownership_type WHERE plot_id = plot_ide;

        --delete plot points
        DELETE FROM respi_plot_points where plot_id = plot_ide;

        --delete plot polygons
        DELETE FROM respi_plot_polygon where plot_id = plot_ide;

        --delete plot
        DELETE FROM respi_plots where id = plot_ide;

        -- delete tp-entry
        DELETE FROM respi_tree_planting_entry where plot_id = plot_ide;
    
END $$;
```