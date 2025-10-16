# Find Duplicates in Tree measurement

```sql
create view duplicates as 
SELECT trm.id,                                       
    trm.latitude,                                    
    trm.longitude,
    trm.comment,
    trm.accuracy,
    trm.rcc_cbh,
    trm.cohort_id,
    trm.fmnr_species_id
   FROM respi_tree_measurement trm
     JOIN ( SELECT respi_tree_measurement.latitude,
            respi_tree_measurement.longitude,
            count(*) AS count
           FROM respi_tree_measurement
          GROUP BY respi_tree_measurement.latitude, respi_tree_measurement.longitude
         HAVING count(*) > 1) dpls ON dpls.latitude = trm.latitude
  ORDER BY trm.latitude;

```

  id   | latitude  |  longitude  |                     comment                                     | accuracy | rcc_cbh | cohort_id | fmnr_species_id 
-------|-----------|-------------|-----------------------------------------------------------------|----------|---------|-----------|-----------------
  5153 | -3.495613 |   38.306280 | well managed                                                    |     4.08 |   52.00 |      4936 |                
  5104 | -3.495613 |   38.306280 | well managed                                                    |     4.08 |   52.00 |      4899 |                
  4852 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             287
  5240 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             344
  4892 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             304
  4857 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             291
  4878 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             297
  4882 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             299
  4863 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             293
  4870 | -3.495394 |   38.306062 | free has three branches multipuple stems                        |     5.10 |   25.00 |           |             295
  4827 | -3.495348 |   38.306071 | multiple trees steaming from one stump                          |     5.86 |   25.00 |           |             279
  4695 | -3.495348 |   38.306071 | multiple trees steaming from one stump                          |     5.86 |   25.00 |           |             236
  5163 | -3.495342 |   38.306054 | well managed                                                    |     3.90 |    8.00 |      4946 |                
  5186 | -3.495342 |   38.306054 | well managed                                                    |     3.90 |    8.00 |      4963 |                
  5200 | -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised      |     3.84 |    8.00 |      4977 |                
  5118 | -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised      |     3.84 |    8.00 |      4907 |                
  5208 | -3.495273 |   38.306058 | very straight poles                                             |     8.48 |   17.00 |           |             343
  5206 | -3.495273 |   38.306058 | very straight poles                                             |     8.48 |   17.00 |           |             341
  4697 | -3.495265 |   38.306247 |                                                                 |     3.90 |   60.00 |           |             238
  4829 | -3.495265 |   38.306247 |                                                                 |     3.90 |   60.00 |           |             281
  5119 | -3.495260 |   38.306352 | dense undergrowth present                                       |    11.63 |    6.00 |      4908 |                
  5201 | -3.495260 |   38.306352 | dense undergrowth present                                       |    11.63 |    6.00 |      4978 |                
  5070 | -3.495181 |   38.306166 |                                                                 |     8.15 |   25.00 |      4871 |                
  5149 | -3.495181 |   38.306166 |                                                                 |     8.15 |   25.00 |      4932 |                
  5168 | -3.495181 |   38.306347 | well managed                                                    |     5.94 |   30.00 |           |             338
  5036 | -3.495181 |   38.306166 |                                                                 |     8.15 |   25.00 |      4847 |                
  5185 | -3.495138 |   38.306282 | well managed                                                    |     3.90 |   15.00 |      4962 |                
  4999 | -3.495138 |   38.306238 | Well Managed tree      


# get tree measurement duplicates only in FMNR module(fmnr_species)


```sql
SELECT * FROM duplicates
where fmnr_species_id is not null order by latitude;


5249 | -3.494499 | 38.306105 |                                             |    10.74 |   48.00 |           |             350
  5259 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             356
  5256 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             353
  5254 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             351
  5258 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             355
  5255 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             352
  5257 | -3.494499 | 38.306105 |                                           |    10.74 |   48.00 |           |             354
 


  id   | latitude  | longitude |                                        comment                                         | accuracy | rcc_cbh | cohort_id | fmnr_species_id 
-------|-----------|-----------|----------------------------------------------------------------------------------------|----------|---------|-----------|-----------------
  4857 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             291
  4870 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             295
  4863 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             293
  5240 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             344
  4852 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             287
  4892 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             304
  4882 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             299
  4878 | -3.495394 | 38.306062 | free has three branches multipuple stems                                               |     5.10 |   25.00 |           |             297
  4827 | -3.495348 | 38.306071 | multiple trees steaming from one stump                                                 |     5.86 |   25.00 |           |             279
  4695 | -3.495348 | 38.306071 | multiple trees steaming from one stump                                                 |     5.86 |   25.00 |           |             236
  5206 | -3.495273 | 38.306058 | very straight poles                                                                    |     8.48 |   17.00 |           |             341
  5208 | -3.495273 | 38.306058 | very straight poles                                                                    |     8.48 |   17.00 |           |             343
  4829 | -3.495265 | 38.306247 |                                                                                        |     3.90 |   60.00 |           |             281
  4697 | -3.495265 | 38.306247 |                                                                                        |     3.90 |   60.00 |           |             238
  5168 | -3.495181 | 38.306347 | well managed                                                                           |     5.94 |   30.00 |           |             338
  4999 | -3.495138 | 38.306238 | Well Managed tree                                                                      |     3.90 |   30.00 |           |             308
  4871 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             296
  4879 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             298
  4858 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             292
  4883 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             300
  5241 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             345
  4864 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             294
  4853 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             288
  4893 | -3.495118 | 38.306282 | Many branches multipuple stems                                                         |     5.64 |   45.00 |           |             305
  5205 | -3.495117 | 38.306286 | well managed                                                                           |     3.94 |   30.00 |           |             340
  5207 | -3.495117 | 38.306286 | well managed                                                                           |     3.94 |   30.00 |           |             342
  4828 | -3.495103 | 38.306238 | has soft vains                                                                         |     3.90 |   45.00 |           |             280
```
## cleaning solution

- choose the dpl record to keep. `4857` with species id `291`
- delete the duplicates in the tree measurement table where id is;
    - `4870, 4863, 5240, 4852, 4892, 4882, 4878`
    - for the deleted/duplicate tree measurements, delete their 
      - **usages** and 
      - **management practices** based on the species ids `295, 293, 344, 287, 304, 299, 297`
  
```sql
create or replace function delete_dpls(species_id INTEGER)
return void as $$

begin
  delete from respi_tree_measurement where fmnr_species_id = species_id;
  delete from respi_fmnr_tree_usage where fmnr_species_id = species_id;
  delete from respi_fmnr_management_practices where fmnr_species_id = species_id;

end;
$$ language plpgsql;

```

## find out whether the entries are in test project. 
- if yes, do not delete plot info, delete the duplicate entry and exit the function.

## 1. get the entries for duplicate species

```sql
regreen=> select fmnr_entry_id 
  from respi_fmnr_species 
  where id 
  in (295, 293, 344, 287, 304, 299, 297);

 fmnr_entry_id 
---------------
           290
           293
           294
           295
           296
           300
           317
(7 rows)
```
## 2. for these entries, get their plot ids.

```sql
regreen=> select * from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id in (295, 293, 344, 287, 304, 299, 297)
  );

 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | date_fmnr_started 
-----+-------------------------------+----------------+--------------+---------+------------+-------------------
 290 | 2024-04-22 16:37:54.457613+03 | 2024-04-22     |          798 |    3897 |          6 | 1982-01-01
 293 | 2024-04-22 16:40:00.202303+03 | 2024-04-22     |          798 |    3911 |          6 | 1982-01-01
 294 | 2024-04-22 16:41:37.123898+03 | 2024-04-22     |          798 |    3919 |          6 | 1982-01-01
 295 | 2024-04-22 16:43:24.586157+03 | 2024-04-22     |          798 |    3924 |          6 | 1982-01-01
 296 | 2024-04-22 16:45:57.078519+03 | 2024-04-22     |          798 |    3930 |          6 | 1982-01-01
 300 | 2024-04-23 07:35:28.17698+03  | 2024-04-22     |          798 |    3959 |          6 | 1982-01-01
 317 | 2024-04-23 16:24:47.999433+03 | 2024-04-22     |          798 |    4209 |          6 | 1982-01-01
(7 rows)

```

## 3. for these plot ids, get the **plot points** and the **plot polygons** for this plot

```sql

-------------------------plot points----------------------

regreen=> select * from respi_plot_points where plot_id in (
    select plot_id from respi_fmnr_entry where id in (
      select fmnr_entry_id from respi_fmnr_species where id =295
  ) 
);
  id   |         recorded_dte          | latitude  | longitude | altitude | accuracy | plot_id 
-------+-------------------------------+-----------+-----------+----------+----------+---------
 44850 | 2024-04-22 16:41:37.068945+03 | -3.495271 | 38.305982 |   935.80 |     3.90 |    3919
 44851 | 2024-04-22 16:41:37.071798+03 | -3.495183 | 38.305966 |   941.70 |     3.90 |    3919
 44852 | 2024-04-22 16:41:37.074879+03 | -3.495059 | 38.306032 |   941.70 |     3.90 |    3919
 44853 | 2024-04-22 16:41:37.077613+03 | -3.494931 | 38.306090 |   939.10 |     3.90 |    3919
 44854 | 2024-04-22 16:41:37.080096+03 | -3.495037 | 38.306238 |   934.50 |     3.90 |    3919
 44855 | 2024-04-22 16:41:37.082707+03 | -3.495230 | 38.306372 |   935.00 |     3.90 |    3919
 44856 | 2024-04-22 16:41:37.08547+03  | -3.495340 | 38.306292 |   935.10 |     3.90 |    3919
 44857 | 2024-04-22 16:41:37.088093+03 | -3.495446 | 38.306204 |   938.30 |     3.90 |    3919
 44858 | 2024-04-22 16:41:37.090875+03 | -3.495392 | 38.306135 |   937.70 |     3.90 |    3919
(9 rows)

regreen=> select * from respi_plot_points where plot_id in (
    select plot_id from respi_fmnr_entry where id in (
      select fmnr_entry_id from respi_fmnr_species where id =293
  ) 
);
  id   |         recorded_dte          | latitude  | longitude | altitude | accuracy | plot_id 
-------+-------------------------------+-----------+-----------+----------+----------+---------
 44781 | 2024-04-22 16:40:00.10155+03  | -3.495271 | 38.305982 |   935.80 |     3.90 |    3911
 44782 | 2024-04-22 16:40:00.105149+03 | -3.495183 | 38.305966 |   941.70 |     3.90 |    3911
 44783 | 2024-04-22 16:40:00.108666+03 | -3.495059 | 38.306032 |   941.70 |     3.90 |    3911
 44784 | 2024-04-22 16:40:00.126774+03 | -3.494931 | 38.306090 |   939.10 |     3.90 |    3911
 44785 | 2024-04-22 16:40:00.130444+03 | -3.495037 | 38.306238 |   934.50 |     3.90 |    3911
 44786 | 2024-04-22 16:40:00.134097+03 | -3.495230 | 38.306372 |   935.00 |     3.90 |    3911
 44787 | 2024-04-22 16:40:00.158012+03 | -3.495340 | 38.306292 |   935.10 |     3.90 |    3911
 44788 | 2024-04-22 16:40:00.161896+03 | -3.495446 | 38.306204 |   938.30 |     3.90 |    3911
 44789 | 2024-04-22 16:40:00.165596+03 | -3.495392 | 38.306135 |   937.70 |     3.90 |    3911
(9 rows)

-------------------------plot polygons------------------------

regreen=> select id, plot_id, actual_size from respi_plot_polygon where plot_id in (
    select plot_id from respi_fmnr_entry where id in (
      select fmnr_entry_id from respi_fmnr_species where id = 295
  ) 
);
  id  | plot_id | actual_size 
------+---------+-------------
 3538 |    3919 |            
(1 row)

regreen=> select id, plot_id, actual_size from respi_plot_polygon where plot_id in (
    select plot_id from respi_fmnr_entry where id in (
      select fmnr_entry_id from respi_fmnr_species where id = 293
  ) 
);
  id  | plot_id | actual_size 
------+---------+-------------
 3530 |    3911 |            
(1 row)


```

## 4. for these plot ids, get the plot info from plots table
```sql
regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id in (295, 293, 344, 287, 304, 299, 297)
  ));

id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3924 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 3919 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 4209 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 3930 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 3959 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 3911 | QUWC |           0.20 |            0.15 | INDIVIDUAL
 3897 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(7 rows)

```

### for every specie, find its plot.

```sql
regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=295                                   
  ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3919 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=293
  ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3911 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=344
    ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 4209 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=287
    ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3897 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=304
  ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3959 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=299
  ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3930 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

regreen=> select id, name, estimated_size, calculated_size, plot_ownership_type from respi_plots where id in (
  select plot_id from respi_fmnr_entry where id in (
    select fmnr_entry_id from respi_fmnr_species where id=297
  ));
  id  | name | estimated_size | calculated_size | plot_ownership_type 
------+------+----------------+-----------------+---------------------
 3924 | QUWC |           0.20 |            0.15 | INDIVIDUAL
(1 row)

```

