
# Duplicates - FMNR & TP
- all duplicates are based on 
    1. exactly same lat, lon, from `respi_tree_measurement` 
    2. for a plot occuring more than once.

- cohort_id >> `tp module`
- fmnr-species_id >> `fmnr module`

# TP Plot Duplicates
- Plots have dupicates(name based) but unique ids. e.g. '02993a44-12b0-48d2-8cbc-51d3792eb65e'
```sql
select *
from (
    select 
        plt.id as plot_id,  
        plt.name, 
        plt.crops, 
        row_number() over (partition by name) as row_no,
        ent.recorded_dte, 
        ent.project_id,
        ent.id as tp_entry_id 
    from respi_plots plt
    left join respi_tree_planting_entry ent on ent.plot_id=plt.id 
)
where 
    row_no > 1 and 
    project_id != 6  
limit 300;

 plot_id |                 name                 |                                 crops                                 | row_no |         recorded_dte          | project_id | tp_entry_id
---------+--------------------------------------+-----------------------------------------------------------------------+--------+-------------------------------+------------+-------------
   11830 | 0024392a-9368-4683-8735-c57018665317 | Banana  - Cassava                                                     |      2 | 2025-05-01 18:00:24.48797+03  |         50 |        5654
   12937 | 005b6fd3-814f-44e7-a43e-c14c39f83823 | Plantain  - Yam - Cocoyam - Cassava                                   |      2 | 2025-05-09 20:24:01.143521+03 |        115 |        6726
   15980 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |      2 | 2025-06-16 19:41:17.710342+03 |        122 |        8895
   15977 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |      3 | 2025-06-16 19:26:48.079649+03 |        122 |        8892
   15979 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |      4 | 2025-06-16 19:35:08.808854+03 |        122 |        8894
   15847 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |      5 | 2025-06-11 10:53:46.766512+03 |        122 |        8848
   10998 | 00f8a17f-4377-4079-98ca-e6ea9a109033 |                                                                       |      2 | 2025-03-17 14:58:32.053109+03 |        115 |        5095
   12867 | 01351558-a399-4017-b8c0-c349574d598c | Irish Potato  - Banana - Maize - Cassava Leaves  - Beans              |      2 | 2025-05-09 06:58:45.990595+03 |         50 |        6656
   17086 | 0152ef8f-8cea-4837-affb-1e1af6081e93 | Ibishyimbo - Ibigori - Amasaka - Soya                                 |      2 | 2025-08-11 13:42:12.717741+03 |         41 |        9845
   12612 | 01596ed1-85ca-4839-8efa-031c621bd214 | Banana tree - Beans  - Maize - yams                                   |      2 | 2025-05-08 18:47:39.204047+03 |         50 |        6421
   10430 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |      2 | 2025-02-14 20:10:38.791445+03 |         49 |        4634
   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |      3 | 2025-02-14 20:10:50.854039+03 |         49 |        4635
   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |      4 | 2025-02-14 20:24:04.14025+03  |         49 |        4638
   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |      5 | 2025-02-14 20:21:54.228783+03 |         49 |        4637
    6015 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |      2 | 2024-05-24 14:13:07.93081+03  |         57 |        2789
    6020 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |      3 | 2024-05-24 14:16:56.801123+03 |         57 |        2794
    6036 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |      4 | 2024-05-24 14:40:08.601475+03 |         57 |        2810
   10914 | 04688ac6-bc92-47bf-93a4-c7d8e4cd788e | Potatoes  - Cassava                                                   |      2 | 2025-03-07 17:29:10.499291+03 |        117 |        5013
   10972 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |      2 | 2025-03-12 16:55:51.538691+03 |         49 |        5069
   10969 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |      3 | 2025-03-12 16:47:01.670742+03 |         49 |        5066
   10970 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |      4 | 2025-03-12 16:51:22.276537+03 |         49 |        5067
   13812 | 04e12ae8-b5bf-49e2-9fe7-2ef82c6324a6 | Plantain                                                              |      2 | 2025-05-17 12:24:54.652487+03 |        115 |        7467
   12791 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |      2 | 2025-05-08 21:50:51.026826+03 |         50 |        6584
   12782 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |      3 | 2025-05-08 21:47:37.837653+03 |         50 |        6580
   12641 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |      4 | 2025-05-08 19:02:13.419992+03 |         50 |        6447
   12440 | 058d9904-7451-452a-8d75-9d82f2d06767 |                                                                       |      2 | 2025-05-07 21:06:46.780892+03 |         50 |        6253
:
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
        array_agg(trm.cohort_id) over (partition by ent.id) as cohort_ids_per_plot,
        ent.plot_id, plt.name,
        ch.tp_entry_id,
        trm.comment
    from respi_tree_measurement trm
    left join respi_cohort ch on ch.id = trm.cohort_id 
    left join respi_tree_planting_entry ent on ent.id=ch.tp_entry_id 
    left join respi_plots plt on plt.id = ent.plot_id
) 
where row_number > 1 and cohort_id is not null and name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1';


 trm_id | latitude  | longitude | accuracy | rcc_cbh | row_number | cohort_id |            cohort_ids_per_plot             | plot_id |                 name                 | tp_entry_id |                  comment
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

**Why `row_number()`?**
- to assign a row number to every duplicate(partition) tree measurement(exact lat, lon)
- to delete only where row_number > 1 (skip first record)

**Why `partition by`?** 
- defines the `window` of rows for the function to work on(The function being `row_number()`)
- it returns every individual record in the query.
- 

**why `ARRAY_AGG()`?**
- allows us combine values from multiple rows(`many tree species in the same plot`) into an array

https://www.geeksforgeeks.org/postgresql/postgresql-array_agg-function/

**why aggregate species(`cohort_id`)ids?**

- one plot can have many cohorts(Tree species) `1:M`
    - theres need to delete all trees before deleting the associated plot 
    - to achieve this, we aggregate trees based on plot


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


## tp delete function

```sql
create or replace function clean_tp_dpls(plot_ide integer)
returns void
language plpgsql
as $$
declare 
    r RECORD;
begin
    for r in
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
                ARRAY_AGG(trm.cohort_id) over (partition by ent.id) as cohort_ids_per_plot,
                ent.plot_id, plt.name,
                ch.tp_entry_id,
                trm.comment
            from respi_tree_measurement trm
            left join respi_cohort ch on ch.id = trm.cohort_id 
            left join respi_tree_planting_entry ent on ent.id=ch.tp_entry_id 
            left join respi_plots plt on plt.id = ent.plot_id
        ) 
        where 
            row_number > 1 and 
            cohort_id is not null  and  
            --name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1'and 
            plot_id=plot_ide
    loop
        --delete tp_management_practices
        delete from respi_tp_management_practices where cohort_id = any(r.cohort_ids_per_plot);

        --delete tp_measurement
        delete from respi_tree_measurement where cohort_id = any(r.cohort_ids_per_plot);

        --delete tp_tree_usage
        delete from respi_tp_tree_usage where cohort_id = any(r.cohort_ids_per_plot);

        --delete tp_planting area type
        delete from respi_tp_plantingarea_type where cohort_id = any(r.cohort_ids_per_plot);

        --delete tp_species
        delete from respi_cohort where id = any(r.cohort_ids_per_plot);
    end loop;

        --delete plot crops
        delete from respi_crops where plot_id = plot_ide;

        --delete plot ownership type
        delete from respi_land_ownership_type where plot_id = plot_ide;

        --delete plot points
        delete from respi_plot_points where plot_id = plot_ide;

        --delete plot polygons
        delete from respi_plot_polygon where plot_id = plot_ide;

        --delete plot
        delete from respi_plots where id = plot_ide;

        -- delete tp-entry
        delete from respi_tree_planting_entry where plot_id = plot_ide;
end $$;
```
- Plots have dupicates(name based) but unique ids. e.g. '02993a44-12b0-48d2-8cbc-51d3792eb65e'

# FMNR plot duplicates

- plot name is occuring more than once
- plot is not in test project
- 
```sql
select * 
from (
    select 
        plt.id as plot_id,  
        plt.name, 
        plt.crops, 
        row_number() over (partition by name order by name) as row_no, 
        ent.recorded_dte, 
        ent.project_id,
        ent.id as fmnr_entry_id 
    from 
        respi_plots plt
    left join respi_fmnr_entry ent on ent.plot_id=plt.id 
) where row_no >1 and fmnr_entry_id is not null and project_id != 6;

 plot_id |                 name                 |                                  crops                                  | row_no |         recorded_dte          | project_id | fmnr_entry_id
---------+--------------------------------------+-------------------------------------------------------------------------+-------------+-------------------------------+------------+---------------
    5563 | 00ce2b5b-2d29-45b2-9a06-23f9a48c8698 |                                                                         |           2 | 2024-05-22 12:03:15.959173+03 |         41 |           670
    5423 | 05c072ae-3a44-44ce-bd34-ab6f051771fa |                                                                         |           2 | 2024-05-21 16:43:00.787024+03 |         41 |           656
   15702 | 0704c949-148d-4cb7-a8a9-9e735397b74b | Oil Palm  - Maize - Plantain - Cocoyam                                  |           2 | 2025-06-06 11:37:36.422321+03 |        115 |          3146
   16098 | 0770629e-26d8-43db-96f1-76d1da87dcc9 |                                                                         |           2 | 2025-06-28 11:43:06.248716+03 |         46 |          3234
   16099 | 0770629e-26d8-43db-96f1-76d1da87dcc9 |                                                                         |           3 | 2025-06-28 11:47:24.08046+03  |         46 |          3235
   16097 | 0770629e-26d8-43db-96f1-76d1da87dcc9 |                                                                         |           4 | 2025-06-28 11:42:22.547231+03 |         46 |          3233
   16106 | 0770629e-26d8-43db-96f1-76d1da87dcc9 |                                                                         |           5 | 2025-06-28 12:03:47.373208+03 |         46 |          3238
   16105 | 0770629e-26d8-43db-96f1-76d1da87dcc9 |                                                                         |           6 | 2025-06-28 12:01:02.647781+03 |         46 |          3237
   13386 | 07d85ded-3952-4210-a73f-d997bc10d575 | Maize  - Cassava                                                        |           2 | 2025-05-13 20:17:09.640238+03 |        115 |          2720
   13385 | 07d85ded-3952-4210-a73f-d997bc10d575 | Maize  - Cassava                                                        |           3 | 2025-05-13 20:16:20.808888+03 |        115 |          2719
    5407 | 080639eb-4f5b-4d9b-8da9-9e23bbb373ed |                                                                         |           2 | 2024-05-21 16:31:31.423507+03 |         41 |           643
    5784 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 | Irish Potatoes                                                          |           2 | 2024-05-22 13:37:08.499787+03 |         41 |           740
    5789 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 | Irish Potatoes                                                          |           3 | 2024-05-22 13:37:39.433546+03 |         41 |           745
    5791 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 | Irish Potatoes                                                          |           4 | 2024-05-22 13:37:58.597947+03 |         41 |           747
    8119 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |                                                                         |           2 | 2024-11-02 13:57:54.380318+03 |         46 |          2273
    8098 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |                                                                         |           3 | 2024-11-02 13:19:13.770393+03 |         46 |          2256
    8094 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |                                                                         |           4 | 2024-11-02 13:12:52.243469+03 |         46 |          2252
    8096 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |                                                                         |           5 | 2024-11-02 13:17:14.431161+03 |         46 |          2254
    8111 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |                                                                         |           6 | 2024-11-02 13:54:18.947786+03 |         46 |          2269
   15706 | 130b463e-4c8a-46c0-bae2-3f101cd41517 | Plantain - Cocoyam  - Cassava                                           |           2 | 2025-06-06 11:41:36.241921+03 |        115 |          3149
    8881 | 135619c7-d5ea-4859-ab48-084be591bfb5 |                                                                         |           2 | 2024-12-18 11:40:45.412312+03 |         46 |          2578
    8882 | 135619c7-d5ea-4859-ab48-084be591bfb5 |                                                                         |           3 | 2024-12-18 11:45:33.480329+03 |         46 |          2579
    8877 | 135619c7-d5ea-4859-ab48-084be591bfb5 |                                                                         |           4 | 2024-12-18 11:25:20.323121+03 |         46 |          2574
    8876 | 135619c7-d5ea-4859-ab48-084be591bfb5 |                                                                         |           5 | 2024-12-18 11:21:34.381843+03 |         46 |          2573
   14912 | 15a4d5cb-9aef-4668-8b7f-ea128abf2776 | Plantain - Cassava                                                      |           2 | 2025-05-25 23:43:15.864392+03 |        115 |          2913
    6954 | 1cf4ddf3-611b-40b2-a6a4-3a561c79132d |                                                                         |           2 | 2024-10-10 18:58:33.506569+03 |         93 |          1307
    4577 | 1d1e4216-9b2a-4b82-8abe-20c5d568a6b7 |                                                                         |           2 | 2024-05-08 12:43:49.847443+03 |         41 |           367
   12857 | 1ff3cadb-6fcb-4fcb-903f-7f51bd6ef4e4 | Maize  - Cassava  - Plantain                                            |           2 | 2025-05-08 23:29:00.656099+03 |        115 |          2691
    7716 | 2295b9d7-a8fd-4359-adef-fc38dc68930b |                                                                         |           2 | 2024-10-30 08:31:13.86178+03  |         46 |          2041
    7709 | 2295b9d7-a8fd-4359-adef-fc38dc68930b |                                                                         |           3 | 2024-10-29 13:56:48.830003+03 |         46 |          2034
   11164 | 22b1d6a1-9350-4f6e-9c26-9141402559e2 |                                                                         |           2 | 2025-03-27 14:43:59.57874+03  |         93 |          2661
   11160 | 22b1d6a1-9350-4f6e-9c26-9141402559e2 |                                                                         |           3 | 2025-03-27 14:41:46.833224+03 |         93 |          2657
   11159 | 22b1d6a1-9350-4f6e-9c26-9141402559e2 |                                                                         |           4 | 2025-03-27 14:27:50.687352+03 |         93 |          2656
   11165 | 22b1d6a1-9350-4f6e-9c26-9141402559e2 |                                                                         |           5 | 2025-03-27 14:44:26.153206+03 |         93 |          2662
    6656 | 284c6068-20c2-4e27-b54f-a2e368db2861 |                                                                         |           2 | 2024-08-27 14:45:04.174701+03 |         87 |          1130
    6645 | 284c6068-20c2-4e27-b54f-a2e368db2861 |                                                                         |           3 | 2024-08-27 12:03:01.189729+03 |         87 |          1122
    6647 | 284c6068-20c2-4e27-b54f-a2e368db2861 |                                                                         |           4 | 2024-08-27 12:05:46.106536+03 |         87 |          1124
    6646 | 284c6068-20c2-4e27-b54f-a2e368db2861 |                                                                         |           5 | 2024-08-27 12:03:40.439833+03 |         87 |          1123
    6517 | 2fdf5641-d336-4da7-b160-af041cbd61fc | Maize                                                                   |           2 | 2024-08-01 13:17:59.062227+03 |         87 |          1035
    5777 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           2 | 2024-05-22 13:35:06.719638+03 |         41 |           733
    5863 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           3 | 2024-05-22 14:01:42.443262+03 |         41 |           819
    5864 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           4 | 2024-05-22 14:01:46.9608+03   |         41 |           820
    5828 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           5 | 2024-05-22 13:46:41.940357+03 |         41 |           784
    5829 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           6 | 2024-05-22 13:46:50.706911+03 |         41 |           785
    5983 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           7 | 2024-05-23 17:57:17.287993+03 |         41 |           877
    5803 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           8 | 2024-05-22 13:42:30.182855+03 |         41 |           759
    5781 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |           9 | 2024-05-22 13:35:37.6942+03   |         41 |           737
    5875 | 342e62a7-d299-4064-a557-62a1ead6300a |                                                                         |          10 | 2024-05-22 14:04:24.334092+03 |         41 |           831
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
        row_number() over (partition by trm.latitude, trm.longitude order by trm.latitude desc, trm.longitude desc) as row_num, 
        trm.fmnr_species_id,
        array_agg(trm.fmnr_species_id) over (partition by plt.id) as sp_ids_per_plot,
        sp.fmnr_entry_id, 
        plt.id as plot_id, 
        plt.name,         
        trm.comment 
    from 
        respi_tree_measurement trm 
    left join respi_fmnr_species sp on sp.id=trm.fmnr_species_id 
    left join respi_fmnr_entry ent on ent.id=sp.fmnr_entry_id 
    left join respi_plots plt on plt.id=ent.plot_id
)
where 
    fmnr_species_id is not null and 
    row_num > 1 and 
    name = 'e7ef9b4c-8c19-4faf-ad70-5583722333d8';
 trm_id | latitude  | longitude | accuracy | row_num | fmnr_species_id |                     sp_ids_per_plot                     | fmnr_entry_id | plot_id |                 name                 | comment
--------+-----------+-----------+----------+---------+-----------------+----------------------------------------------------------+---------------+---------+--------------------------------------+---------
  14122 | 13.499581 | 39.603302 |     6.70 |       2 |            6075 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14100 | 13.499581 | 39.603302 |     6.70 |       3 |            6053 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14102 | 13.499450 | 39.603488 |     7.25 |       2 |            6055 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14124 | 13.499450 | 39.603488 |     7.25 |       3 |            6077 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14123 | 13.499428 | 39.603545 |     6.42 |       2 |            6076 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14101 | 13.499428 | 39.603545 |     6.42 |       3 |            6054 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14103 | 13.499412 | 39.603633 |     9.00 |       2 |            6056 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14125 | 13.499412 | 39.603633 |     9.00 |       3 |            6078 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14104 | 13.499376 | 39.603642 |     9.38 |       2 |            6057 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14126 | 13.499376 | 39.603642 |     9.38 |       3 |            6079 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14105 | 13.499102 | 39.603890 |     9.00 |       2 |            6058 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14116 | 13.499102 | 39.603890 |     9.00 |       3 |            6069 | {6072,6065,6074,6073,6071,6070,6069,6068,6067,6066,6064} |          2586 |    8897 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14128 | 13.498853 | 39.603904 |     7.00 |       2 |            6081 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14117 | 13.498853 | 39.603904 |     7.00 |       3 |            6070 | {6072,6065,6074,6073,6071,6070,6069,6068,6067,6066,6064} |          2586 |    8897 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14107 | 13.498448 | 39.603922 |     7.00 |       2 |            6060 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14129 | 13.498448 | 39.603922 |     7.00 |       3 |            6082 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14130 | 13.498433 | 39.603897 |     8.33 |       2 |            6083 | {6080,6081,6075,6076,6077,6084,6085,6079,6078,6083,6082} |          2587 |    8898 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14108 | 13.498433 | 39.603897 |     8.33 |       3 |            6061 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14109 | 13.497947 | 39.604086 |     9.33 |       2 |            6062 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14120 | 13.497947 | 39.604086 |     9.33 |       3 |            6073 | {6072,6065,6074,6073,6071,6070,6069,6068,6067,6066,6064} |          2586 |    8897 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14110 | 13.497901 | 39.604050 |     6.88 |       2 |            6063 | {6060,6059,6058,6057,6054,6056,6055,6053,6063,6062,6061} |          2585 |    8896 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
  14121 | 13.497901 | 39.604050 |     6.88 |       3 |            6074 | {6072,6065,6074,6073,6071,6070,6069,6068,6067,6066,6064} |          2586 |    8897 | e7ef9b4c-8c19-4faf-ad70-5583722333d8 |
(22 rows)
```
## fmnr delete function

```sql
create or replace function clean_fmnr_dpls(plot_ide integer)
returns void
language plpgsql
as $$
declare
    r RECORD;
begin
    for r in
        select *
        from (
            select
                trm.id as trm_id,
                trm.latitude,
                trm.longitude,
                trm.accuracy,
                row_number() over (partition by trm.latitude, trm.longitude order by trm.latitude desc, trm.longitude desc) as row_num,
                trm.fmnr_species_id,
                array_agg(trm.fmnr_species_id) over (partition by plt.id) as sp_ids_per_plot,
                sp.fmnr_entry_id,
                plt.id as plot_id,
                plt.name,     
                trm.comment
            from
                respi_tree_measurement trm
            left join respi_fmnr_species sp on sp.id=trm.fmnr_species_id
            left join respi_fmnr_entry ent on ent.id=sp.fmnr_entry_id
            left join respi_plots plt on plt.id=ent.plot_id
        )
        where
            row_num > 1 and
            fmnr_species_id is not null and
            plot_id=plot_ide
            --and  name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1'     

    loop
        --delete fmnr_management_practices
        delete from respi_fmnr_management_practices where fmnr_species_id = any(r.sp_ids_per_plot);

        --delete fmnr_measurement
        delete from respi_tree_measurement where fmnr_species_id = any(r.sp_ids_per_plot);

        --delete fmnr_tree_usage
        delete from respi_fmnr_tree_usage where fmnr_species_id = any(r.sp_ids_per_plot);

        --delete fmnr_species
        delete from respi_fmnr_species where id = any(r.sp_ids_per_plot);
    end loop;

        --delete plot crops
        delete from respi_crops where plot_id = plot_ide;

        --delete plot ownership type
        delete from respi_land_ownership_type where plot_id = plot_ide;

        --delete plot points
        delete from respi_plot_points where plot_id = plot_ide;

        --delete plot polygons
        delete from respi_plot_polygon where plot_id = plot_ide;

        --delete plot
        delete from respi_plots where id = plot_ide;

        -- delete fmnr-entry
        delete from respi_fmnr_entry where plot_id = plot_ide;
end $$;

```