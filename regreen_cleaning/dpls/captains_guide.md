This query gives us the duplicates.
```sql
--window function
with duplicates as (
    select *,count(*) over (partition by latitude, longitude) as kount, 
    row_number() over (partition by latitude, longitude order by latitude) as dup_rank
    from respi_tree_measurement
    )
    select latitude, longitude, comment, accuracy, rcc_cbh, cohort_id, fmnr_species_id, dup_rank
        from duplicates where kount>1 order by latitude;


 latitude  |  longitude  |                  commment                                                        | accuracy | rcc_cbh | cohort_id | fmnr_species_id 
-----------+-------------+----------------------------------------------------------------------------------+----------+---------+-----------+-----------------
 -3.495613 |   38.306280 | well managed                                                                     |     4.08 |   52.00 |      4899 |                
 -3.495613 |   38.306280 | well managed                                                                     |     4.08 |   52.00 |      4936 |                
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             304
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             344
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             299
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             297
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             295
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             293
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             291
 -3.495348 |   38.306071 | multiple trees steaming from one stump                                           |     5.86 |   25.00 |           |             236
 -3.495348 |   38.306071 | multiple trees steaming from one stump                                           |     5.86 |   25.00 |           |             279
 -3.495342 |   38.306054 | well managed                                                                     |     3.90 |    8.00 |      4946 |                
 -3.495342 |   38.306054 | well managed                                                                     |     3.90 |    8.00 |      4963 |                
 -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised                       |     3.84 |    8.00 |      4977 |                
 -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised                       |     3.84 |    8.00 |      4907 |                
 -3.495273 |   38.306058 | very straight poles                                                              |     8.48 |   17.00 |           |             341
 -3.495273 |   38.306058 | very straight poles                                                              |     8.48 |   17.00 |           |             343
 -3.495265 |   38.306247 |                                                                                  |     3.90 |   60.00 |           |             281
 -3.495265 |   38.306247 |                                                                                  |     3.90 |   60.00 |           |             238
 -3.495260 |   38.306352 | dense undergrowth present                                                        |    11.63 |    6.00 |      4978 |                
 -3.495260 |   38.306352 | dense undergrowth present                                                        |    11.63 |    6.00 |      4908 |                
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4932 |                
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4871 |                
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4847 |                

```

### problem
-  get rows that are only duplicates for one tree(lat,lon)
    -**why??** so that our cursor can loop through only duplicates and skip first record.
    - **advantage**: rows are not grouped into a single output(like aggregate calls would do).
        - every row retains its separate identity
        - a new column with the ranks is added.

- **solution**: use dense_rank() on the entire result set to rank the duplicates 

### dense_rank() function

- a [window function](https://www.postgresql.org/docs/current/tutorial-window.html)
- assigns a rank(id) to each row with no gaps for ties/duplicates
- the ranks are applied within a partion of the result set or the entire result set if the `PARTITION BY` clause is omitted
- the columns used to sort the data are specified in the `ORDER BY` clause

**Syntax**:
```sql
DENSE_RANK() OVER (PARTION BY column1, columns2,....ORDER BY sort_column1, sort_column2,...)
``` 
**Example** datasets and their ranking

- **10,20,30,40 -> 1,2,3,4**

- **10,20,20,60,60,60,80,90,90,90 -> 1,2,2,3,3,3,4,5,5,5**

## Applied Solution

```sql
SELECT trm.latitude, trm.longitude, trm.comment, trm.accuracy, trm.rcc_cbh, trm.cohort_id, trm.fmnr_species_id,
       --rank(group) the duplicates
       DENSE_RANK() OVER (ORDER BY trm.latitude, trm.longitude) AS dup_group
FROM respi_tree_measurement trm
JOIN (                        
    SELECT latitude, longitude
    FROM respi_tree_measurement
    GROUP BY latitude, longitude
    HAVING count(*) > 1
) dpls                          
ON trm.latitude = dpls.latitude 
AND trm.longitude = dpls.longitude
ORDER BY dup_group, trm.latitude;


 latitude  |  longitude  |                      comment                                                     | accuracy | rcc_cbh | cohort_id | fmnr_species_id | dup_group 
-----------+-------------+----------------------------------------------------------------------------------+----------+---------+-----------+-----------------+-----------
 -3.495613 |   38.306280 | well managed                                                                     |     4.08 |   52.00 |      4899 |                 |         1
 -3.495613 |   38.306280 | well managed                                                                     |     4.08 |   52.00 |      4936 |                 |         1
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             287 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             304 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             344 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             299 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             297 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             295 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             293 |         2
 -3.495394 |   38.306062 | free has three branches multipuple stems                                         |     5.10 |   25.00 |           |             291 |         2
 -3.495348 |   38.306071 | multiple trees steaming from one stump                                           |     5.86 |   25.00 |           |             236 |         3
 -3.495348 |   38.306071 | multiple trees steaming from one stump                                           |     5.86 |   25.00 |           |             279 |         3
 -3.495342 |   38.306054 | well managed                                                                     |     3.90 |    8.00 |      4946 |                 |         4
 -3.495342 |   38.306054 | well managed                                                                     |     3.90 |    8.00 |      4963 |                 |         4
 -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised                       |     3.84 |    8.00 |      4977 |                 |         5
 -3.495336 |   38.306050 | the bark has a sweet scent whose use is yet to be realised                       |     3.84 |    8.00 |      4907 |                 |         5
 -3.495273 |   38.306058 | very straight poles                                                              |     8.48 |   17.00 |           |             341 |         6
 -3.495273 |   38.306058 | very straight poles                                                              |     8.48 |   17.00 |           |             343 |         6
 -3.495265 |   38.306247 |                                                                                  |     3.90 |   60.00 |           |             281 |         7
 -3.495265 |   38.306247 |                                                                                  |     3.90 |   60.00 |           |             238 |         7
 -3.495260 |   38.306352 | dense undergrowth present                                                        |    11.63 |    6.00 |      4978 |                 |         8
 -3.495260 |   38.306352 | dense undergrowth present                                                        |    11.63 |    6.00 |      4908 |                 |         8
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4932 |                 |         9
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4871 |                 |         9
 -3.495181 |   38.306166 |                                                                                  |     8.15 |   25.00 |      4847 |                 |         9
 ```



## the function
```sql
do $$
declare
    rec record;
begin
    for rec in (
        with duplicates as (
                select *, count(*) over (partition by latitude, longitude) as kount, 
                row_number() over (partition by latitude, longitude order by latitude) as dup_rank
                from respi_tree_measurement
            )
            select latitude, longitude, comment, accuracy, rcc_cbh, cohort_id, fmnr_species_id, dup_rank
             from duplicates where kount>1 and dup_rank > 1 --skip first row in each group/partiion
    ) loop
    --real work now begins
        raise notice 'Processing....%', rec;

    end loop;
end $$;
```


## fmnr function
```sql
do $$
declare
    --declare record variables to be avle to loop over rows 
    rec record;
    usage record;
    measurement record;
    management record;
    species record;
    fmnr_entry record;
    fmnr_plot_points record;
    fmnr_plot_polygon record;
    plots record;

begin
    for rec in (
        with duplicates as (
                select *, count(*) over (partition by latitude, longitude) as kount, 
                row_number() over (partition by latitude, longitude order by latitude) as dup_rank
                from respi_tree_measurement
            )
            select latitude, longitude, comment, accuracy, rcc_cbh, cohort_id, fmnr_species_id, dup_rank
             from duplicates where 
                kount > 1 and --only duplicates
                fmnr_species_id is not null and --only fmnr species are considered
                dup_rank > 1 --skip first row in each group/partiion
                --limit 10
    ) loop
    --real work now begins
        raise notice 'Processing..........% at occurence number - %', rec.fmnr_species_id, rec.dup_rank;
        --get tree usages
        for usage in 
            select usg.id as usage_id, usg.tree_usage as fmnr_tree_usage, usg.fmnr_species_id as fmnr_species_id from respi_fmnr_tree_usage usg where fmnr_species_id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Tree usage....% with a  usage id - %', usage, usage.usage_id; 
            delete from respi_fmnr_tree_usage where id = usage.usage_id;
        end loop;
        --get tree measurements
        for measurement in 
            select msm.* from respi_tree_measurement msm where fmnr_species_id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Tree measurement....% with a  measurement id - %', measurement, measurement.id;
            delete from respi_tree_measurement where id = measurement.id;
        end loop;
        --get management practices
        for management in
            select * from respi_fmnr_management_practices where fmnr_species_id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Management practices...% with a  management id - %', management, management.id;
            delete from respi_fmnr_management_practices where id = management.id;
        end loop;
        --get the species
        for species in 
            select * from respi_fmnr_species where id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Species...% with a  species_id - %', species, species.id;
            delete from respi_fmnr_species where id = species.id;
        end loop;
        --get the fmnr entries
        for fmnr_entry in 
            select spcs.id, ent.id as fmnr_entry_id, ent.collector_id as collector_id, ent.plot_id as fmnr_plot_id, ent.project_id from respi_fmnr_species spcs inner join respi_fmnr_entry ent on ent.id=spcs.fmnr_entry_id where spcs.id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Entry.....% with a  fmnr_entry id - %', fmnr_entry, fmnr_entry.fmnr_entry_id;
            delete from respi_fmnr_entry where id = fmnr_entry.fmnr_entry_id;
        end loop;
        --get the plot points
        for fmnr_plot_points in
            select spcs.id, plp.id as plot_points_id, plp.latitude as plot_lat, plp.longitude as plot_lon, plp.accuracy as plot_accuracy, plp.plot_id as plot_id from respi_fmnr_species spcs inner join respi_fmnr_entry ent on ent.id=spcs.fmnr_entry_id inner join respi_plot_points plp on plp.plot_id=ent.plot_id where spcs.id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Plot Points....% with a  plot_point_id - %', fmnr_plot_points, fmnr_plot_points.plot_points_id;
            delete from respi_plot_points where id = fmnr_plot_points.plot_points_id;
        end loop;

        --get the plot polygons
        for fmnr_plot_polygon in
            select spcs.id, plp.id as plot_polygon_id, plp.plot_id as plot_id, plp.actual_size as polygon_actual_size from respi_fmnr_species spcs inner join respi_fmnr_entry ent on ent.id=spcs.fmnr_entry_id inner join respi_plot_polygon plp on plp.plot_id=ent.plot_id where spcs.id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Plot Polygon...% with a  plot_polygon_id - %', fmnr_plot_polygon, fmnr_plot_polygon.plot_polygon_id;
            delete from respi_plot_polygon where id = fmnr_plot_polygon.plot_polygon_id;
        end loop;
        
        for plots in 
            select spcs.id as fmnr_species_id, plt.id as plot_id, plt.estimated_size, plt.photo_url from respi_fmnr_species spcs inner join respi_fmnr_entry ent on ent.id=spcs.fmnr_entry_id inner join respi_plots plt on plt.id=ent.plot_id where spcs.id=rec.fmnr_species_id
        loop
            --deletion here
            raise notice 'FMNR Plot...% with a  plot_id - %', plots, plots.plot_id;
            delete from respi_plots where id = plots.plot_id;
        end loop;
    end loop;
end $$;
```



ref:
- https://www.postgresql.org/docs/current/tutorial-window.html
- https://www.geeksforgeeks.org/postgresql/postgresql-record-type-variable/

