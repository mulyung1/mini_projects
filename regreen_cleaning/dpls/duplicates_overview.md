# Duplicates
The regreen db has duplicates.

We will explore them module by module.

- [FMNR & TP Duplicates](#fmnr--tp-duplicates)
    - [TP Plot Duplicates](#tp-plot-duplicates)
        - [Measurement Duplicates](#measurement-duplicates)
        - [related tables to delete from](#related-tables-to-delete-from)
        - [tp delete function](#tp-delete-function)
    - [FMNR plot duplicates](#fmnr-plot-duplicates)
        - [Measurement Duplicates](#measurement-duplicates-1)
        - [related tables to delete from](#related-tables-to-delete-from-1)
        - [fmnr delete function](#fmnr-delete-function)
    - [Nursery Duplicates](#nursery-duplicates)
        - [case study: Christine Tree Nursery, REGREENING AFRICA_CHILDFUND project](#case-study-christine-tree-nursery-regreening-africa_childfund-project)

## FMNR & TP Duplicates 

- all duplicates are based on 
    1. exactly same lat, lon, from `respi_tree_measurement` 
    2. for a plot occuring more than once.

- cohort_id >> `tp module`
- fmnr-species_id >> `fmnr module`

### TP Plot Duplicates
- Plots have dupicates(name based) but unique ids. e.g. '02993a44-12b0-48d2-8cbc-51d3792eb65e'
- keep only plots with tp entries `inner join`
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
        ent.id as tp_entry_id, fent.first_name, proj.project_name
    from respi_plots plt
    inner join respi_tree_planting_entry ent on ent.plot_id=plt.id 
    left join respi_farming_entity fent on fent.id=plt.farming_entity_id 
    left join respi_projects proj on proj.id=ent.project_id
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

#### Measurement Duplicates
- These duplicated plots have repeating tree measurements 
- only tree msmts with a cohort_id(tp module) survive
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
        array_agg(trm.cohort_id) over (partition by ent.plot_id) as cohort_ids_per_plot,
        ent.plot_id, plt.name,
        ch.tp_entry_id,
        trm.comment
    from respi_tree_measurement trm
    inner join respi_cohort ch on ch.id = trm.cohort_id 
    left join respi_tree_planting_entry ent on ent.id=ch.tp_entry_id 
    left join respi_plots plt on plt.id = ent.plot_id
) 
where 
    row_number > 1 and name = '06a139a3-29a9-474a-8b94-479e9c8d6cc1';


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
- choose one plot to retain(first one)
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


#### related tables to delete from

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


#### tp delete function

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
            inner join respi_cohort ch on ch.id = trm.cohort_id 
            left join respi_tree_planting_entry ent on ent.id=ch.tp_entry_id 
            left join respi_plots plt on plt.id = ent.plot_id
        ) 
        where 
            row_number > 1 and 
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

### FMNR plot duplicates
- plot name is occuring more than once
- plot has fmnr entry `inner join`
- plot is not in test project
- 
**check for only plots with fmnr entry**
```sql
select count(*)     
from
    respi_plots plt
left join respi_fmnr_entry ent on ent.plot_id=plt.id ;
 count
-------
 17512
(1 row)

--only plots with fmnr entries
select count(*)     
from
    respi_plots plt
inner join respi_fmnr_entry ent on ent.plot_id=plt.id ;
 count
-------
  2531
(1 row)

```
assgn row numbers to plot names that are recurring

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
    inner join respi_fmnr_entry ent on ent.plot_id=plt.id 
) where row_no >1 and project_id != 6;

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

#### Measurement Duplicates
- These duplicated plots have repeating tree measurements 
- keep only tree msmt rows with fmnr_species id

**check for only tree msmts with fmnr species**

```sql
select count(*) 
from 
    respi_tree_measurement trm
left join respi_fmnr_species sp on sp.id=trm.fmnr_species_id
left join respi_fmnr_entry ent on ent.id=sp.fmnr_entry_id
left join respi_plots plt on plt.id=ent.plot_id;

 count
-------
 44764
(1 row)
--only tree msmt rows with fmnr_species id

select count(*) 
from
    respi_tree_measurement trm
inner join respi_fmnr_species sp on sp.id=trm.fmnr_species_id
left join respi_fmnr_entry ent on ent.id=sp.fmnr_entry_id
left join respi_plots plt on plt.id=ent.plot_id;
 count
-------
  5766
(1 row)


```


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
    inner join respi_fmnr_species sp on sp.id=trm.fmnr_species_id 
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

#### related tables to delete from
delete all rows in tables below based on `species_id` & `plot_id`

- respi_fmnr_management_practices - `species_id`
- respi_tree_measurement - `species_id`
- respi_fmnr_tree_usage - `species_id`
- respi_fmnr_species - `species_id`
- respi_crops - `plot_id`
- respi_land_ownership_type - `plot_id`
- respi_plot_points - `plot_id`
- respi_plot_polygon - `plot_id`
- respi_plots - `plot_id`
- respi_fmnr_entry - `plot_id`


#### fmnr delete function

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
            inner join respi_fmnr_species sp on sp.id=trm.fmnr_species_id
            left join respi_fmnr_entry ent on ent.id=sp.fmnr_entry_id
            left join respi_plots plt on plt.id=ent.plot_id
        )
        where
            row_num > 1 and
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

## Nursery Duplicates

**Questions**
- Dow we expect nursery name to be unique?
```sql
  id  |         recorded_dte          |                              nursery_name                              | altitude |  latitude  | longitude  | accuracy | species_count | nursery_operator_id | nursery_ownership_type_id | project_id | sub_county_id |                             photo_url                             | date_started |           other_ownership_type           |        water_sources         |           other_water_sources
------+-------------------------------+------------------------------------------------------------------------+----------+------------+------------+----------+---------------+---------------------+---------------------------+------------+---------------+-------------------------------------------------------------------+--------------+------------------------------------------+------------------------------+------------------------------------------
  315 | 2024-03-04 15:10:42.095918+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       451 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  268 | 2024-02-28 15:35:48.534494+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       394 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  270 | 2024-02-28 16:39:54.203248+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       397 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  273 | 2024-02-28 17:53:05.70254+03  |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       401 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  266 | 2024-02-28 15:35:42.140915+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       391 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  287 | 2024-02-29 15:27:53.867657+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       418 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  303 | 2024-03-04 10:31:02.126074+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       437 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  358 | 2024-03-26 10:21:38.59253+03  |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       498 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  265 | 2024-02-28 15:30:42.176626+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       390 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  308 | 2024-03-04 11:57:22.329134+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       443 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  292 | 2024-02-29 16:33:48.934263+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       424 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  277 | 2024-02-29 09:43:04.536331+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       406 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  299 | 2024-02-29 16:42:06.977649+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       432 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  280 | 2024-02-29 15:27:43.826881+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       410 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  324 | 2024-03-05 17:20:41.528573+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       461 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  345 | 2024-03-26 10:20:23.172289+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       484 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
  336 | 2024-03-12 12:41:26.395875+03 |    Christine Tree Nursery                                              | 1188.508 |  -2.017078 |  37.462925 |     3.90 |             4 |                 111 |                       474 |         44 |           494 | JPEG_eaa225a4-2d4b-4110-988c-de291447fba7_3089708158651942435.jpg | 2018-03-06   |                                          | RAIN - SURFACE               | Purchase from local supp
 1106 | 2024-09-19 15:11:44.2162+03   |  CIFOR ICRAF                                                           |  359.000 |  12.527938 |  -8.070253 |    17.26 |             3 |                 459 |                      1365 |          6 |           709 | JPEG_63a64641-bf9a-41fb-be28-69b1cd9b05e0_3240493855555257873.jpg | 1988-09-08   | Institutions                             | UNDERGROUND                  |
 1138 | 2024-11-05 18:32:36.409797+03 |  Tegawende                                                             |  324.400 |  13.333690 |  -1.532971 |     1.90 |             2 |                 489 |                      1400 |          6 |           749 | JPEG_ee08a2a6-2813-488f-9ab5-ed47aa8412f5_8418393621962406215.jpg | 2024-11-05   |                                          | RAIN - UNDERGROUND           |
 1716 | 2025-10-06 12:21:28.57284+03  | 1                                                                      |  300.475 |  14.517415 |  -4.093880 |    15.00 |             1 |                 916 |                      2022 |          6 |           767 | JPEG_f3c0005a-ffd0-4078-93dd-4ee13efb80e3_7188026786016548051.jpg | 2025-10-02   |                                          | SURFACE - RAIN - UNDERGROUND |
   68 | 2022-06-24 11:10:31.755626+03 | 2                                                                      |    0.000 |  -1.271342 |  36.782093 |     0.00 |             2 |                   7 |                        77 |          6 |            10 | JPEG_8dc4897a-a81e-45be-bb74-79ed823468c7_3498560658289358521.jpg | 2022-06-24   |                                          |                              |
  130 | 2023-04-01 09:16:04.246055+03 | 4                                                                      |    0.000 |  -1.271342 |  36.782093 |     0.00 |         49499 |                   3 |                       164 |          6 |            42 | JPEG_e0112ac6-e404-48e2-9d27-089407891ffc_7454714828459329430.jpg | 2023-04-01   | ff                                       | SURFACE                      | 0
 2012 | 2025-10-24 12:20:33.963923+03 | alheri                                                                 |  235.500 |  14.206037 |   1.457302 |     2.70 |             2 |                1177 |                      2351 |         57 |          1089 | JPEG_b4ad0dff-c539-47c6-aea6-37bfd3fad273_8226051040177721456.jpg | 2025-10-24   |                                          | SURFACE                      |
 2014 | 2025-10-24 12:21:14.119189+03 | alheri                                                                 |  265.785 |  14.206098 |   1.457231 |     2.57 |             2 |                1182 |                      2353 |          6 |          1080 | JPEG_d5ac4bfc-7856-40c3-837b-9795d3641edd_3023064714348259063.jpg | 2013-11-14   |                                          | RAIN - SURFACE - UNDERGROUND |
 2013 | 2025-10-24 12:20:48.177119+03 | alheri                                                                 |  218.800 |  14.206044 |   1.457274 |     1.47 |             2 |                1177 |                      2352 |          6 |          1086 | JPEG_c2c74e3c-663e-4a79-ae01-a1b65f12fe50_2833818126445377594.jpg | 2013-11-14   |                                          | SURFACE - RAIN - UNDERGROUND |
 2007 | 2025-10-24 12:19:59.370414+03 | alheri                                                                 |  225.600 |  14.206013 |   1.457330 |     1.75 |             2 |                1179 |                      2346 |          6 |          1080 | JPEG_fe2399e2-2b73-4c89-8d98-a6fb123caab0_8956921412730095508.jpg | 2013-11-14   |                                          | UNDERGROUND - SURFACE - RAIN |
 2004 | 2025-10-24 12:19:46.294486+03 | alheri                                                                 |  235.500 |  14.206027 |   1.457369 |    11.44 |             2 |                1176 |                      2343 |          6 |          1085 | JPEG_c960e678-f756-4c92-ac34-06de05e6bdad_7475705634547917151.jpg | 2013-11-14   |                                          | UNDERGROUND - RAIN - SURFACE | eau de surface
 2010 | 2025-10-24 12:20:10.275437+03 | alheri                                                                 |  235.700 |  14.205987 |   1.457312 |     7.22 |             2 |                1180 |                      2349 |          6 |           710 | JPEG_89df610c-3a01-4860-ae98-22d99b4ec25b_1939590934658122188.jpg | 2013-11-14   |                                          | SURFACE - UNDERGROUND - RAIN |
 2005 | 2025-10-24 12:19:53.968782+03 | alheri                                                                 |  235.500 |  14.206038 |   1.457366 |     2.87 |             2 |                1177 |                      2344 |          6 |          1087 | JPEG_f83bdb6a-868a-48f8-b26a-ea6dda800d6d_1434690817808880140.jpg | 2013-10-10   |                                          | SURFACE                      |
 2009 | 2025-10-24 12:20:09.034698+03 | alheri                                                                 |  235.500 |  14.206169 |   1.457802 |    87.60 |             2 |                1177 |                      2348 |          6 |          1088 | JPEG_db924573-7ccf-4032-99fb-0709afe839f1_1496907422026842356.jpg | 2013-11-14   |                                          | SURFACE - UNDERGROUND - RAIN |
 2006 | 2025-10-24 12:19:55.183348+03 | alheri                                                                 |  235.500 |  14.206671 |   1.456006 |   200.00 |             2 |                1178 |                      2345 |          6 |          1085 | JPEG_2bb5d12b-9573-4ea5-b78b-5b14713f1dad_3127588209244473045.jpg | 2013-11-11   |                                          | UNDERGROUND - SURFACE - RAIN |
 2039 | 2025-10-27 20:47:20.904991+03 | alheri                                                                 |  237.537 |  14.205978 |   1.457335 |     1.03 |             2 |                1252 |                      2431 |          6 |          1084 | JPEG_5853c79f-149f-40a0-9ad1-7d5cbf4c1c9d_4172386501779079818.jpg | 2025-10-14   |                                          | SURFACE - UNDERGROUND - RAIN |
 1244 | 2024-12-08 13:21:19.623694+03 | Alheri                                                                 |  195.500 |  14.202434 |   1.454297 |     2.40 |             2 |                 575 |                      1533 |          6 |           797 | JPEG_accaf4c2-7d85-4aea-8f56-cf7ef4b0421f_7845668417481917777.jpg | 2023-04-23   |                                          | UNDERGROUND - SURFACE        |
 2008 | 2025-10-24 12:20:04.450825+03 | Alheri                                                                 |  235.500 |  14.206252 |   1.458015 |   500.00 |             2 |                1177 |                      2347 |          6 |          1083 | JPEG_a4d805a1-3bc4-40d1-ac86-e990e1d8522a_1016988131744620062.jpg | 2013-11-14   |                                          | UNDERGROUND - RAIN - SURFACE |
 2011 | 2025-10-24 12:20:11.56581+03  | Alheri                                                                 |    0.000 |  14.206671 |   1.456006 |   200.00 |             2 |                1181 |                      2350 |          6 |          1085 | JPEG_a1466775-4e4f-4931-943e-4de8f341fb5c_5650819762358522890.jpg | 2014-11-14   |                                          | SURFACE                      |
  440 | 2024-05-07 12:33:04.90528+03  | ATC kwa kathoka                                                        | 1156.500 |  -1.848360 |  37.664008 |     5.47 |             7 |                 155 |                       601 |          6 |           530 | JPEG_0262f5e4-44c4-4937-a351-912e026b683d_7665572459343594122.jpg | 2020-01-02   |                                          | RAIN - UNDERGROUND           |
  441 | 2024-05-07 12:33:05.617194+03 | ATC kwa kathoka                                                        | 1156.500 |  -1.848360 |  37.664008 |     5.47 |             7 |                 155 |                       602 |          6 |           530 | JPEG_0262f5e4-44c4-4937-a351-912e026b683d_7665572459343594122.jpg | 2020-01-02   |                                          | RAIN - UNDERGROUND           |
  439 | 2024-05-07 12:32:58.913721+03 | ATC kwa kathoka                                                        | 1156.500 |  -1.848360 |  37.664008 |     5.47 |             7 |                 155 |                       600 |          6 |           530 | JPEG_0262f5e4-44c4-4937-a351-912e026b683d_7665572459343594122.jpg | 2020-01-02   |                                          | RAIN - UNDERGROUND           |
  560 | 2024-05-08 16:13:28.225837+03 | ATC kwa kathoka                                                        | 1156.500 |  -1.848360 |  37.664008 |     5.47 |             7 |                 155 |                       736 |          6 |           530 | JPEG_0262f5e4-44c4-4937-a351-912e026b683d_7665572459343594122.jpg | 2020-01-02   |                                          | RAIN - UNDERGROUND           |
  457 | 2024-05-07 16:27:36.882239+03 | ATC kwa Kathoka                                                        | 1158.763 |  -1.848290 |  37.664025 |    74.12 |             7 |                 155 |                       618 |          6 |           530 | JPEG_b2df1a5d-5c28-4ba7-bfe8-be3570b0bc02_4575205974138918625.jpg | 2020-01-01   |                                          | RAIN - UNDERGROUND           |
  454 | 2024-05-07 16:27:23.426032+03 | ATC Kwa kathoka                                                        | 1145.325 |  -1.848366 |  37.664022 |     3.90 |             7 |                 155 |                       615 |          6 |           530 | JPEG_caf9cd63-0d1a-4a80-af44-3116e066ad09_7747155063529347598.jpg | 2020-01-01   |                                          | UNDERGROUND                  | rain
  558 | 2024-05-08 16:10:31.550856+03 | ATC Kwa kathoka                                                        | 1154.202 |  -1.848293 |  37.663980 |     8.79 |            20 |                 165 |                       734 |          6 |           530 | JPEG_36eff2ff-d5cc-4a8e-92a9-95b30403bc9b_3849696698529592882.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  455 | 2024-05-07 16:27:27.982295+03 | ATC Kwa kathoka                                                        | 1151.338 |  -1.848278 |  37.663990 |     7.00 |             5 |                 165 |                       616 |          6 |           530 | JPEG_c0d6b61f-5dd2-4bff-bec6-ec114fe5a1b2_4290384775904389638.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  576 | 2024-05-08 16:15:21.10716+03  | ATC Kwa Kathoka                                                        | 1149.000 |  -1.848340 |  37.663957 |     7.30 |             5 |                 165 |                       754 |          6 |           530 | JPEG_09e34803-f53e-4511-86a2-fdc546b372b2_3826579111346859171.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  562 | 2024-05-08 16:13:46.933601+03 | ATC Kwa Kathoka                                                        | 1149.000 |  -1.848340 |  37.663957 |     7.30 |             5 |                 165 |                       738 |          6 |           530 | JPEG_09e34803-f53e-4511-86a2-fdc546b372b2_3826579111346859171.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  580 | 2024-05-08 16:17:30.067544+03 | ATC kwa kathoka nursery                                                | 1174.600 |  -1.848309 |  37.663948 |     3.90 |             5 |                 165 |                       758 |          6 |           530 | JPEG_faf0b032-5b0a-49e2-b25d-4b41317868be_1111762218.jpg          | 2010-10-01   |                                          | UNDERGROUND                  |
  452 | 2024-05-07 16:27:11.717716+03 | ATC KWA KATHOKA NURSERY                                                | 1147.552 |  -1.848284 |  37.663955 |     5.40 |             5 |                 165 |                       613 |          6 |           530 | JPEG_1d251879-a7b8-4b88-97e2-f771b2c3ac34_5975469628562120019.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  451 | 2024-05-07 16:20:03.265986+03 | ATC Kwa Kathoka Nursery                                                | 1150.804 |  -1.848287 |  37.663942 |     3.90 |             5 |                 164 |                       612 |          6 |           530 | JPEG_1ebce9d4-f780-47e8-8368-e6f583076487_8462483117792255430.jpg | 2010-01-10   |                                          | UNDERGROUND                  |
  460 | 2024-05-08 06:37:41.038555+03 | ATC KWA KATHOKA NURSERY                                                | 1150.000 |  -1.848252 |  37.663978 |    12.62 |             5 |                 165 |                       628 |          6 |           530 | JPEG_a26b01ee-5e4a-490d-88aa-3e0b3c217911_3074324837854318603.jpg | 2010-10-01   |                                          | UNDERGROUND                  | ground water
  449 | 2024-05-07 16:19:48.201299+03 | Atc kwakathoka                                                         | 1149.300 |  -1.848314 |  37.664000 |     3.45 |             7 |                 155 |                       610 |          6 |           530 | JPEG_8da524d9-8e26-434d-9837-ed0bf97a8f23_193864653854547152.jpg  | 2020-01-02   |                                          | RAIN - UNDERGROUND           |
  565 | 2024-05-08 16:14:04.03407+03  | ATC kwakathoka                                                         | 1148.451 |  -1.848313 |  37.664057 |    10.02 |             7 |                 155 |                       741 |          6 |           530 | JPEG_d7eb8563-c78a-4fb3-b4f8-64a57ba4e1e7_8249282192208929326.jpg | 2020-01-03   |                                          | RAIN - UNDERGROUND           |
  584 | 2024-05-09 09:10:10.74129+03  | ATC KWAKATHOKA                                                         | 1144.302 |  -1.848310 |  37.663927 |     9.85 |             5 |                 240 |                       762 |          6 |           530 | JPEG_66a08178-29da-4518-8a8a-57ec4b25dde3_1220757588812761388.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  456 | 2024-05-07 16:27:28.013914+03 | ATC KwaKathoka Nursery                                                 | 1142.000 |  -1.848227 |  37.663838 |    10.75 |             5 |                 165 |                       617 |         57 |           530 | JPEG_84be5815-1840-4824-ad00-77243dfde39d_5902368413931523214.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  458 | 2024-05-07 16:27:49.432623+03 | ATC Kwakathoka Tree Nursery                                            | 1171.000 |  -1.848265 |  37.663965 |     3.00 |             5 |                 165 |                       619 |          6 |           530 | JPEG_936d70c1-58ba-4609-a6e7-b6b72487a3b5_4249723857763264401.jpg | 2010-10-01   |                                          | UNDERGROUND                  |
  569 | 2024-05-08 16:14:48.920705+03 | ATC NURSARY                                                            | 1171.700 |  -1.848324 |  37.664011 |     1.44 |             7 |                 155 |                       745 |          6 |           530 | JPEG_aee839ec-ae21-4bc4-8a53-8c37834fe084_4559155660657812507.jpg | 2020-01-01   |                                          | UNDERGROUND - RAIN           |
  563 | 2024-05-08 16:14:01.763976+03 | ATC nursery                                                            | 1152.100 |  -1.848337 |  37.663986 |     3.90 |             7 |                 155 |                       739 |          6 |           530 | JPEG_7063b3fd-a951-40d4-af62-62bf13c7e2a0_2420659367872710952.jpg | 2020-01-01   |                                          | UNDERGROUND - RAIN           |
  572 | 2024-05-08 16:14:59.245744+03 | ATC nursery                                                            | 1164.700 |  -1.848360 |  37.664031 |     3.90 |             7 |                 237 |                       749 |          6 |           530 | JPEG_3a3fb311-ed16-43c1-bd1a-8d6e9b407a81_7119401981819768599.jpg | 2020-01-01   |                                          | UNDERGROUND - RAIN           |

```

**Same lat lon nursery records**
```sql
select *
from (
    select nurs.id, nurs.nursery_name, nurs.altitude, nurs.latitude, nurs.longitude, nurs.accuracy,
        row_number() over(partition by latitude, longitude order by latitude desc, longitude desc) as location_row_no,
        op.username, nurs.nursery_ownership_type_id, prj.id as proj_id, prj.project_name, nurs.sub_county_id
    from
    respi_nurserie nurs
    left join respi_projects prj on prj.id=nurs.project_id left join respi_nursery_operator op on op.id=nurs.nursery_operator_id
)
where location_row_no > 1 and proj_id != 6;
```
### case study: Christine Tree Nursery, REGREENING AFRICA_CHILDFUND project

```sql
  id  |           nursery_name            | altitude | latitude  | longitude | accuracy | location_row_no |            username            | nursery_ownership_type_id | proj_id |        project_name         | sub_county_id
------+-----------------------------------+----------+-----------+-----------+----------+-----------------+--------------------------------+---------------------------+---------+-----------------------------+---------------
  358 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               2 | Christine Kanini               |                       498 |      44 | REGREENING AFRICA_CHILDFUND |           494
  345 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               3 | Christine Kanini               |                       484 |      44 | REGREENING AFRICA_CHILDFUND |           494
  336 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               4 | Christine Kanini               |                       474 |      44 | REGREENING AFRICA_CHILDFUND |           494
  315 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               5 | Christine Kanini               |                       451 |      44 | REGREENING AFRICA_CHILDFUND |           494
  308 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               6 | Christine Kanini               |                       443 |      44 | REGREENING AFRICA_CHILDFUND |           494
  303 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               7 | Christine Kanini               |                       437 |      44 | REGREENING AFRICA_CHILDFUND |           494
  299 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               8 | Christine Kanini               |                       432 |      44 | REGREENING AFRICA_CHILDFUND |           494
  292 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |               9 | Christine Kanini               |                       424 |      44 | REGREENING AFRICA_CHILDFUND |           494
  287 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              10 | Christine Kanini               |                       418 |      44 | REGREENING AFRICA_CHILDFUND |           494
  280 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              11 | Christine Kanini               |                       410 |      44 | REGREENING AFRICA_CHILDFUND |           494
  277 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              12 | Christine Kanini               |                       406 |      44 | REGREENING AFRICA_CHILDFUND |           494
  273 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              13 | Christine Kanini               |                       401 |      44 | REGREENING AFRICA_CHILDFUND |           494
  270 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              14 | Christine Kanini               |                       397 |      44 | REGREENING AFRICA_CHILDFUND |           494
  268 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              15 | Christine Kanini               |                       394 |      44 | REGREENING AFRICA_CHILDFUND |           494
  266 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              16 | Christine Kanini               |                       391 |      44 | REGREENING AFRICA_CHILDFUND |           494
  265 |    Christine Tree Nursery         | 1188.508 | -2.017078 | 37.462925 |     3.90 |              17 | Christine Kanini               |                       390 |      44 | REGREENING AFRICA_CHILDFUND |           494

```

- is the associated info for each nursery id the same?
    - what is the associated info?
        - respi_nursery_operator
        - respi_nursery_ownership_type
        - respi_projects
        - respi_subcounties
        - respi_nursery_entry
        - respi_nursery_specie
        - respi_scion_source
        - respi_seed_source
        - respi_seedling_propagation_method
        - respi_seedling_production_method 

```sql
select
    nent.*, nurs.nursery_name, nspc.local_name, nspc.scientific_name, nspc.date_sown, nspc.price_per_seedling, nspc.purchase_unit,
    nspc.seeds_germinated, nspc.seeds_purchased, nspc.seeds_sown, nspc.seeds_survived, nspc.sow_unit
from
    respi_nursery_entry nent
left join respi_nursery_specie nspc on nspc.nursery_entry_id=nent.id
left join respi_nurserie nurs on nurs.id=nent.nursery_id
where 
    nent.nursery_id in (358, 345,336,315,308,303, 299, 292, 287, 280, 277, 273, 270, 268, 266, 265);
 id  |         recorded_dte          | date_collected | collector_id | nursery_id |        nursery_name        | local_name | scientific_name | date_sown  | price_per_seedling | purchase_unit | seeds_germinated | seeds_purchased | seeds_sown | seeds_survived | sow_unit
-----+-------------------------------+----------------+--------------+------------+----------------------------+------------+-----------------+------------+--------------------+---------------+------------------+-----------------+------------+----------------+----------
 265 | 2024-02-28 15:30:42.18155+03  | 2024-02-28     |          464 |        265 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 266 | 2024-02-28 15:35:42.165665+03 | 2024-02-28     |          464 |        266 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 268 | 2024-02-28 15:35:48.540736+03 | 2024-02-28     |          464 |        268 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 270 | 2024-02-28 16:39:54.209673+03 | 2024-02-28     |          464 |        270 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 273 | 2024-02-28 17:53:05.72987+03  | 2024-02-28     |          464 |        273 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 277 | 2024-02-29 09:43:04.578596+03 | 2024-02-28     |          464 |        277 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 280 | 2024-02-29 15:27:43.832456+03 | 2024-02-28     |          464 |        280 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 287 | 2024-02-29 15:27:53.872927+03 | 2024-02-28     |          464 |        287 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 292 | 2024-02-29 16:33:48.939272+03 | 2024-02-28     |          464 |        292 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 299 | 2024-02-29 16:42:06.983216+03 | 2024-02-28     |          464 |        299 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 303 | 2024-03-04 10:31:02.13238+03  | 2024-02-28     |          464 |        303 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 308 | 2024-03-04 11:57:22.335374+03 | 2024-02-28     |          464 |        308 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 315 | 2024-03-04 15:10:42.101654+03 | 2024-02-28     |          464 |        315 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 336 | 2024-03-12 12:41:26.401614+03 | 2024-02-28     |          464 |        336 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 345 | 2024-03-26 10:20:23.177621+03 | 2024-02-28     |          464 |        345 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
 358 | 2024-03-26 10:21:38.598629+03 | 2024-02-28     |          464 |        358 |    Christine Tree Nursery  | Maembe     |                 | 2024-02-05 |              50.00 | KG            |              350 |               4 |          4 |            350 | KG
(16 rows)

```