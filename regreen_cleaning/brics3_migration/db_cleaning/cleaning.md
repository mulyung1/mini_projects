

## Waterpoints

#### Problem

uploaded brics3 microcatchment and waterpoints data under username 'benards'.

|   Module   | Time Uploaded       | uname   | record count
|------------|---------------------|---------|------------
| watepoints | 10:24:46 - 10:23:32 | benards | 46
| halfmoons  | 15:49:46 - 16:00:00 | benards | 55

1. get uname id for 'benards'

```sql
regreen_local_jan2026=# select id, username from respi_regreeningusers where username='benards';
 id | username
----+----------
 34 | benards
(1 row)

```

2. get the waterpoint records 
- uploaded by 'benards'
- in Test, BRCiS III projects,
- uploaded between 10:23 to 10:24 on Jan 26

```sql
select 
    rent.*, 
    proj.project_name 
from 
    respi_rangeland_entry rent 
left join 
    respi_projects proj on proj.id=rent.project_id 
where 
    rent.collector_id = 34 and 
    proj.id in (93, 6) and 
    rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';

 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit | project_name
-----+-------------------------------+----------------+--------------+---------+------------+------------+--------------
 851 | 2026-01-26 10:23:32.633362+03 | 2024-12-27     |           34 |   21522 |         93 | False      | BRCiS III
 852 | 2026-01-26 10:23:34.870125+03 | 2025-03-31     |           34 |   21523 |         93 | False      | BRCiS III
 853 | 2026-01-26 10:23:36.060464+03 | 2025-03-29     |           34 |   21524 |         93 | False      | BRCiS III
 854 | 2026-01-26 10:23:41.142464+03 | 2025-04-15     |           34 |   21525 |         93 | False      | BRCiS III
 855 | 2026-01-26 10:23:43.190366+03 | 2025-04-16     |           34 |   21526 |         93 | False      | BRCiS III
 856 | 2026-01-26 10:23:44.522844+03 | 2025-04-16     |           34 |   21527 |         93 | False      | BRCiS III
 857 | 2026-01-26 10:23:45.73056+03  | 2025-04-16     |           34 |   21528 |         93 | False      | BRCiS III
 858 | 2026-01-26 10:23:46.956007+03 | 2025-04-16     |           34 |   21529 |         93 | False      | BRCiS III
 859 | 2026-01-26 10:23:48.113225+03 | 2025-04-16     |           34 |   21530 |         93 | False      | BRCiS III
 860 | 2026-01-26 10:23:49.281501+03 | 2025-04-16     |           34 |   21531 |         93 | False      | BRCiS III
 861 | 2026-01-26 10:23:50.548221+03 | 2025-04-16     |           34 |   21532 |         93 | False      | BRCiS III
 862 | 2026-01-26 10:23:51.686908+03 | 2025-04-17     |           34 |   21533 |         93 | False      | BRCiS III
 863 | 2026-01-26 10:23:54.711855+03 | 2025-04-17     |           34 |   21534 |         93 | False      | BRCiS III
 864 | 2026-01-26 10:23:55.845087+03 | 2025-04-17     |           34 |   21535 |         93 | False      | BRCiS III
 865 | 2026-01-26 10:23:57.074484+03 | 2025-04-17     |           34 |   21536 |         93 | False      | BRCiS III
 866 | 2026-01-26 10:23:58.272053+03 | 2025-04-17     |           34 |   21537 |         93 | False      | BRCiS III
 867 | 2026-01-26 10:23:59.423624+03 | 2025-04-17     |           34 |   21538 |         93 | False      | BRCiS III
 868 | 2026-01-26 10:24:00.645156+03 | 2025-01-03     |           34 |   21539 |         93 | False      | BRCiS III
 869 | 2026-01-26 10:24:01.843537+03 | 2024-10-12     |           34 |   21540 |         93 | False      | BRCiS III
 870 | 2026-01-26 10:24:02.987542+03 | 2025-04-22     |           34 |   21541 |         93 | False      | BRCiS III
 871 | 2026-01-26 10:24:09.110747+03 | 2025-04-23     |           34 |   21542 |         93 | False      | BRCiS III
 872 | 2026-01-26 10:24:10.975616+03 | 2025-04-23     |           34 |   21543 |         93 | False      | BRCiS III
 873 | 2026-01-26 10:24:15.103118+03 | 2025-04-23     |           34 |   21544 |         93 | False      | BRCiS III
 874 | 2026-01-26 10:24:16.844473+03 | 2025-05-06     |           34 |   21545 |         93 | False      | BRCiS III
 875 | 2026-01-26 10:24:18.042753+03 | 2024-12-31     |           34 |   21546 |         93 | False      | BRCiS III
 876 | 2026-01-26 10:24:19.166631+03 | 2025-09-02     |           34 |   21547 |         93 | False      | BRCiS III
 877 | 2026-01-26 10:24:21.493688+03 | 2025-09-02     |           34 |   21548 |         93 | False      | BRCiS III
 878 | 2026-01-26 10:24:23.375528+03 | 2025-09-02     |           34 |   21549 |         93 | False      | BRCiS III
 879 | 2026-01-26 10:24:24.761504+03 | 2025-09-02     |           34 |   21550 |         93 | False      | BRCiS III
 880 | 2026-01-26 10:24:25.976189+03 | 2025-09-02     |           34 |   21551 |         93 | False      | BRCiS III
 881 | 2026-01-26 10:24:27.488324+03 | 2025-09-02     |           34 |   21552 |         93 | False      | BRCiS III
 882 | 2026-01-26 10:24:28.809855+03 | 2025-04-21     |           34 |   21553 |          6 | False      | Test
 883 | 2026-01-26 10:24:30.08014+03  | 2025-04-22     |           34 |   21554 |          6 | False      | Test
 884 | 2026-01-26 10:24:31.342524+03 | 2025-01-11     |           34 |   21555 |         93 | False      | BRCiS III
 885 | 2026-01-26 10:24:32.584138+03 | 2025-01-13     |           34 |   21556 |         93 | False      | BRCiS III
 886 | 2026-01-26 10:24:33.748781+03 | 2025-01-14     |           34 |   21557 |         93 | False      | BRCiS III
 887 | 2026-01-26 10:24:35.26057+03  | 2025-01-15     |           34 |   21558 |         93 | False      | BRCiS III
 888 | 2026-01-26 10:24:36.595734+03 | 2025-01-16     |           34 |   21559 |         93 | False      | BRCiS III
 889 | 2026-01-26 10:24:37.812993+03 | 2025-01-17     |           34 |   21560 |         93 | False      | BRCiS III
 890 | 2026-01-26 10:24:39.132439+03 | 2025-01-17     |           34 |   21561 |         93 | False      | BRCiS III
 891 | 2026-01-26 10:24:40.415519+03 | 2025-01-18     |           34 |   21562 |         93 | False      | BRCiS III
 892 | 2026-01-26 10:24:41.835011+03 | 2025-01-19     |           34 |   21563 |         93 | False      | BRCiS III
 893 | 2026-01-26 10:24:43.110827+03 | 2025-03-15     |           34 |   21564 |         93 | False      | BRCiS III
 894 | 2026-01-26 10:24:44.34633+03  | 2025-03-18     |           34 |   21565 |         93 | False      | BRCiS III
 895 | 2026-01-26 10:24:45.668394+03 | 2025-03-17     |           34 |   21566 |         93 | False      | BRCiS III
 896 | 2026-01-26 10:24:46.843411+03 | 2025-04-16     |           34 |   21567 |         93 | False      | BRCiS III
(46 rows)

```

3. get waterpoint ids to be deleted

```sql
select 
    rent.*, 
    proj.project_name, 
    wps.id as wps_id, 
    wps.comments 
from 
    respi_rangeland_entry rent 
left join 
    respi_projects proj on proj.id=rent.project_id 
left join respi_waterpoints wps on wps.rangleland_entry_id=rent.id 
where 
    rent.collector_id = 34 and
    proj.id in (93, 6) and 
    rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit | project_name | wps_id |                             comments
-----+-------------------------------+----------------+--------------+---------+------------+------------+--------------+--------+------------------------------------------------------------------
 851 | 2026-01-26 10:23:32.633362+03 | 2024-12-27     |           34 |   21522 |         93 | False      | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 | 2025-03-31     |           34 |   21523 |         93 | False      | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 | 2025-03-29     |           34 |   21524 |         93 | False      | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 | 2025-04-15     |           34 |   21525 |         93 | False      | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 855 | 2026-01-26 10:23:43.190366+03 | 2025-04-16     |           34 |   21526 |         93 | False      | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 | 2025-04-16     |           34 |   21527 |         93 | False      | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  | 2025-04-16     |           34 |   21528 |         93 | False      | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 | 2025-04-16     |           34 |   21529 |         93 | False      | BRCiS III    |    316 | wp_depth 2.0 wp_ownership others
 859 | 2026-01-26 10:23:48.113225+03 | 2025-04-16     |           34 |   21530 |         93 | False      | BRCiS III    |    317 | wp_depth 2.0 wp_ownership communal/village
 860 | 2026-01-26 10:23:49.281501+03 | 2025-04-16     |           34 |   21531 |         93 | False      | BRCiS III    |    318 | wp_depth 1000.0 wp_ownership communal/village
 861 | 2026-01-26 10:23:50.548221+03 | 2025-04-16     |           34 |   21532 |         93 | False      | BRCiS III    |    319 | wp_depth 1000.0 wp_ownership communal/village
 862 | 2026-01-26 10:23:51.686908+03 | 2025-04-17     |           34 |   21533 |         93 | False      | BRCiS III    |    320 | wp_depth 1000.0 wp_ownership communal/village
 863 | 2026-01-26 10:23:54.711855+03 | 2025-04-17     |           34 |   21534 |         93 | False      | BRCiS III    |    321 | wp_depth 1000.0 wp_ownership private/individual communal/village
 864 | 2026-01-26 10:23:55.845087+03 | 2025-04-17     |           34 |   21535 |         93 | False      | BRCiS III    |    322 | wp_depth 1.0 wp_ownership communal/village
 865 | 2026-01-26 10:23:57.074484+03 | 2025-04-17     |           34 |   21536 |         93 | False      | BRCiS III    |    323 | wp_depth 2.0 wp_ownership communal/village
 866 | 2026-01-26 10:23:58.272053+03 | 2025-04-17     |           34 |   21537 |         93 | False      | BRCiS III    |    324 | wp_depth 1000.0 wp_ownership communal/village
 867 | 2026-01-26 10:23:59.423624+03 | 2025-04-17     |           34 |   21538 |         93 | False      | BRCiS III    |    325 | wp_depth 20.0 wp_ownership communal/village
 868 | 2026-01-26 10:24:00.645156+03 | 2025-01-03     |           34 |   21539 |         93 | False      | BRCiS III    |    326 | wp_depth 6.0 wp_ownership communal/village
 869 | 2026-01-26 10:24:01.843537+03 | 2024-10-12     |           34 |   21540 |         93 | False      | BRCiS III    |    327 | wp_depth 5.0 wp_ownership communal/village
 870 | 2026-01-26 10:24:02.987542+03 | 2025-04-22     |           34 |   21541 |         93 | False      | BRCiS III    |    328 | wp_depth 5.0 wp_ownership communal/village
 871 | 2026-01-26 10:24:09.110747+03 | 2025-04-23     |           34 |   21542 |         93 | False      | BRCiS III    |    329 | wp_depth 8.0 wp_ownership communal/village
 872 | 2026-01-26 10:24:10.975616+03 | 2025-04-23     |           34 |   21543 |         93 | False      | BRCiS III    |    330 | wp_depth 3.0 wp_ownership communal/village
 873 | 2026-01-26 10:24:15.103118+03 | 2025-04-23     |           34 |   21544 |         93 | False      | BRCiS III    |    331 | wp_depth 8.0 wp_ownership communal/village
 874 | 2026-01-26 10:24:16.844473+03 | 2025-05-06     |           34 |   21545 |         93 | False      | BRCiS III    |    332 | wp_depth 168.0 wp_ownership private/individual communal/village
 875 | 2026-01-26 10:24:18.042753+03 | 2024-12-31     |           34 |   21546 |         93 | False      | BRCiS III    |    333 | wp_depth 11.0 wp_ownership communal/village
 876 | 2026-01-26 10:24:19.166631+03 | 2025-09-02     |           34 |   21547 |         93 | False      | BRCiS III    |    334 | wp_depth 3.0 wp_ownership communal/village
 877 | 2026-01-26 10:24:21.493688+03 | 2025-09-02     |           34 |   21548 |         93 | False      | BRCiS III    |    335 | wp_depth 3.0 wp_ownership communal/village
 878 | 2026-01-26 10:24:23.375528+03 | 2025-09-02     |           34 |   21549 |         93 | False      | BRCiS III    |    336 | wp_depth 3.0 wp_ownership communal/village
 879 | 2026-01-26 10:24:24.761504+03 | 2025-09-02     |           34 |   21550 |         93 | False      | BRCiS III    |    337 | wp_depth 12.0 wp_ownership communal/village
 880 | 2026-01-26 10:24:25.976189+03 | 2025-09-02     |           34 |   21551 |         93 | False      | BRCiS III    |    338 | wp_depth 12.0 wp_ownership communal/village
 881 | 2026-01-26 10:24:27.488324+03 | 2025-09-02     |           34 |   21552 |         93 | False      | BRCiS III    |    339 | wp_depth 12.0 wp_ownership communal/village
 882 | 2026-01-26 10:24:28.809855+03 | 2025-04-21     |           34 |   21553 |          6 | False      | Test         |    340 | wp_depth 8.0 wp_ownership communal/village
 883 | 2026-01-26 10:24:30.08014+03  | 2025-04-22     |           34 |   21554 |          6 | False      | Test         |    341 | wp_depth 100.0 wp_ownership communal/village
 884 | 2026-01-26 10:24:31.342524+03 | 2025-01-11     |           34 |   21555 |         93 | False      | BRCiS III    |    342 | wp_depth 2.0 wp_ownership communal/village
 885 | 2026-01-26 10:24:32.584138+03 | 2025-01-13     |           34 |   21556 |         93 | False      | BRCiS III    |    343 | wp_depth 3.0 wp_ownership communal/village
 886 | 2026-01-26 10:24:33.748781+03 | 2025-01-14     |           34 |   21557 |         93 | False      | BRCiS III    |    344 | wp_depth 2.0 wp_ownership communal/village
 887 | 2026-01-26 10:24:35.26057+03  | 2025-01-15     |           34 |   21558 |         93 | False      | BRCiS III    |    345 | wp_depth 105.0 wp_ownership communal/village
 888 | 2026-01-26 10:24:36.595734+03 | 2025-01-16     |           34 |   21559 |         93 | False      | BRCiS III    |    346 | wp_depth 130.0 wp_ownership communal/village
 889 | 2026-01-26 10:24:37.812993+03 | 2025-01-17     |           34 |   21560 |         93 | False      | BRCiS III    |    347 | wp_depth 69.0 wp_ownership private/individual
 890 | 2026-01-26 10:24:39.132439+03 | 2025-01-17     |           34 |   21561 |         93 | False      | BRCiS III    |    348 | wp_depth 75.0 wp_ownership private/individual
 891 | 2026-01-26 10:24:40.415519+03 | 2025-01-18     |           34 |   21562 |         93 | False      | BRCiS III    |    349 | wp_depth 2.0 wp_ownership communal/village
 892 | 2026-01-26 10:24:41.835011+03 | 2025-01-19     |           34 |   21563 |         93 | False      | BRCiS III    |    350 | wp_depth 8.0 wp_ownership communal/village
 893 | 2026-01-26 10:24:43.110827+03 | 2025-03-15     |           34 |   21564 |         93 | False      | BRCiS III    |    351 | wp_depth 300.0 wp_ownership communal/village
 894 | 2026-01-26 10:24:44.34633+03  | 2025-03-18     |           34 |   21565 |         93 | False      | BRCiS III    |    352 | wp_depth 3.0 wp_ownership communal/village
 895 | 2026-01-26 10:24:45.668394+03 | 2025-03-17     |           34 |   21566 |         93 | False      | BRCiS III    |    353 | wp_depth 25.0 wp_ownership communal/village
 896 | 2026-01-26 10:24:46.843411+03 | 2025-04-16     |           34 |   21567 |         93 | False      | BRCiS III    |    354 | wp_depth 2.0 wp_ownership others
(46 rows)
```


to delete waterpoint info... delete directly. i.e 

```sql
delete from respi_waterpoints where id = 354;
```

every intervention has an independent plot, so the plot, plot ponts and plot polygons for every row(46) will also be deleted.



### order of tables to clean
1. drop waterpoints
2. drop plot_points
3. drop plot_polygon
4. drop plots
5. drop rangeland_entry


```sql
DO $$
declare
    r record;
begin
    for r in
        select distinct
               rent.id as rent_id,
               rent.plot_id as plot_id
        from respi_rangeland_entry rent
        where 
            rent.collector_id = 34 and 
            rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03' and 
            rent.project_id in (93, 6) -- BRCiS III & Test respectively
    loop
        -- 1. waterpoints
        delete from respi_waterpoints where rangleland_entry_id = r.rent_id;

        -- 2. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 3. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 4. plots
        delete from respi_plots where id = r.plot_id;

        -- 5. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;

```




## Halfmoons

```sql
select 
    rent.*, 
    proj.project_name 
from 
    respi_rangeland_entry rent 
left join respi_projects proj on proj.id=rent.project_id 
where 
    rent.collector_id = 34 and 
    project_id in (93, 131) and
    rent.recorded_dte between '2026-01-26T15:40:46.858534' and '2026-01-26T16:10:00.704079';
  id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit | project_name
------+-------------------------------+----------------+--------------+---------+------------+------------+--------------
  969 | 2026-01-26 15:49:39.223122+03 | 2024-12-27     |           34 |   21656 |         93 | False      | BRCiS III
  970 | 2026-01-26 15:49:46.858534+03 | 2025-03-31     |           34 |   21657 |         93 | False      | BRCiS III
  971 | 2026-01-26 15:49:54.542692+03 | 2025-04-08     |           34 |   21658 |         93 | False      | BRCiS III
  972 | 2026-01-26 15:49:59.919613+03 | 2025-01-03     |           34 |   21659 |         93 | False      | BRCiS III
  973 | 2026-01-26 15:50:09.336181+03 | 2025-04-21     |           34 |   21660 |         93 | False      | BRCiS III
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III
  975 | 2026-01-26 15:50:45.455638+03 | 2025-04-23     |           34 |   21662 |         93 | False      | BRCiS III
  976 | 2026-01-26 15:50:52.37619+03  | 2025-04-23     |           34 |   21663 |         93 | False      | BRCiS III
  977 | 2026-01-26 15:51:03.495112+03 | 2025-05-06     |           34 |   21664 |         93 | False      | BRCiS III
  978 | 2026-01-26 15:51:21.628946+03 | 2025-05-07     |           34 |   21665 |         93 | False      | BRCiS III
  979 | 2026-01-26 15:51:32.799579+03 | 2025-05-29     |           34 |   21666 |         93 | False      | BRCiS III
  980 | 2026-01-26 15:51:44.078254+03 | 2025-07-07     |           34 |   21667 |         93 | False      | BRCiS III
  981 | 2026-01-26 15:51:50.471328+03 | 2025-07-21     |           34 |   21668 |         93 | False      | BRCiS III
  982 | 2026-01-26 15:52:06.312193+03 | 2025-07-21     |           34 |   21669 |         93 | False      | BRCiS III
  983 | 2026-01-26 15:52:22.212811+03 | 2024-12-31     |           34 |   21670 |         93 | False      | BRCiS III
  984 | 2026-01-26 15:52:33.271649+03 | 2025-07-06     |           34 |   21671 |        131 | False      | TERRA
  985 | 2026-01-26 15:53:57.147561+03 | 2025-07-07     |           34 |   21672 |        131 | False      | TERRA
  986 | 2026-01-26 15:54:59.544996+03 | 2025-01-11     |           34 |   21673 |         93 | False      | BRCiS III
  987 | 2026-01-26 15:55:12.17126+03  | 2025-01-12     |           34 |   21674 |         93 | False      | BRCiS III
  988 | 2026-01-26 15:55:21.279933+03 | 2025-01-12     |           34 |   21675 |         93 | False      | BRCiS III
  989 | 2026-01-26 15:55:31.384737+03 | 2025-01-12     |           34 |   21676 |         93 | False      | BRCiS III
  990 | 2026-01-26 15:55:40.383072+03 | 2025-01-13     |           34 |   21677 |         93 | False      | BRCiS III
  991 | 2026-01-26 15:55:51.559125+03 | 2025-01-13     |           34 |   21678 |         93 | False      | BRCiS III
  992 | 2026-01-26 15:56:02.842829+03 | 2025-01-14     |           34 |   21679 |         93 | False      | BRCiS III
  993 | 2026-01-26 15:56:11.212068+03 | 2025-01-15     |           34 |   21680 |         93 | False      | BRCiS III
  994 | 2026-01-26 15:56:18.937737+03 | 2025-01-16     |           34 |   21681 |         93 | False      | BRCiS III
  995 | 2026-01-26 15:56:28.39425+03  | 2025-01-23     |           34 |   21682 |         93 | False      | BRCiS III
  996 | 2026-01-26 15:56:38.039453+03 | 2025-01-23     |           34 |   21683 |         93 | False      | BRCiS III
  997 | 2026-01-26 15:56:46.353257+03 | 2025-01-19     |           34 |   21684 |         93 | False      | BRCiS III
  998 | 2026-01-26 15:56:56.309761+03 | 2025-01-23     |           34 |   21685 |         93 | False      | BRCiS III
  999 | 2026-01-26 15:57:04.524563+03 | 2024-09-24     |           34 |   21686 |         93 | False      | BRCiS III
 1000 | 2026-01-26 15:57:14.087485+03 | 2025-01-25     |           34 |   21687 |         93 | False      | BRCiS III
 1001 | 2026-01-26 15:57:22.308229+03 | 2025-01-25     |           34 |   21688 |         93 | False      | BRCiS III
 1002 | 2026-01-26 15:57:31.826505+03 | 2024-09-24     |           34 |   21689 |         93 | False      | BRCiS III
 1003 | 2026-01-26 15:57:40.050353+03 | 2024-10-24     |           34 |   21690 |         93 | False      | BRCiS III
 1004 | 2026-01-26 15:57:49.634379+03 | 2025-01-25     |           34 |   21691 |         93 | False      | BRCiS III
 1005 | 2026-01-26 15:57:57.796868+03 | 2024-09-24     |           34 |   21692 |         93 | False      | BRCiS III
 1006 | 2026-01-26 15:58:04.570738+03 | 2024-09-24     |           34 |   21693 |         93 | False      | BRCiS III
 1007 | 2026-01-26 15:58:11.343593+03 | 2025-01-26     |           34 |   21694 |         93 | False      | BRCiS III
 1008 | 2026-01-26 15:58:18.104572+03 | 2024-09-24     |           34 |   21695 |         93 | False      | BRCiS III
 1009 | 2026-01-26 15:58:27.776215+03 | 2025-01-26     |           34 |   21696 |         93 | False      | BRCiS III
 1010 | 2026-01-26 15:58:38.757113+03 | 2024-09-24     |           34 |   21697 |         93 | False      | BRCiS III
 1011 | 2026-01-26 15:58:49.744001+03 | 2024-09-24     |           34 |   21698 |         93 | False      | BRCiS III
 1012 | 2026-01-26 15:58:58.009989+03 | 2025-01-26     |           34 |   21699 |         93 | False      | BRCiS III
 1013 | 2026-01-26 15:59:07.561178+03 | 2024-09-24     |           34 |   21700 |         93 | False      | BRCiS III
 1014 | 2026-01-26 15:59:18.57244+03  | 2025-01-26     |           34 |   21701 |         93 | False      | BRCiS III
 1015 | 2026-01-26 15:59:26.769895+03 | 2024-09-24     |           34 |   21702 |         93 | False      | BRCiS III
 1016 | 2026-01-26 15:59:33.54619+03  | 2025-02-28     |           34 |   21703 |         93 | False      | BRCiS III
 1017 | 2026-01-26 15:59:43.59654+03  | 2025-03-26     |           34 |   21704 |         93 | False      | BRCiS III
 1018 | 2026-01-26 16:00:00.704079+03 | 2025-07-06     |           34 |   21705 |         93 | False      | BRCiS III
 1019 | 2026-01-26 16:00:13.871555+03 | 2025-07-07     |           34 |   21706 |         93 | False      | BRCiS III
(51 rows)
```


1. get all current and establishment status ids

```sql
select 
    rent.*, 
    proj.project_name, 
    est.id as microcatchment_establishement_id, 
    curr.id as microcatchment_current_status_id  
from 
    respi_rangeland_entry rent 
left join respi_projects proj on proj.id=rent.project_id 
left join respi_microcatchment_establishment est on est.rangleland_entry_id=rent.id 
left join respi_mirocatchment_current curr on curr.rangleland_entry_id =rent.id 
where 
    rent.collector_id = 34 and
    project_id in (93, 131) and
    rent.recorded_dte between '2026-01-26T15:40:46.858534' and '2026-01-26T16:10:00.704079';
  id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit | project_name | microcatchment_establishement_id |  microcatchment_current_status_id
------+-------------------------------+----------------+--------------+---------+------------+------------+--------------+----------------------------------+---------------------------------------
  969 | 2026-01-26 15:49:39.223122+03 | 2024-12-27     |           34 |   21656 |         93 | False      | BRCiS III    |                              358 |                                   347
  969 | 2026-01-26 15:49:39.223122+03 | 2024-12-27     |           34 |   21656 |         93 | False      | BRCiS III    |                              358 |                                   348
  969 | 2026-01-26 15:49:39.223122+03 | 2024-12-27     |           34 |   21656 |         93 | False      | BRCiS III    |                              358 |                                   349
  970 | 2026-01-26 15:49:46.858534+03 | 2025-03-31     |           34 |   21657 |         93 | False      | BRCiS III    |                              359 |                                   350
  970 | 2026-01-26 15:49:46.858534+03 | 2025-03-31     |           34 |   21657 |         93 | False      | BRCiS III    |                              359 |                                   351
  970 | 2026-01-26 15:49:46.858534+03 | 2025-03-31     |           34 |   21657 |         93 | False      | BRCiS III    |                              359 |                                   352
  971 | 2026-01-26 15:49:54.542692+03 | 2025-04-08     |           34 |   21658 |         93 | False      | BRCiS III    |                              360 |                                   353
  971 | 2026-01-26 15:49:54.542692+03 | 2025-04-08     |           34 |   21658 |         93 | False      | BRCiS III    |                              360 |                                   354
  971 | 2026-01-26 15:49:54.542692+03 | 2025-04-08     |           34 |   21658 |         93 | False      | BRCiS III    |                              360 |                                   355
  972 | 2026-01-26 15:49:59.919613+03 | 2025-01-03     |           34 |   21659 |         93 | False      | BRCiS III    |                              361 |                                   356
  972 | 2026-01-26 15:49:59.919613+03 | 2025-01-03     |           34 |   21659 |         93 | False      | BRCiS III    |                              361 |                                   357
  973 | 2026-01-26 15:50:09.336181+03 | 2025-04-21     |           34 |   21660 |         93 | False      | BRCiS III    |                              362 |                                   358
  973 | 2026-01-26 15:50:09.336181+03 | 2025-04-21     |           34 |   21660 |         93 | False      | BRCiS III    |                              362 |                                   359
  973 | 2026-01-26 15:50:09.336181+03 | 2025-04-21     |           34 |   21660 |         93 | False      | BRCiS III    |                              362 |                                   360
  973 | 2026-01-26 15:50:09.336181+03 | 2025-04-21     |           34 |   21660 |         93 | False      | BRCiS III    |                              362 |                                   361
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   362
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   363
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   364
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   365
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   366
  974 | 2026-01-26 15:50:28.311482+03 | 2024-10-12     |           34 |   21661 |         93 | False      | BRCiS III    |                              363 |                                   367
  975 | 2026-01-26 15:50:45.455638+03 | 2025-04-23     |           34 |   21662 |         93 | False      | BRCiS III    |                              364 |                                   368
  976 | 2026-01-26 15:50:52.37619+03  | 2025-04-23     |           34 |   21663 |         93 | False      | BRCiS III    |                              365 |                                   369
  976 | 2026-01-26 15:50:52.37619+03  | 2025-04-23     |           34 |   21663 |         93 | False      | BRCiS III    |                              365 |                                   370
  976 | 2026-01-26 15:50:52.37619+03  | 2025-04-23     |           34 |   21663 |         93 | False      | BRCiS III    |                              365 |                                   371
```

### order of tables deletion
1. drop rangeland trees - trees where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
2. drop rangeland grasses - grasses where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
3. drop microcatchments_current - has entries of interest(based on rent id). 
4. drop microcatchments_establishment - has entries of interest(based on rent id). 
5. drop plot points
6. drop plot polygon
7. drop plots
8. drop rangeland_entry

### deletion
```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.plot_id as plot_id,
            est.id as estab_id,
            curr.id as curr_id

        from respi_rangeland_entry rent
            left join respi_microcatchment_establishment est  on est.rangleland_entry_id = rent.id
            left join respi_mirocatchment_current curr on curr.rangleland_entry_id = rent.id
        where rent.collector_id = 34
          and rent.recorded_dte between
              '2026-01-26T15:40:46.858534'
          and '2026-01-26T16:10:00.704079'
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where mirocatchment_curr_tree_id = r.curr_id or mirocatchment_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where mirocatchment_curr_grass_id = r.curr_id or mirocatchment_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_mirocatchment_current where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_microcatchment_establishment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;

```


## iremoval

### inspection

```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where name in('uuid:067d64de-e69d-4f4b-bb9f-0ad8ce828677')
    );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 968 | 2026-01-26 15:43:56.510891+03 | 2025-05-06     |         5360 |   21655 |         93 | False
(1 row)

```

#### cleaning logic
1. drop rangeland trees - trees where `iremoval_grass_id` is matched to a rent id
2. drop rangeland grasses - grasses where  `iremoval_treee_id` is matched to a rent id
3. drop iremoval records - based on rangeland entry id
5. drop plot points
6. drop plot polygon
7. drop plots
8. drop rangeland_entry


### deletion

```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            irm.id as iremoval_id
        from respi_rangeland_entry rent
        left join respi_invasive_species_removal irm
            on rent.id = irm.rangleland_entry_id
        where rent.id =968
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where  invasive_species_removal_trees_id = r.iremoval_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where invasive_species_removal_grass_id = r.iremoval_id;

        --3 invasives
        delete from respi_invasive_species_removal where id = r.iremoval_id;

        -- 3. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 4. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 5. plots
        delete from respi_plots where id = r.plot_id;

        -- 6. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;
```


## econtrol
### soil bunds
#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where 
            name in ('uuid:2ca2ab31-bd46-4e9a-ab60-f5302fc183e9', 'uuid:41bbf3d3-c52d-4762-9891-1c0f741004df', 'uuid:df558d01-226f-4386-8489-6d93fc5bd57c', 'uuid:3e4fc751-d450-48f6-9381-4776f84813b3',                'uuid:678dc500-72ef-49ef-9466-45e835ed56c5', 'uuid:fb9ef9f3-f1c6-417c-aa89-c9df87a3bb71', 'uuid:8389e603-3c19-487b-891e-09be3216d068', 'uuid:c37c2898-5448-4fde-8f61-4b5f7574fec2', 'uuid:5c7ce128-3964-46a0-9d37-13199a1f8876', 'uuid:57a7e247-54e6-4250-871f-2f8332724077', 'uuid:eb1bef63-6909-4c81-9829-ec466c147c77', 'uuid:1e3fc6e8-4640-4f36-8a8c-d770e9c448d8')
        );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 956 | 2026-01-26 15:31:15.597066+03 | 2025-03-31     |          457 |   21643 |         93 | False
 957 | 2026-01-26 15:31:19.607226+03 | 2025-04-15     |         1839 |   21644 |         93 | False
 958 | 2026-01-26 15:31:25.083177+03 | 2025-04-15     |         4310 |   21645 |         93 | False
 959 | 2026-01-26 15:31:29.458719+03 | 2025-04-15     |         1839 |   21646 |         93 | False
 960 | 2026-01-26 15:31:35.031648+03 | 2025-04-23     |         5368 |   21647 |         93 | False
 961 | 2026-01-26 15:31:39.463952+03 | 2025-04-23     |         5368 |   21648 |         93 | False
 962 | 2026-01-26 15:31:45.046891+03 | 2025-05-15     |         1839 |   21649 |         93 | False
 963 | 2026-01-26 15:31:49.435751+03 | 2025-06-30     |         1839 |   21650 |        131 | False
 964 | 2026-01-26 15:31:54.988743+03 | 2025-01-13     |         4310 |   21651 |         93 | False
 965 | 2026-01-26 15:31:59.392767+03 | 2025-01-14     |         4310 |   21652 |         93 | False
 966 | 2026-01-26 15:32:03.292588+03 | 2025-01-16     |         4243 |   21653 |         93 | False
 967 | 2026-01-26 15:32:08.96351+03  | 2025-04-24     |         5368 |   21654 |         93 | False
(12 rows)
```


#### econtrol cleaning logic
1. drop rangeland trees - trees where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
2. drop rangeland grasses - grasses where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
3. drop erosion_control_current - has entries of interest(based on rent id). 
4. drop erosion_control_establishment - has entries of interest(based on rent id). 
5. drop plot points
6. drop plot polygon
7. drop plots
8. drop rangeland_entry

#### deletion
```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id in (956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967)
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;

```


### swales
#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where 
            name in ('uuid:1331b5be-46d6-48e0-9214-20783c424198', 'uuid:87f62109-3378-4cf0-afab-a8b00d16c7a0', 'uuid:0d49cc6d-e895-4b7f-a552-0ea79857aa36', 'uuid:16e7dbfa-89ff-4c17-a937-378089985c66', 'uuid:3939d745-7ac3-4820-b988-7fb40649b22e', 'uuid:9c989ebe-ba11-4e2b-834e-dfe7615435c9', 'uuid:d2072d2d-97ca-4a83-834a-c27e99188b48', 'uuid:a4eae44f-b36c-4cae-8421-7378bc91914f', 'uuid:e5677b65-835c-46ce-b5cb-89f53918868f', 'uuid:db39d4f3-44d1-40d4-b9ad-eecc08f99689', 'uuid:c0a0a739-a9b7-45cd-a4f4-d5a6041bba7e', 'uuid:9bc08ead-66d6-416e-9cfd-73e634f31332', 'uuid:8996dbb6-0d60-4b2c-a1e9-f51b47f547e8', 'uuid:f48df7a1-f40a-4814-9d6f-9ba469b9492b', 'uuid:ea395672-2d6c-4b55-af83-05c2a08bf3f7', 'uuid:b97e5134-6f45-4e89-961d-da10eda03d8d', 'uuid:fc7b8211-9071-4fc9-94a9-cf230349b9cb', 'uuid:f1d66b19-ecf9-44ae-93c2-726d589d7507', 'uuid:99bd20e3-47c6-45b0-817f-1bdaaec5b772', 'uuid:ced5a8ec-c355-4e63-b78f-ceaf4adabfb5', 'uuid:e3d86805-1395-4ac0-82a0-5bed17b2c944', 'uuid:88700ace-dd82-4470-b4c4-8787180edfb4', 'uuid:13dbc9d1-0b45-471c-b590-e36b51780385', 'uuid:ad362004-5efb-4d98-a3cf-f8cf463d6fd7', 'uuid:11a82c12-e47a-44e5-bab7-18344ba4ad77', 'uuid:f13fe3b7-c5d3-4ced-bfa1-b23537e275b6', 'uuid:18957170-6ad1-437e-91d2-2e7eee65aae5', 'uuid:7a7df9e0-2c76-4842-a963-c513f14b3dce', 'uuid:d7f64eec-5435-4468-96cd-ca25834561b4', 'uuid:901943c9-a6e9-445a-aaf3-441397991c45', 'uuid:c8452e84-ab62-4002-93db-9fac83d8ae65', 'uuid:d3eb123b-3f83-4ba9-a834-407e8f313ed0', 'uuid:ce8e3710-14af-4b1c-90f4-1d7308d1a48d', 'uuid:13264977-558a-4501-803e-193a61ce7b93', 'uuid:ab40534c-e63e-4c6d-9079-58299b13b419', 'uuid:a23d76d2-a9fd-4a74-a414-d8b941f3b16e', 'uuid:ebaf8192-4369-430d-8965-f59f402e6246', 'uuid:e1d5f7d2-83af-4a3d-af33-9da6849add4f', 'uuid:3e7ca76a-7dd1-40b9-93d4-18a9f848dcfe', 'uuid:8624e7be-1d0c-4918-ba6f-94896ee7d1e0', 'uuid:b7d4c3bc-e83f-476b-b0bd-d8c3de6e2b0a', 'uuid:aba484fa-b677-4b57-8bae-d6182f94fe85', 'uuid:8c9152f4-c1e1-4d91-93ea-c7fc07806a94', 'uuid:fd451770-807d-468a-a30b-512f82e004af', 'uuid:c3b6a7b3-b381-4e96-b060-cabf49e7cec1')
        );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 900 | 2026-01-26 10:33:15.511102+03 | 2024-12-27     |         4300 |   21571 |         93 | False
 901 | 2026-01-26 10:33:16.974124+03 | 2025-03-31     |          457 |   21572 |         93 | False
 902 | 2026-01-26 10:33:18.936534+03 | 2025-04-08     |         5113 |   21573 |         93 | False
 903 | 2026-01-26 10:33:20.276462+03 | 2025-04-21     |         2495 |   21574 |         93 | False
 904 | 2026-01-26 10:33:21.888702+03 | 2024-10-12     |         2495 |   21575 |         93 | False
 905 | 2026-01-26 10:33:23.35335+03  | 2025-04-23     |         5368 |   21576 |         93 | False
 906 | 2026-01-26 10:33:24.763575+03 | 2025-04-23     |         5368 |   21577 |         93 | False
 907 | 2026-01-26 10:33:26.19454+03  | 2025-07-21     |         5368 |   21578 |         93 | False
 908 | 2026-01-26 10:33:27.774113+03 | 2024-12-31     |         4300 |   21579 |         93 | False
 909 | 2026-01-26 10:33:29.418354+03 | 2025-09-02     |         5368 |   21580 |         93 | False
 910 | 2026-01-26 10:33:30.598196+03 | 2025-09-02     |         5368 |   21581 |         93 | False
 911 | 2026-01-26 10:33:31.823867+03 | 2025-09-02     |         5368 |   21582 |         93 | False
 912 | 2026-01-26 10:33:33.014498+03 | 2025-09-03     |         5368 |   21583 |         93 | False
 913 | 2026-01-26 15:07:33.284407+03 | 2025-01-11     |         4300 |   21600 |         93 | False
 914 | 2026-01-26 15:07:40.265976+03 | 2025-01-12     |         3228 |   21601 |         93 | False
 915 | 2026-01-26 15:07:45.922388+03 | 2025-01-12     |         5113 |   21602 |         93 | False
 916 | 2026-01-26 15:07:51.588678+03 | 2025-01-12     |         5113 |   21603 |         93 | False
 917 | 2026-01-26 15:07:57.236456+03 | 2025-01-16     |         4243 |   21604 |         93 | False
 918 | 2026-01-26 15:08:03.194112+03 | 2025-01-23     |         4548 |   21605 |         93 | False
 919 | 2026-01-26 15:08:07.143637+03 | 2025-01-23     |         4257 |   21606 |         93 | False
 920 | 2026-01-26 15:08:11.939372+03 | 2025-01-19     |         4257 |   21607 |         93 | False
 921 | 2026-01-26 15:08:17.021672+03 | 2025-01-23     |         4548 |   21608 |         93 | False
 922 | 2026-01-26 15:08:21.147713+03 | 2024-09-24     |         3726 |   21609 |         93 | False
 923 | 2026-01-26 15:08:25.063569+03 | 2025-01-25     |         4257 |   21610 |         93 | False
 924 | 2026-01-26 15:08:28.960096+03 | 2025-01-25     |         4257 |   21611 |         93 | False
 925 | 2026-01-26 15:08:32.839911+03 | 2024-09-24     |         3726 |   21612 |         93 | False
 926 | 2026-01-26 15:08:37.607999+03 | 2024-10-24     |         4257 |   21613 |         93 | False
 927 | 2026-01-26 15:08:41.759289+03 | 2025-01-25     |         4257 |   21614 |         93 | False
 928 | 2026-01-26 15:08:45.702825+03 | 2024-09-24     |         3726 |   21615 |         93 | False
 929 | 2026-01-26 15:08:50.382259+03 | 2024-09-24     |         3726 |   21616 |         93 | False
 930 | 2026-01-26 15:08:55.363803+03 | 2025-01-26     |         4257 |   21617 |         93 | False
 931 | 2026-01-26 15:08:59.469242+03 | 2024-09-24     |         3726 |   21618 |         93 | False
 932 | 2026-01-26 15:09:03.357142+03 | 2025-01-26     |         4257 |   21619 |         93 | False
 933 | 2026-01-26 15:09:07.255719+03 | 2024-09-24     |         4257 |   21620 |         93 | False
 934 | 2026-01-26 15:09:11.135483+03 | 2024-09-24     |         3726 |   21621 |         93 | False
 935 | 2026-01-26 15:09:15.195199+03 | 2025-01-26     |         4548 |   21622 |         93 | False
 936 | 2026-01-26 15:09:19.119889+03 | 2024-09-24     |         3726 |   21623 |         93 | False
 937 | 2026-01-26 15:09:23.833774+03 | 2025-01-26     |         4257 |   21624 |         93 | False
 938 | 2026-01-26 15:09:27.947178+03 | 2024-09-24     |         4548 |   21625 |         93 | False
 939 | 2026-01-26 15:09:31.760888+03 | 2025-02-28     |         4300 |   21626 |         93 | False
 940 | 2026-01-26 15:09:37.445232+03 | 2025-03-10     |         1839 |   21627 |         93 | False
 941 | 2026-01-26 15:09:42.412833+03 | 2025-03-26     |         3228 |   21628 |         93 | False
 942 | 2026-01-26 15:09:46.52647+03  | 2025-07-07     |         2226 |   21629 |         93 | False
(43 rows)
```


#### delete
```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from 
            respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id between 900 and 942
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;

```


### contours
#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where 
            name in ('uuid:202ce50b-2bb7-46df-ae2f-fc5dbf488be7', 'uuid:194825bd-d88e-4e43-90a9-f543d748eb07', 'uuid:600f692e-6a5e-406d-80a2-d95f2d417080', 'uuid:de055a13-caa7-4b2d-8f12-92c9dc1fa663', 'uuid:e924c3c5-b9fe-43c3-abd3-19699d1b3670', 'uuid:2bfcd705-4db8-4e02-bc3b-ead0e28d7461', 'uuid:a0084932-3068-4f63-9cc1-4f59b4ac6fa9', 'uuid:0a0153cb-9abe-49ac-9f40-3caabdbaa6d7', 'uuid:e0813f39-0683-4fd6-ac2b-52b610471e55')
    );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 952 | 2026-01-26 15:24:47.872011+03 | 2025-01-03     |         2226 |   21639 |         93 | False
 953 | 2026-01-26 15:24:55.625012+03 | 2025-04-23     |         5364 |   21640 |         93 | False
 954 | 2026-01-26 15:25:00.033374+03 | 2025-01-16     |         4243 |   21641 |         93 | False
 955 | 2026-01-26 15:25:06.494167+03 | 2025-03-25     |         1839 |   21642 |         93 | False

```

#### delete

```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id between 952 and 955
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;

```

### rock_dams

#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where 
            name in ('fbad898a87704c61a5aa2422b9cc2bd5')
    );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 943 | 2026-01-26 15:16:52.708634+03 | 2025-04-23     |         5364 |   21630 |         93 | False
(1 row)

```
#### delete

```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id = 943
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;
```


### gabions

#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where name in ('4e05a03319874d9e8e6d6d93a98a8549', '28f5d92ab34f4e09997c70b9ac9c09b9', 'a2248eed0dcd4e30a3ff6127463d8cb7', '3ff55409a4d74ff580825c7cb24123c5', '4a7f1333762c4ab5a6c6a1df649bd5f7', '800cab0c32114810b522ac5106f397f6', '98cd5c6acf9f401982c5e7d37da33f59', 'd390d03baf254032b41860fadb72b950')
    );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 944 | 2026-01-26 15:21:04.295347+03 | 2024-10-12     |         2495 |   21631 |         93 | False
 945 | 2026-01-26 15:21:10.832094+03 | 2025-05-17     |         1894 |   21632 |         93 | False
 946 | 2026-01-26 15:21:16.43199+03  | 2025-05-17     |         1894 |   21633 |         93 | False
 947 | 2026-01-26 15:21:22.41324+03  | 2025-01-13     |         1894 |   21634 |         93 | False
 948 | 2026-01-26 15:21:28.408845+03 | 2025-03-15     |         1894 |   21635 |         93 | False
 949 | 2026-01-26 15:21:34.417632+03 | 2025-03-16     |         1894 |   21636 |         93 | False
 950 | 2026-01-26 15:21:38.85438+03  | 2025-03-11     |         1839 |   21637 |         93 | False
 951 | 2026-01-26 15:21:42.82055+03  | 2025-05-17     |         1894 |   21638 |         93 | False
(8 rows)
```

#### delete

```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id between 944 and 951
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;
```

### terraces

#### inspection
```sql
select * 
from 
    respi_rangeland_entry 
where 
    plot_id in(
        select id 
        from 
            respi_plots 
        where name in ('2c5e7bb635334f689694bb14eab49f27', 'b4ce1a6ab5374562a64a35af27cad3c4', 'f4d1dc15b03348f9acefbfe4dd5ed5f0')
    );
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 944 | 2026-01-26 15:21:04.295347+03 | 2024-10-12     |         2495 |   21631 |         93 | False
 945 | 2026-01-26 15:21:10.832094+03 | 2025-05-17     |         1894 |   21632 |         93 | False
 946 | 2026-01-26 15:21:16.43199+03  | 2025-05-17     |         1894 |   21633 |         93 | False
 947 | 2026-01-26 15:21:22.41324+03  | 2025-01-13     |         1894 |   21634 |         93 | False
 948 | 2026-01-26 15:21:28.408845+03 | 2025-03-15     |         1894 |   21635 |         93 | False
 949 | 2026-01-26 15:21:34.417632+03 | 2025-03-16     |         1894 |   21636 |         93 | False
 950 | 2026-01-26 15:21:38.85438+03  | 2025-03-11     |         1839 |   21637 |         93 | False
 951 | 2026-01-26 15:21:42.82055+03  | 2025-05-17     |         1894 |   21638 |         93 | False
(8 rows)
```

#### delete

```sql

DO $$
declare
    r record;
begin
    for r in
        select distinct
            rent.id as rent_id,
            rent.project_id  as project_id,
            rent.plot_id as plot_id,
            est.id  as estab_id,
            curr.id as curr_id
        from respi_rangeland_entry rent
        left join respi_erosion_control_establisment est
            on rent.id = est.rangleland_entry_id
        left join respi_erosion_control_currnt curr
            on curr.rangleland_entry_id = rent.id
        where rent.id between 897 and 899
          and rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    loop
        --1. rangeland current & established trees
        delete from respi_rangeland_trees where econtrol_curr_tree_id = r.curr_id or econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        delete from respi_rangeland_grasses where econtrol_curr_grass_id = r.curr_id or econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        delete from respi_erosion_control_currnt where rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        delete from respi_erosion_control_establisment where rangleland_entry_id = r.rent_id;

        -- 5. plot points
        delete from respi_plot_points where plot_id = r.plot_id;

        -- 6. plot polygon
        delete from respi_plot_polygon where plot_id = r.plot_id;

        -- 7. plots
        delete from respi_plots where id = r.plot_id;

        -- 8. rangeland entry
        delete from respi_rangeland_entry where id = r.rent_id;
    end loop;
end $$;
```

