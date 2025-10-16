- [get the duplicate plots based on name](#get-the-duplicate-plots-based-on-name)
    - [create the view for duplicate plots](#create-the-view-for-duplicate-plots)
    - [query the view](#query-the-view)
- [check if the duplicate plots `16019, 16020, 16021, 16022, 16023, 16024, 16025` are complete by:]
# get the duplicate plots based on name

## create the view for duplicate plots
```sql
regreen=>  create view duplicate_plots as 
  SELECT pl.id AS plot_id,
    pl.recorded_dte,
    pl.name,
    en.project_id,
    en.id AS fmnr_entry_id
   FROM respi_plots pl
     JOIN ( SELECT plt.name,
            count(*) AS count
           FROM respi_plots plt
          GROUP BY plt.name
         HAVING count(*) > 1) dpls ON dpls.name::text = pl.name::text
     JOIN respi_fmnr_entry en ON en.plot_id = pl.id
  ORDER BY pl.name;

```

## query the view for duplicates: identify plot ids xyz
```sql
regreen=> select * from duplicate_plots limit 33;

 plot_id |         recorded_dte          |                 name                 | project_id | fmnr_entry_id 
---------+-------------------------------+--------------------------------------+------------+---------------
    5566 | 2024-05-22 12:03:23.92071+03  | 00ce2b5b-2d29-45b2-9a06-23f9a48c8698 |         41 |           672
    5563 | 2024-05-22 12:03:15.840254+03 | 00ce2b5b-2d29-45b2-9a06-23f9a48c8698 |         41 |           670
    5423 | 2024-05-21 16:43:00.670744+03 | 05c072ae-3a44-44ce-bd34-ab6f051771fa |         41 |           656
    5425 | 2024-05-21 16:45:14.652153+03 | 05c072ae-3a44-44ce-bd34-ab6f051771fa |         41 |           658
    5406 | 2024-05-21 16:30:27.976304+03 | 080639eb-4f5b-4d9b-8da9-9e23bbb373ed |         41 |           642
    5407 | 2024-05-21 16:31:31.367448+03 | 080639eb-4f5b-4d9b-8da9-9e23bbb373ed |         41 |           643
    5791 | 2024-05-22 13:37:58.542645+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           747
    5789 | 2024-05-22 13:37:39.349655+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           745
    5784 | 2024-05-22 13:37:08.410414+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           740
    5787 | 2024-05-22 13:37:23.201496+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           743
     353 | 2023-04-01 08:45:32.010726+03 | 0XTM                                 |          6 |           126
     356 | 2023-04-01 08:54:18.325986+03 | 0XTM                                 |          6 |           129
    8111 | 2024-11-02 13:54:18.896568+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2269
    8094 | 2024-11-02 13:12:52.191322+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2252
    8098 | 2024-11-02 13:19:13.721988+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2256
    8096 | 2024-11-02 13:17:14.376749+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2254
    8112 | 2024-11-02 13:54:35.58189+03  | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2270
    8119 | 2024-11-02 13:57:54.33334+03  | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2273
    8881 | 2024-12-18 11:40:45.378657+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2578
    8883 | 2024-12-18 12:11:01.378154+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2580
    8882 | 2024-12-18 11:45:33.416685+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2579
    8876 | 2024-12-18 11:21:34.322642+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2573
    8877 | 2024-12-18 11:25:20.266396+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2574
     351 | 2023-03-30 15:25:46.463704+03 | 14ZY                                 |          6 |           125
     346 | 2023-03-30 14:03:50.837844+03 | 14ZY                                 |          6 |           123
    6838 | 2024-10-04 14:47:22.995914+03 | 1b037949-9ea6-4a49-89e9-86a595a1c7d0 |          6 |          1196
    6821 | 2024-10-04 00:03:37.647527+03 | 1b037949-9ea6-4a49-89e9-86a595a1c7d0 |          6 |          1187
    8234 | 2024-11-14 18:34:26.338303+03 | 1b6b0c02-0534-4a0c-b5e9-91a36ba38d8d |          6 |          2340
    8233 | 2024-11-14 18:34:16.070468+03 | 1b6b0c02-0534-4a0c-b5e9-91a36ba38d8d |          6 |          2339
    6952 | 2024-10-10 14:31:13.741183+03 | 1cf4ddf3-611b-40b2-a6a4-3a561c79132d |         93 |          1305
    6954 | 2024-10-10 18:58:33.377495+03 | 1cf4ddf3-611b-40b2-a6a4-3a561c79132d |         93 |          1307
    4577 | 2024-05-08 12:43:49.740445+03 | 1d1e4216-9b2a-4b82-8abe-20c5d568a6b7 |         41 |           367
    4507 | 2024-05-08 10:54:33.894303+03 | 1d1e4216-9b2a-4b82-8abe-20c5d568a6b7 |         41 |           361
(33 rows)


```

## get the dpls for plot ids xyz...
```sql
regreen=> select en.recorded_dte, en.plot_id, en.project_id, sp.local_name, trm.latitude, trm.longitude, trm.altitude, trm.rcc_cbh, us.tree_usage, mn.management_practies from respi_fmnr_entry en join respi_fmnr_species sp on sp.fmnr_entry_id=en.id join respi_tree_measurement trm on trm.fmnr_species_id=sp.id join respi_fmnr_tree_usage us on us.fmnr_species_id=sp.id join respi_fmnr_management_practices mn on mn.fmnr_species_id=sp.id where plot_id in (8881,8882,8883,8876,8877) order by trm.latitude;

 plot_id |         recorded_dte          |                 name                 | project_id | fmnr_entry_id 
---------+-------------------------------+--------------------------------------+------------+---------------
    5566 | 2024-05-22 12:03:23.92071+03  | 00ce2b5b-2d29-45b2-9a06-23f9a48c8698 |         41 |           672
    5563 | 2024-05-22 12:03:15.840254+03 | 00ce2b5b-2d29-45b2-9a06-23f9a48c8698 |         41 |           670
    5425 | 2024-05-21 16:45:14.652153+03 | 05c072ae-3a44-44ce-bd34-ab6f051771fa |         41 |           658
    5423 | 2024-05-21 16:43:00.670744+03 | 05c072ae-3a44-44ce-bd34-ab6f051771fa |         41 |           656
    5406 | 2024-05-21 16:30:27.976304+03 | 080639eb-4f5b-4d9b-8da9-9e23bbb373ed |         41 |           642
    5407 | 2024-05-21 16:31:31.367448+03 | 080639eb-4f5b-4d9b-8da9-9e23bbb373ed |         41 |           643
    5784 | 2024-05-22 13:37:08.410414+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           740
    5791 | 2024-05-22 13:37:58.542645+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           747
    5789 | 2024-05-22 13:37:39.349655+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           745
    5787 | 2024-05-22 13:37:23.201496+03 | 0f097aa0-c9b4-4e2c-b20a-333da0584826 |         41 |           743
     356 | 2023-04-01 08:54:18.325986+03 | 0XTM                                 |          6 |           129
     353 | 2023-04-01 08:45:32.010726+03 | 0XTM                                 |          6 |           126
    8096 | 2024-11-02 13:17:14.376749+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2254
    8112 | 2024-11-02 13:54:35.58189+03  | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2270
    8094 | 2024-11-02 13:12:52.191322+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2252
    8119 | 2024-11-02 13:57:54.33334+03  | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2273
    8098 | 2024-11-02 13:19:13.721988+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2256
    8111 | 2024-11-02 13:54:18.896568+03 | 10536cfb-ca19-4a93-a061-a1c759bf7ab3 |         46 |          2269
    8876 | 2024-12-18 11:21:34.322642+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2573
    8883 | 2024-12-18 12:11:01.378154+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2580
    8882 | 2024-12-18 11:45:33.416685+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2579
    8877 | 2024-12-18 11:25:20.266396+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2574
    8881 | 2024-12-18 11:40:45.378657+03 | 135619c7-d5ea-4859-ab48-084be591bfb5 |         46 |          2578
     351 | 2023-03-30 15:25:46.463704+03 | 14ZY                                 |          6 |           125
     346 | 2023-03-30 14:03:50.837844+03 | 14ZY                                 |          6 |           123
    6821 | 2024-10-04 00:03:37.647527+03 | 1b037949-9ea6-4a49-89e9-86a595a1c7d0 |          6 |          1187
    6838 | 2024-10-04 14:47:22.995914+03 | 1b037949-9ea6-4a49-89e9-86a595a1c7d0 |          6 |          1196
    8233 | 2024-11-14 18:34:16.070468+03 | 1b6b0c02-0534-4a0c-b5e9-91a36ba38d8d |          6 |          2339
    8234 | 2024-11-14 18:34:26.338303+03 | 1b6b0c02-0534-4a0c-b5e9-91a36ba38d8d |          6 |          2340
    6954 | 2024-10-10 18:58:33.377495+03 | 1cf4ddf3-611b-40b2-a6a4-3a561c79132d |         93 |          1307
    6952 | 2024-10-10 14:31:13.741183+03 | 1cf4ddf3-611b-40b2-a6a4-3a561c79132d |         93 |          1305
    4577 | 2024-05-08 12:43:49.740445+03 | 1d1e4216-9b2a-4b82-8abe-20c5d568a6b7 |         41 |           367
    4507 | 2024-05-08 10:54:33.894303+03 | 1d1e4216-9b2a-4b82-8abe-20c5d568a6b7 |         41 |           361
    7716 | 2024-10-30 08:31:13.792535+03 | 2295b9d7-a8fd-4359-adef-fc38dc68930b |         46 |          2041
:

```

## the function

```sql
select en.plot_id as plot_id,
  en.recorded_dte,
  sp.local_name,
  trm.latitude,
  trm.longitude,
  trm.accuracy,
  trm.rcc_cbh,
  us.tree_usage,
  mn.management_pracices
  --plp.id as plot_point_id, 
  --plpl.id as plot_polygon_id 
from respi_fmnr_entry en 
  join respi_fmnr_species sp on sp.fmnr_entry_id=en.id 
  join respi_tree_measurement trm on trm.fmnr_species_id=sp.id 
  join respi_fmnr_tree_usage us on us.fmnr_species_id=sp.id 
  join respi_fmnr_management_practices mn on mn.fmnr_species_id=sp.id 
  join respi_plot_points plp on plp.plot_id=en.plot_id 
  join respi_plot_polygon plpl on plpl.plot_id=en.plot_id 
where en.plot_id in (5197, 5243, 5199, 5249, 5207) 
order by trm.latitude limit 33;
```



```sql
select en.plot_id as plot_id,
  en.id as entry_id, 
  sp.id as species_id, 
  us.id as usage_id, 
  mn.id as management_id, 
  trm.id as tree_meaurement_id, 
  plp.id as plot_point_id, 
  plpl.id as plot_polygon_id 
from respi_fmnr_entry en 
  join respi_fmnr_species sp on sp.fmnr_entry_id=en.id 
  join respi_tree_measurement trm on trm.fmnr_species_id=sp.id 
  join respi_fmnr_tree_usage us on us.fmnr_species_id=sp.id 
  join respi_fmnr_management_practices mn on mn.fmnr_species_id=sp.id 
  join respi_plot_points plp on plp.plot_id=en.plot_id 
  join respi_plot_polygon plpl on plpl.plot_id=en.plot_id 
where en.plot_id in (8881,8882,8883,8876,8877) 
order by trm.latitude limit 33;


 entry_id | species_id | usage_id | management_id | tree_meaurement_id | plot_point_id | plot_polygon_id 
----------+------------+----------+---------------+--------------------+---------------+-----------------
     2574 |       6021 |     6021 |          6021 |              14068 |         83338 |            8227
     2578 |       6032 |     6032 |          6032 |              14079 |         83361 |            8231
     2574 |       6021 |     6021 |          6021 |              14068 |         83334 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83337 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83341 |            8227
     2578 |       6032 |     6032 |          6032 |              14079 |         83360 |            8231
     2574 |       6021 |     6021 |          6021 |              14068 |         83332 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83333 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83335 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83336 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83339 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83340 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83342 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83344 |            8227
     2574 |       6021 |     6021 |          6021 |              14068 |         83331 |            8227
     2573 |       6016 |     6016 |          6016 |              14063 |         83316 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83317 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83318 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83319 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83320 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83321 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83322 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83323 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83324 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83325 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83326 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83327 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83328 |            8226
     2573 |       6016 |     6016 |          6016 |              14063 |         83329 |            8226
     2574 |       6021 |     6021 |          6021 |              14068 |         83343 |            8227
     2573 |       6016 |     6016 |          6016 |              14063 |         83315 |            8226
     2574 |       6021 |     6021 |          6021 |              14068 |         83330 |            8227
     2578 |       6032 |     6032 |          6032 |              14079 |         83362 |            8231
(33 rows)

```