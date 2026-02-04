# views

### 1. all duplicates view
- all duplicates in `duplicates` view are based on exactly same lat, lon, from `respi_tree_measurement`.
    - cohort_id >> `tp module`
    - fmnr-species_id >> `fmnr module`

visualise the view like
```sql
select * from duplicates;
```

#### view definition `\d+ duplicates`
```sql
CREATE OR REPLACE VIEW duplicates AS
SELECT trm.id,
    trm.latitude,
    trm.longitude,
    trm.accuracy,
    trm.rcc_cbh,
    trm.comment,
    trm.cohort_id,
    trm.fmnr_species_id
   FROM respi_tree_measurement trm
    JOIN ( SELECT trm.latitude,
                trm.longitude
            FROM respi_tree_measurement trm
            GROUP BY trm.latitude, trm.longitude
            HAVING count(*) > 1
        ) dpls 
    ON trm.latitude = dpls.latitude AND trm.longitude = dpls.longitude
ORDER BY trm.latitude;

```



### 2. fmnr_dpls view `\d+ fmnr_duplicates`
- `fmnr_duplicates` shows only dpls found in fmnr module.
- gives us the plot id column to delete from

```sql
CREATE OR REPLACE VIEW fmnr_duplicates AS
SELECT 
    ent.plot_id as fmnr_plot_id,
	ent.project_id as project_id,
    dpls.latitude,
    dpls.longitude,
    dpls.comment,
    dpls.accuracy,
    dpls.rcc_cbh,
    dpls.cohort_id,
    dpls.fmnr_species_id,
    spcs.local_name,
    spcs.scientific_name,
    spcs.fmnr_entry_id,
    ent.collector_id,
    plt.name AS plot_name
   FROM duplicates dpls
     JOIN respi_fmnr_species spcs ON spcs.id = dpls.fmnr_species_id
     JOIN respi_fmnr_entry ent ON ent.id = spcs.fmnr_entry_id
     JOIN respi_plots plt ON plt.id = ent.plot_id
  WHERE ent.project_id <> 6
  ORDER BY dpls.latitude;

```
### 3. tp_dpls view `\d+ tp_duplicates`

- `tp_duplicates` shows only dpls dound in tp module
- gives the plot id to delete from


```sql
CREATE OR REPLACE VIEW tp_duplicates AS
SELECT 
    tpe.plot_id as tp_entry_plot_id,
	tpe.project_id as project_id,
    dpls.latitude,
    dpls.longitude,
    dpls.comment,
    dpls.accuracy,
    dpls.rcc_cbh,
    dpls.cohort_id,
	dpls.id as dpls_id,
    dpls.fmnr_species_id,
    tp_ch.local_name,
    tp_ch.scientific_name

    
FROM duplicates dpls
    JOIN respi_cohort tp_ch on tp_ch.id = dpls.cohort_id
    JOIN respi_tree_planting_entry tpe on tpe.id = tp_ch.tp_entry_id
    JOIN respi_plots plt2 on plt2.id = tpe.plot_id
WHERE tpe.project_id <> 6
ORDER BY dpls.latitude;
```


## functions

### delete_fmnr_dpls `\sf delete_fmnr_dpls` 
- `delete_fmnr_dpls` -  deletes based on plot id, the ids of
    - respi_fmnr_management_practices     
    - respi_fmnr_tree_usage 
    - respi_tree_measurement
    - respi_fmnr_species    
    - respi_fmnr_entry     
    - respi_plot_points    
    - respi_plot_polygon   
    - respi_plots 

### delete_tp_dpls `\sf delete_tp_dpls` 
- `delete_tp_dpls` - deletes based on plot id, the ids of
    - respi_tp_management_practices - `cohort_id`
    - respi_tree_measurement - `cohort_id`
    - respi_cohort - `cohort_id`
    - respi_tree_planting_entry - `plot_id`
    - respi_plot_points  - `plot_id`
    - respi_plot_polygon  - `plot_id`
    - respi_plots - `plot_id`

## Duplicates - FMNR & TP

- `Plots have dupicates(name based) but unique ids.` e.g. '02993a44-12b0-48d2-8cbc-51d3792eb65e'
```sql
regreen_local_jan2026=# select dpls.plot_id, dpls.name, dpls.crops,dpls.plot_row_no, ent.recorded_dte, ent.project_id, ent.id as tp_entry_id from (select id as plot_id,  name, crops, row_number() over (partition by name) as plot_row_no from respi_plots) dpls left join respi_tree_planting_entry ent on ent.plot_id=dpls.plot_id where plot_row_no > 1 and ent.project_id != 6  limit 300;
 plot_id |                 name                 |                                 crops                                 | plot_row_no |         recorded_dte          | project_id | tp_entry_id
---------+--------------------------------------+-----------------------------------------------------------------------+-------------+-------------------------------+------------+-------------
   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           2 | 2025-02-14 20:24:04.14025+03  |         49 |        4638
   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           3 | 2025-02-14 20:21:54.228783+03 |         49 |        4637
   10432 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           4 | 2025-02-14 20:11:33.438573+03 |         49 |        4636
   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           5 | 2025-02-14 20:10:50.854039+03 |         49 |        4635
    6036 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           2 | 2024-05-24 14:40:08.601475+03 |         57 |        2810
    6031 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           3 | 2024-05-24 14:37:15.411662+03 |         57 |        2805
```
- `These duplicated plots have duplicated trees(based on measurement)`

```sql
regreen_local_jan2026=# SELECT *
FROM (
    SELECT trm.id, trm.latitude, trm.longitude, trm.accuracy, trm.rcc_cbh,
        ROW_NUMBER() OVER (
            PARTITION BY trm.latitude, trm.longitude
            ORDER BY trm.latitude
        ) AS dup_count,
        ent.plot_id, plt.name, trm.cohort_id, trm.fmnr_species_id, trm.comment
    FROM respi_tree_measurement trm
    LEFT JOIN respi_cohort ch ON ch.id = trm.cohort_id
    LEFT JOIN respi_tree_planting_entry ent ON ent.id=ch.tp_entry_id 
    left join respi_plots plt on plt.id = ent.plot_id
) t
WHERE dup_count > 1 and name = '02993a44-12b0-48d2-8cbc-51d3792eb65e'
ORDER BY latitude desc, longitude desc;
  id   | latitude  | longitude | accuracy | rcc_cbh | dup_count | plot_id |                 name                 | cohort_id | fmnr_species_id | comment
-------+-----------+-----------+----------+---------+-----------+---------+--------------------------------------+-----------+-----------------+---------
 16708 | -1.880789 | 30.645290 |     1.30 |    0.50 |         5 |   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10788 |                 |
 16706 | -1.880789 | 30.645290 |     1.30 |    0.50 |         2 |   10432 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10786 |                 |
 16704 | -1.880789 | 30.645290 |     1.30 |    0.50 |         3 |   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10784 |                 |
 16710 | -1.880789 | 30.645290 |     1.30 |    0.50 |         4 |   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10790 |                 |
 16707 | -1.880849 | 30.645463 |     1.30 |    0.50 |         2 |   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10787 |                 |
 16709 | -1.880849 | 30.645463 |     1.30 |    0.50 |         3 |   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10789 |                 |
 16703 | -1.880849 | 30.645463 |     1.30 |    0.50 |         4 |   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10783 |                 |
 16705 | -1.880849 | 30.645463 |     1.30 |    0.50 |         5 |   10432 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |     10785 |                 |
(8 rows)

```

**Proposed solution**

- get all duplicates for one plot
- based on id, check if all duplicated plots have same number of duplicates
- choose one plot to retain
- the rest, delete tree and plot info(including plot ownership, planting area, crops...)

**Philosophy**
- Assign a row number to every duplicate(partition) tree measurement(exact lat, lon)
    - requires a window function - `ROW_NUMBER()`
- delete only row_number > 1 (skip first record)
- we will not consider `TEST` project

**Why `PARTITION BY`?** 
- defines the `window` of rows for the function to work on(The function being `ROW_NUMBER()`)
- it returns every individual record in the query.
- 

```sql
SELECT *
FROM (
    SELECT
        trm.id,
        trm.latitude,
        trm.longitude,
        trm.accuracy,
        trm.rcc_cbh,
        ROW_NUMBER() OVER (
            PARTITION BY trm.latitude, trm.longitude
            ORDER BY trm.latitude
        ) AS dup_count,
        ent.plot_id,
        trm.cohort_id,
        trm.fmnr_species_id,        
        trm.comment
    FROM respi_tree_measurement trm
    LEFT JOIN respi_cohort ch
        ON ch.id = trm.cohort_id
    LEFT JOIN respi_tree_planting_entry ent
        ON ent.id=ch.tp_entry_id
) t
WHERE dup_count > 1
ORDER BY latitude desc
LIMIT 30;

  id   | latitude  |  longitude  | accuracy | rcc_cbh | dup_count | plot_id | cohort_id | fmnr_species_id |     comment
-------+-----------+-------------+----------+---------+-----------+---------+-----------+-----------------+-----------------
   128 | 37.422114 | -122.082661 |     5.00 |   12.00 |         2 |     183 |       110 |                 | Good stuff
   133 | 37.422114 | -122.082661 |     5.00 |   12.00 |         3 |     188 |       115 |                 | Good stuff
 42327 | 15.014057 |   -2.949828 |     3.90 |    1.00 |         2 |         |           |            9456 | kadidia cisse
 42329 | 15.014057 |   -2.949828 |     3.90 |    1.00 |         3 |         |           |            9458 | kadidia cisse
 42330 | 15.014057 |   -2.949828 |     3.90 |    1.00 |         4 |         |           |            9459 | kadidia cisse
 42199 | 15.006174 |   -2.954281 |   300.00 |    2.00 |         3 |         |           |            9392 |
 42228 | 15.006174 |   -2.954281 |   300.00 |    1.00 |         2 |   18679 |     32684 |                 |
 42138 | 15.006174 |   -2.954281 |   300.00 |   15.00 |         4 |         |           |            9351 | kowi bocoum
 42302 | 15.005745 |   -2.954758 |     2.20 |    1.50 |         2 |         |           |            9447 | fatoumata kone
 42303 | 15.005745 |   -2.954758 |     2.20 |    1.50 |         3 |         |           |            9448 | fatoumata kone
 42301 | 15.005745 |   -2.954758 |     2.20 |    1.50 |         5 |         |           |            9446 | fatoumata kone
 42299 | 15.005745 |   -2.954758 |     2.20 |    1.50 |         4 |         |           |            9444 | fatoumata kone
 41724 | 15.005743 |   -2.954840 |     4.30 |  133.00 |         2 |         |           |            9092 | arbre de repos
 42152 | 15.003851 |   -2.954519 |     1.93 |    1.50 |         2 |         |           |            9365 | Fatoumata kone
 42151 | 15.003851 |   -2.954519 |     1.93 |    1.50 |         3 |         |           |            9364 | Fatoumata kone
 42516 | 15.003396 |   -2.949675 |     8.95 |    1.00 |         2 |   19014 |     32855 |                 | kadidia cisse
 42149 | 15.003216 |   -2.949761 |     2.04 |   10.00 |         2 |         |           |            9363 | Fatoumata Maiga
 42217 | 15.003148 |   -2.949652 |    95.18 |   20.00 |         2 |   18665 |     32680 |                 | fatoumata maiga
 42500 | 15.002492 |   -2.964665 |     3.90 |   10.00 |         4 |   18999 |     32844 |                 | kadidia cisse
 42493 | 15.002492 |   -2.964665 |     3.90 |   10.00 |         2 |   18995 |     32837 |                 | kadidia cisse
 42498 | 15.002492 |   -2.964665 |     3.90 |   10.00 |         3 |   18998 |     32842 |                 | kadidia cisse
 42502 | 15.002492 |   -2.964665 |     3.90 |   10.00 |         5 |   19000 |     32846 |                 | kadidia cisse
 42503 | 15.002479 |   -2.964505 |    12.10 |    1.00 |         2 |   19000 |     32847 |                 | kadidia cisse
 42496 | 15.002479 |   -2.964505 |    12.10 |    1.00 |         3 |   18996 |     32840 |                 | kadidia cisse
 42501 | 15.002479 |   -2.964505 |    12.10 |    1.00 |         5 |   18999 |     32845 |                 | kadidia cisse
 42499 | 15.002479 |   -2.964505 |    12.10 |    1.00 |         4 |   18998 |     32843 |                 | kadidia cisse
 42009 | 15.001054 |   -2.954688 |     2.10 |   15.00 |         2 |   18306 |     32589 |                 | Fatoumata kone
 42008 | 15.001054 |   -2.954688 |     2.10 |   15.00 |         3 |   18305 |     32588 |                 | Fatoumata kone
 42007 | 15.001054 |   -2.954688 |     2.10 |   15.00 |         4 |   18304 |     32587 |                 | Fatoumata kone
 42006 | 15.001054 |   -2.954688 |     2.10 |   15.00 |         5 |   18303 |     32586 |                 | Fatoumata kone
(30 rows)


```


## Deletion logic

## get duplicate plot ids based on name
```sql
regreen_local_jan2026=# select dpls.plot_id, dpls.name, dpls.crops,dpls.plot_row_no, ent.recorded_dte, ent.project_id, ent.id as tp_entry_id from (select id as plot_id,  name, crops, row_number() over (partition by name) as plot_row_no from respi_plots) dpls left join respi_tree_planting_entry ent on ent.plot_id=dpls.plot_id where plot_row_no > 1 and ent.project_id != 6  limit 300;
 plot_id |                 name                 |                                 crops                                 | plot_row_no |         recorded_dte          | project_id | tp_entry_id
---------+--------------------------------------+-----------------------------------------------------------------------+-------------+-------------------------------+------------+-------------
   11855 | 0024392a-9368-4683-8735-c57018665317 | Banana  - Cassava                                                     |           2 | 2025-05-01 18:34:17.531992+03 |         50 |        5679
   12938 | 005b6fd3-814f-44e7-a43e-c14c39f83823 | Plantain  - Yam - Cocoyam - Cassava                                   |           2 | 2025-05-09 20:24:09.872214+03 |        115 |        6727
   15981 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |           2 | 2025-06-16 20:59:15.769396+03 |        122 |        8896
   15979 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |           3 | 2025-06-16 19:35:08.808854+03 |        122 |        8894
   15980 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |           4 | 2025-06-16 19:41:17.710342+03 |        122 |        8895
   15847 | 009ecdbe-2f27-4a4f-bf19-827f22497228 | Banane                                                                |           5 | 2025-06-11 10:53:46.766512+03 |        122 |        8848
   10998 | 00f8a17f-4377-4079-98ca-e6ea9a109033 |                                                                       |           2 | 2025-03-17 14:58:32.053109+03 |        115 |        5095
   12866 | 01351558-a399-4017-b8c0-c349574d598c | Irish Potato  - Banana - Maize - Cassava Leaves  - Beans              |           2 | 2025-05-09 06:39:28.062971+03 |         50 |        6655
   17086 | 0152ef8f-8cea-4837-affb-1e1af6081e93 | Ibishyimbo - Ibigori - Amasaka - Soya                                 |           2 | 2025-08-11 13:42:12.717741+03 |         41 |        9845
   12612 | 01596ed1-85ca-4839-8efa-031c621bd214 | Banana tree - Beans  - Maize - yams                                   |           2 | 2025-05-08 18:47:39.204047+03 |         50 |        6421
   10434 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           2 | 2025-02-14 20:24:04.14025+03  |         49 |        4638
   10433 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           3 | 2025-02-14 20:21:54.228783+03 |         49 |        4637
   10432 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           4 | 2025-02-14 20:11:33.438573+03 |         49 |        4636
   10431 | 02993a44-12b0-48d2-8cbc-51d3792eb65e |                                                                       |           5 | 2025-02-14 20:10:50.854039+03 |         49 |        4635
    6036 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           2 | 2024-05-24 14:40:08.601475+03 |         57 |        2810
    6031 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           3 | 2024-05-24 14:37:15.411662+03 |         57 |        2805
    6015 | 0373b36f-fdcb-4b1f-9596-23cefc8c06ac | Wheat                                                                 |           4 | 2024-05-24 14:13:07.93081+03  |         57 |        2789
   10914 | 04688ac6-bc92-47bf-93a4-c7d8e4cd788e | Potatoes  - Cassava                                                   |           2 | 2025-03-07 17:29:10.499291+03 |        117 |        5013
   10970 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |           2 | 2025-03-12 16:51:22.276537+03 |         49 |        5067
   10971 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |           3 | 2025-03-12 16:53:32.133242+03 |         49 |        5068
   10969 | 04c674ef-bf60-45ce-8146-5bdb589fa00e | maize - millet - beans - cassava                                      |           4 | 2025-03-12 16:47:01.670742+03 |         49 |        5066
   13812 | 04e12ae8-b5bf-49e2-9fe7-2ef82c6324a6 | Plantain                                                              |           2 | 2025-05-17 12:24:54.652487+03 |        115 |        7467
   12782 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |           2 | 2025-05-08 21:47:37.837653+03 |         50 |        6580
   13070 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |           3 | 2025-05-11 00:26:24.364694+03 |         50 |        6842
   12791 | 054e2dd5-93e7-4662-97b7-b3ac9d4d6a8b | Green Bananas - Irish Potato                                          |           4 | 2025-05-08 21:50:51.026826+03 |         50 |        6584
   12440 | 058d9904-7451-452a-8d75-9d82f2d06767 |                                                                       |           2 | 2025-05-07 21:06:46.780892+03 |         50 |        6253
   12405 | 05a912bd-715f-473e-b06b-13114f1effed | Tomato                                                                |           2 | 2025-05-07 20:23:31.268603+03 |         50 |        6218
   15639 | 05d8f7ae-1ee4-46e1-9ec2-b6ab1c48db0d | Plantain                                                              |           2 | 2025-06-04 01:03:12.538275+03 |        115 |        8671
   12150 | 0604de5f-3966-4b6c-8fcb-94e96483a54a | beans                                                                 |           2 | 2025-05-06 19:28:13.012206+03 |         50 |        5966
    6107 | 06629fb5-9f44-400e-995c-307fb963fd4c | Irish Potatoes                                                        |           2 | 2024-05-25 12:27:32.760938+03 |         58 |        2877
    6108 | 06629fb5-9f44-400e-995c-307fb963fd4c | Irish Potatoes                                                        |           3 | 2024-05-25 12:28:56.876787+03 |         58 |        2878
```


### delete tp dpls logic

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
                trm.id AS trm_id,
                trm.latitude,
                trm.longitude,
                trm.accuracy,
                trm.rcc_cbh,
                ROW_NUMBER() OVER (
                    PARTITION BY trm.latitude, trm.longitude
                    ORDER BY trm.latitude
                ) AS row_num,
                ent.plot_id,
                trm.cohort_id,
                trm.fmnr_species_id,        
                trm.comment
            FROM respi_tree_measurement trm
            LEFT JOIN respi_cohort ch
                ON ch.id = trm.cohort_id
            LEFT JOIN respi_tree_planting_entry ent
                ON ent.id=ch.tp_entry_id
        ) dpls
        WHERE row_num > 1 AND plot_id=plot_ide
        ORDER BY latitude desc, longitude desc
    LOOP
        --delete tp_management_practices
        DELETE FROM respi_tp_management_practices WHERE cohort_id = r.cohort_id;

        --delete tp_measurement
        DELETE FROM respi_tree_measurement WHERE cohort_id = r.cohort_id;

        --delete tp_tree_usage
        DELETE FROM respi_tp_tree_usage WHERE cohort_id = r.cohort_id;        

        --delete tp_planting area type
        DELETE FROM respi_tp_plantingarea_type WHERE cohort_id = r.cohort_id;

        --delete tp_species
        DELETE FROM respi_cohort WHERE id = r.cohort_id;

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
    END LOOP;
END $$;    
```