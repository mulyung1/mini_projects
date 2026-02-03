

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

2. get the waterpoint records uploaded by 'benards'

```sql
regreen_local_jan2026=# select rent.*, proj.project_name from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
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
regreen_local_jan2026=# select rent.*, proj.project_name, wps.id as wps_id, wps.comments from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id left join respi_waterpoints wps on wps.rangleland_entry_id=rent.id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
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

3. get plots(names) for these waterpoints

```sql
regreen_local_jan2026=# select rent.id, rent.recorded_dte, rent.collector_id, rent.plot_id, plt.name,plt.has_crops, proj.project_name, wps.id as wps_id, wps.comments from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id left join respi_waterpoints wps on wps.rangleland_entry_id=rent.id left join respi_plots plt on plt.id=rent.plot_id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
 id  |         recorded_dte          | collector_id | plot_id |                   name                    | has_crops | project_name | wps_id |                             comments
-----+-------------------------------+--------------+---------+-------------------------------------------+-----------+--------------+--------+------------------------------------------------------------------
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 |           34 |   21529 | uuid:11acdc1a-8f77-4700-91c0-ed310ce73dc1 | f         | BRCiS III    |    316 | wp_depth 2.0 wp_ownership others
 859 | 2026-01-26 10:23:48.113225+03 |           34 |   21530 | uuid:2a18511e-d898-44d0-bfd0-dbf621c6e520 | f         | BRCiS III    |    317 | wp_depth 2.0 wp_ownership communal/village
 860 | 2026-01-26 10:23:49.281501+03 |           34 |   21531 | uuid:2ac46903-7d89-4f70-a3be-b6284ae0a85d | f         | BRCiS III    |    318 | wp_depth 1000.0 wp_ownership communal/village
 861 | 2026-01-26 10:23:50.548221+03 |           34 |   21532 | uuid:232c321b-62c5-4f74-a6ff-ac51db64a5fd | f         | BRCiS III    |    319 | wp_depth 1000.0 wp_ownership communal/village
 862 | 2026-01-26 10:23:51.686908+03 |           34 |   21533 | uuid:67a58d5e-ca84-40e8-993b-13722c51ebcf | f         | BRCiS III    |    320 | wp_depth 1000.0 wp_ownership communal/village
 863 | 2026-01-26 10:23:54.711855+03 |           34 |   21534 | uuid:3fd36f2f-2f45-449e-a4e9-8d33697e425e | f         | BRCiS III    |    321 | wp_depth 1000.0 wp_ownership private/individual communal/village
 864 | 2026-01-26 10:23:55.845087+03 |           34 |   21535 | uuid:1b409e64-9bbd-4563-b54f-615d0c3c96f9 | f         | BRCiS III    |    322 | wp_depth 1.0 wp_ownership communal/village
 865 | 2026-01-26 10:23:57.074484+03 |           34 |   21536 | uuid:e6b67c61-4a7a-453b-a026-2524b189767c | f         | BRCiS III    |    323 | wp_depth 2.0 wp_ownership communal/village
 866 | 2026-01-26 10:23:58.272053+03 |           34 |   21537 | uuid:0386af66-d8c3-4cc3-9ad5-74e73ace85dc | f         | BRCiS III    |    324 | wp_depth 1000.0 wp_ownership communal/village
 867 | 2026-01-26 10:23:59.423624+03 |           34 |   21538 | uuid:a9563087-6ccb-4b5f-8dcd-02d76bea3b91 | f         | BRCiS III    |    325 | wp_depth 20.0 wp_ownership communal/village
 868 | 2026-01-26 10:24:00.645156+03 |           34 |   21539 | uuid:eacf04ce-e243-42ec-9c43-d9cd2b715cf3 | f         | BRCiS III    |    326 | wp_depth 6.0 wp_ownership communal/village
 869 | 2026-01-26 10:24:01.843537+03 |           34 |   21540 | uuid:e6a1596f-188e-4194-a818-5f8baf593bfa | f         | BRCiS III    |    327 | wp_depth 5.0 wp_ownership communal/village
 870 | 2026-01-26 10:24:02.987542+03 |           34 |   21541 | uuid:f5aae752-4c28-4798-b7d4-a25f84a6c1a6 | f         | BRCiS III    |    328 | wp_depth 5.0 wp_ownership communal/village
 871 | 2026-01-26 10:24:09.110747+03 |           34 |   21542 | uuid:869ec802-7628-4d9c-b69a-e67984d5097b | f         | BRCiS III    |    329 | wp_depth 8.0 wp_ownership communal/village
 872 | 2026-01-26 10:24:10.975616+03 |           34 |   21543 | uuid:b790fdba-c7d5-42b1-8ae1-d5d361744a9f | f         | BRCiS III    |    330 | wp_depth 3.0 wp_ownership communal/village
 873 | 2026-01-26 10:24:15.103118+03 |           34 |   21544 | uuid:0f88a92c-0321-433a-9aee-a8b4f3c3381b | f         | BRCiS III    |    331 | wp_depth 8.0 wp_ownership communal/village
 874 | 2026-01-26 10:24:16.844473+03 |           34 |   21545 | uuid:cb192702-7825-44ac-afd7-10a71a7a7fb2 | f         | BRCiS III    |    332 | wp_depth 168.0 wp_ownership private/individual communal/village
 875 | 2026-01-26 10:24:18.042753+03 |           34 |   21546 | uuid:a0204769-6ca7-47c9-86a3-8db1465308d1 | f         | BRCiS III    |    333 | wp_depth 11.0 wp_ownership communal/village
 876 | 2026-01-26 10:24:19.166631+03 |           34 |   21547 | uuid:0426165b-91ff-4933-9168-9696de5bbfd1 | f         | BRCiS III    |    334 | wp_depth 3.0 wp_ownership communal/village
 877 | 2026-01-26 10:24:21.493688+03 |           34 |   21548 | uuid:400ab4fa-38fc-48a4-9b01-ee0aaa2e1f32 | f         | BRCiS III    |    335 | wp_depth 3.0 wp_ownership communal/village
 878 | 2026-01-26 10:24:23.375528+03 |           34 |   21549 | uuid:b68a5057-c8fc-43c1-abf3-0b174fc13375 | f         | BRCiS III    |    336 | wp_depth 3.0 wp_ownership communal/village
 879 | 2026-01-26 10:24:24.761504+03 |           34 |   21550 | uuid:739736c3-9b3c-41fc-b9dc-3ee215d7f674 | f         | BRCiS III    |    337 | wp_depth 12.0 wp_ownership communal/village
 880 | 2026-01-26 10:24:25.976189+03 |           34 |   21551 | uuid:7881cbae-3376-4071-89e5-55f8708a06d9 | f         | BRCiS III    |    338 | wp_depth 12.0 wp_ownership communal/village
 881 | 2026-01-26 10:24:27.488324+03 |           34 |   21552 | uuid:55158257-406b-4380-b02e-7300105d5017 | f         | BRCiS III    |    339 | wp_depth 12.0 wp_ownership communal/village
 882 | 2026-01-26 10:24:28.809855+03 |           34 |   21553 | uuid:4a9f4f80-0697-4a44-b111-98d85b7c07ee | f         | Test         |    340 | wp_depth 8.0 wp_ownership communal/village
 883 | 2026-01-26 10:24:30.08014+03  |           34 |   21554 | uuid:eb90db61-7d32-4d10-9c83-87438427a99f | f         | Test         |    341 | wp_depth 100.0 wp_ownership communal/village
 884 | 2026-01-26 10:24:31.342524+03 |           34 |   21555 | uuid:707083d1-0d4f-4ed6-bc62-2a6292566903 | f         | BRCiS III    |    342 | wp_depth 2.0 wp_ownership communal/village
 885 | 2026-01-26 10:24:32.584138+03 |           34 |   21556 | uuid:eeb20946-bc4e-4854-bcdc-60d65341d1b4 | f         | BRCiS III    |    343 | wp_depth 3.0 wp_ownership communal/village
 886 | 2026-01-26 10:24:33.748781+03 |           34 |   21557 | uuid:f4a0707b-496d-4ab1-a002-dd0f60c2503b | f         | BRCiS III    |    344 | wp_depth 2.0 wp_ownership communal/village
 887 | 2026-01-26 10:24:35.26057+03  |           34 |   21558 | uuid:f81aa10c-45c2-4180-a66b-0e3cfee35709 | f         | BRCiS III    |    345 | wp_depth 105.0 wp_ownership communal/village
 888 | 2026-01-26 10:24:36.595734+03 |           34 |   21559 | uuid:7368bb35-f7c9-4118-8322-c2fe7d74ea1a | f         | BRCiS III    |    346 | wp_depth 130.0 wp_ownership communal/village
 889 | 2026-01-26 10:24:37.812993+03 |           34 |   21560 | uuid:3fc70aa3-77a5-4e0b-a607-8d46c71458e3 | f         | BRCiS III    |    347 | wp_depth 69.0 wp_ownership private/individual
 890 | 2026-01-26 10:24:39.132439+03 |           34 |   21561 | uuid:1579b1ea-01c6-4280-bb43-b8b73cbd22a7 | f         | BRCiS III    |    348 | wp_depth 75.0 wp_ownership private/individual
 891 | 2026-01-26 10:24:40.415519+03 |           34 |   21562 | uuid:0995adbb-4139-4050-bf2a-1e0c72bdc745 | f         | BRCiS III    |    349 | wp_depth 2.0 wp_ownership communal/village
 892 | 2026-01-26 10:24:41.835011+03 |           34 |   21563 | uuid:a36ffc5f-a997-4620-9760-53f3ca265c80 | f         | BRCiS III    |    350 | wp_depth 8.0 wp_ownership communal/village
 893 | 2026-01-26 10:24:43.110827+03 |           34 |   21564 | uuid:1d36b88d-2aad-4205-969a-3fb8c834f2a0 | f         | BRCiS III    |    351 | wp_depth 300.0 wp_ownership communal/village
 894 | 2026-01-26 10:24:44.34633+03  |           34 |   21565 | uuid:447b5002-6f78-43a6-b944-432e372bc494 | f         | BRCiS III    |    352 | wp_depth 3.0 wp_ownership communal/village
 895 | 2026-01-26 10:24:45.668394+03 |           34 |   21566 | uuid:d5b2d0dd-004f-4de5-8136-719273baede6 | f         | BRCiS III    |    353 | wp_depth 25.0 wp_ownership communal/village
 896 | 2026-01-26 10:24:46.843411+03 |           34 |   21567 | uuid:0eccc5a1-b1a1-4ad8-aad9-4a5b63872043 | f         | BRCiS III    |        |
(46 rows)

```

4. for these plots, get 
- plot polygons
- plot points

**plot polygons**
```sql
regreen_local_jan2026=# select rent.id, rent.recorded_dte, rent.collector_id, rent.plot_id, plp.id as plot_polygon_id, plt.name,plt.has_crops, proj.project_name, wps.id as wps_id, wps.comments from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id left join respi_waterpoints wps on wps.rangleland_entry_id=rent.id left join respi_plots plt on plt.id=rent.plot_id left join respi_plot_polygon plp on plp.plot_id=plt.id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
 id  |         recorded_dte          | collector_id | plot_id | plot_polygon_id |                   name                    | has_crops | project_name | wps_id |                             comments
-----+-------------------------------+--------------+---------+-----------------+-------------------------------------------+-----------+--------------+--------+------------------------------------------------------------------
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 |           34 |   21529 |           19694 | uuid:11acdc1a-8f77-4700-91c0-ed310ce73dc1 | f         | BRCiS III    |    316 | wp_depth 2.0 wp_ownership others
 859 | 2026-01-26 10:23:48.113225+03 |           34 |   21530 |           19695 | uuid:2a18511e-d898-44d0-bfd0-dbf621c6e520 | f         | BRCiS III    |    317 | wp_depth 2.0 wp_ownership communal/village
 860 | 2026-01-26 10:23:49.281501+03 |           34 |   21531 |           19696 | uuid:2ac46903-7d89-4f70-a3be-b6284ae0a85d | f         | BRCiS III    |    318 | wp_depth 1000.0 wp_ownership communal/village
 861 | 2026-01-26 10:23:50.548221+03 |           34 |   21532 |           19697 | uuid:232c321b-62c5-4f74-a6ff-ac51db64a5fd | f         | BRCiS III    |    319 | wp_depth 1000.0 wp_ownership communal/village
 862 | 2026-01-26 10:23:51.686908+03 |           34 |   21533 |           19698 | uuid:67a58d5e-ca84-40e8-993b-13722c51ebcf | f         | BRCiS III    |    320 | wp_depth 1000.0 wp_ownership communal/village
 863 | 2026-01-26 10:23:54.711855+03 |           34 |   21534 |           19699 | uuid:3fd36f2f-2f45-449e-a4e9-8d33697e425e | f         | BRCiS III    |    321 | wp_depth 1000.0 wp_ownership private/individual communal/village
 864 | 2026-01-26 10:23:55.845087+03 |           34 |   21535 |           19700 | uuid:1b409e64-9bbd-4563-b54f-615d0c3c96f9 | f         | BRCiS III    |    322 | wp_depth 1.0 wp_ownership communal/village
 865 | 2026-01-26 10:23:57.074484+03 |           34 |   21536 |           19701 | uuid:e6b67c61-4a7a-453b-a026-2524b189767c | f         | BRCiS III    |    323 | wp_depth 2.0 wp_ownership communal/village
 866 | 2026-01-26 10:23:58.272053+03 |           34 |   21537 |           19702 | uuid:0386af66-d8c3-4cc3-9ad5-74e73ace85dc | f         | BRCiS III    |    324 | wp_depth 1000.0 wp_ownership communal/village
 867 | 2026-01-26 10:23:59.423624+03 |           34 |   21538 |           19703 | uuid:a9563087-6ccb-4b5f-8dcd-02d76bea3b91 | f         | BRCiS III    |    325 | wp_depth 20.0 wp_ownership communal/village
 868 | 2026-01-26 10:24:00.645156+03 |           34 |   21539 |           19704 | uuid:eacf04ce-e243-42ec-9c43-d9cd2b715cf3 | f         | BRCiS III    |    326 | wp_depth 6.0 wp_ownership communal/village
 869 | 2026-01-26 10:24:01.843537+03 |           34 |   21540 |           19705 | uuid:e6a1596f-188e-4194-a818-5f8baf593bfa | f         | BRCiS III    |    327 | wp_depth 5.0 wp_ownership communal/village
 870 | 2026-01-26 10:24:02.987542+03 |           34 |   21541 |           19706 | uuid:f5aae752-4c28-4798-b7d4-a25f84a6c1a6 | f         | BRCiS III    |    328 | wp_depth 5.0 wp_ownership communal/village
 871 | 2026-01-26 10:24:09.110747+03 |           34 |   21542 |           19707 | uuid:869ec802-7628-4d9c-b69a-e67984d5097b | f         | BRCiS III    |    329 | wp_depth 8.0 wp_ownership communal/village
 872 | 2026-01-26 10:24:10.975616+03 |           34 |   21543 |           19708 | uuid:b790fdba-c7d5-42b1-8ae1-d5d361744a9f | f         | BRCiS III    |    330 | wp_depth 3.0 wp_ownership communal/village
 873 | 2026-01-26 10:24:15.103118+03 |           34 |   21544 |           19709 | uuid:0f88a92c-0321-433a-9aee-a8b4f3c3381b | f         | BRCiS III    |    331 | wp_depth 8.0 wp_ownership communal/village
 874 | 2026-01-26 10:24:16.844473+03 |           34 |   21545 |           19710 | uuid:cb192702-7825-44ac-afd7-10a71a7a7fb2 | f         | BRCiS III    |    332 | wp_depth 168.0 wp_ownership private/individual communal/village
 875 | 2026-01-26 10:24:18.042753+03 |           34 |   21546 |           19711 | uuid:a0204769-6ca7-47c9-86a3-8db1465308d1 | f         | BRCiS III    |    333 | wp_depth 11.0 wp_ownership communal/village
 876 | 2026-01-26 10:24:19.166631+03 |           34 |   21547 |           19712 | uuid:0426165b-91ff-4933-9168-9696de5bbfd1 | f         | BRCiS III    |    334 | wp_depth 3.0 wp_ownership communal/village
 877 | 2026-01-26 10:24:21.493688+03 |           34 |   21548 |           19713 | uuid:400ab4fa-38fc-48a4-9b01-ee0aaa2e1f32 | f         | BRCiS III    |    335 | wp_depth 3.0 wp_ownership communal/village
 878 | 2026-01-26 10:24:23.375528+03 |           34 |   21549 |           19714 | uuid:b68a5057-c8fc-43c1-abf3-0b174fc13375 | f         | BRCiS III    |    336 | wp_depth 3.0 wp_ownership communal/village
 879 | 2026-01-26 10:24:24.761504+03 |           34 |   21550 |           19715 | uuid:739736c3-9b3c-41fc-b9dc-3ee215d7f674 | f         | BRCiS III    |    337 | wp_depth 12.0 wp_ownership communal/village
 880 | 2026-01-26 10:24:25.976189+03 |           34 |   21551 |           19716 | uuid:7881cbae-3376-4071-89e5-55f8708a06d9 | f         | BRCiS III    |    338 | wp_depth 12.0 wp_ownership communal/village
 881 | 2026-01-26 10:24:27.488324+03 |           34 |   21552 |           19717 | uuid:55158257-406b-4380-b02e-7300105d5017 | f         | BRCiS III    |    339 | wp_depth 12.0 wp_ownership communal/village
 882 | 2026-01-26 10:24:28.809855+03 |           34 |   21553 |           19718 | uuid:4a9f4f80-0697-4a44-b111-98d85b7c07ee | f         | Test         |    340 | wp_depth 8.0 wp_ownership communal/village
 883 | 2026-01-26 10:24:30.08014+03  |           34 |   21554 |           19719 | uuid:eb90db61-7d32-4d10-9c83-87438427a99f | f         | Test         |    341 | wp_depth 100.0 wp_ownership communal/village
 884 | 2026-01-26 10:24:31.342524+03 |           34 |   21555 |           19720 | uuid:707083d1-0d4f-4ed6-bc62-2a6292566903 | f         | BRCiS III    |    342 | wp_depth 2.0 wp_ownership communal/village
 885 | 2026-01-26 10:24:32.584138+03 |           34 |   21556 |           19721 | uuid:eeb20946-bc4e-4854-bcdc-60d65341d1b4 | f         | BRCiS III    |    343 | wp_depth 3.0 wp_ownership communal/village
 886 | 2026-01-26 10:24:33.748781+03 |           34 |   21557 |           19722 | uuid:f4a0707b-496d-4ab1-a002-dd0f60c2503b | f         | BRCiS III    |    344 | wp_depth 2.0 wp_ownership communal/village
 887 | 2026-01-26 10:24:35.26057+03  |           34 |   21558 |           19723 | uuid:f81aa10c-45c2-4180-a66b-0e3cfee35709 | f         | BRCiS III    |    345 | wp_depth 105.0 wp_ownership communal/village
 888 | 2026-01-26 10:24:36.595734+03 |           34 |   21559 |           19724 | uuid:7368bb35-f7c9-4118-8322-c2fe7d74ea1a | f         | BRCiS III    |    346 | wp_depth 130.0 wp_ownership communal/village
 889 | 2026-01-26 10:24:37.812993+03 |           34 |   21560 |           19725 | uuid:3fc70aa3-77a5-4e0b-a607-8d46c71458e3 | f         | BRCiS III    |    347 | wp_depth 69.0 wp_ownership private/individual
 890 | 2026-01-26 10:24:39.132439+03 |           34 |   21561 |           19726 | uuid:1579b1ea-01c6-4280-bb43-b8b73cbd22a7 | f         | BRCiS III    |    348 | wp_depth 75.0 wp_ownership private/individual
 891 | 2026-01-26 10:24:40.415519+03 |           34 |   21562 |           19727 | uuid:0995adbb-4139-4050-bf2a-1e0c72bdc745 | f         | BRCiS III    |    349 | wp_depth 2.0 wp_ownership communal/village
 892 | 2026-01-26 10:24:41.835011+03 |           34 |   21563 |           19728 | uuid:a36ffc5f-a997-4620-9760-53f3ca265c80 | f         | BRCiS III    |    350 | wp_depth 8.0 wp_ownership communal/village
 893 | 2026-01-26 10:24:43.110827+03 |           34 |   21564 |           19729 | uuid:1d36b88d-2aad-4205-969a-3fb8c834f2a0 | f         | BRCiS III    |    351 | wp_depth 300.0 wp_ownership communal/village
 894 | 2026-01-26 10:24:44.34633+03  |           34 |   21565 |           19730 | uuid:447b5002-6f78-43a6-b944-432e372bc494 | f         | BRCiS III    |    352 | wp_depth 3.0 wp_ownership communal/village
 895 | 2026-01-26 10:24:45.668394+03 |           34 |   21566 |           19731 | uuid:d5b2d0dd-004f-4de5-8136-719273baede6 | f         | BRCiS III    |    353 | wp_depth 25.0 wp_ownership communal/village
 896 | 2026-01-26 10:24:46.843411+03 |           34 |   21567 |           19732 | uuid:0eccc5a1-b1a1-4ad8-aad9-4a5b63872043 | f         | BRCiS III    |        |
(46 rows)
```


```sql

regreen_local_jan2026=# select rent.id, rent.recorded_dte, rent.collector_id, rent.plot_id, plp.id as plot_polygon_id, plps.id as plot_points_id, plt.name,plt.has_crops, proj.project_name, wps.id as wps_id, wps.comments from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id left join respi_waterpoints wps on wps.rangleland_entry_id=rent.id left join respi_plots plt on plt.id=rent.plot_id left join respi_plot_polygon plp on plp.plot_id=plt.id left join respi_plot_points plps on plps.plot_id=plt.id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26 10:23:32.633362+03' and '2026-01-26 10:24:47.633362+03';
 id  |         recorded_dte          | collector_id | plot_id | plot_polygon_id | plot_points_id |                   name                    | has_crops | project_name | wps_id |                             comments
-----+-------------------------------+--------------+---------+-----------------+----------------+-------------------------------------------+-----------+--------------+--------+------------------------------------------------------------------
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 |         185789 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 |         185790 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 |         185791 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 |         185792 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 851 | 2026-01-26 10:23:32.633362+03 |           34 |   21522 |           19687 |         185793 | uuid:e6b85764-ebd2-45b4-938a-bfedd7360931 | f         | BRCiS III    |    309 | wp_depth 14.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 |         185794 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 |         185795 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 |         185796 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 |         185797 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 852 | 2026-01-26 10:23:34.870125+03 |           34 |   21523 |           19688 |         185798 | uuid:1ed128ab-085c-4793-aea5-e9a78c988d63 | f         | BRCiS III    |    310 | wp_depth 12.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 |         185799 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 |         185800 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 |         185801 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 |         185802 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 853 | 2026-01-26 10:23:36.060464+03 |           34 |   21524 |           19689 |         185803 | uuid:9c74493e-ff93-445f-b243-a14ff4e4af41 | f         | BRCiS III    |    311 | wp_depth 4.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185804 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185805 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185806 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185807 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185808 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 854 | 2026-01-26 10:23:41.142464+03 |           34 |   21525 |           19690 |         185809 | uuid:f17afc33-041e-48fe-bf66-e32cc1ff1185 | f         | BRCiS III    |    312 | wp_depth 15.0 wp_ownership communal/village
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 |         185810 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 |         185811 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 |         185812 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 |         185813 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 855 | 2026-01-26 10:23:43.190366+03 |           34 |   21526 |           19691 |         185814 | uuid:4f270da3-f020-4019-b6b3-32212ae038a2 | f         | BRCiS III    |    313 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185815 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185816 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185817 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185818 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185819 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 856 | 2026-01-26 10:23:44.522844+03 |           34 |   21527 |           19692 |         185820 | uuid:ef1dd36e-4552-4c37-a9d4-ab8d747410f6 | f         | BRCiS III    |    314 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185821 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185822 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185823 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185824 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185825 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185826 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185827 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185828 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 857 | 2026-01-26 10:23:45.73056+03  |           34 |   21528 |           19693 |         185829 | uuid:65e2bbec-56aa-4b04-a398-092a2272169c | f         | BRCiS III    |    315 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 |           34 |   21529 |           19694 |         185830 | uuid:11acdc1a-8f77-4700-91c0-ed310ce73dc1 | f         | BRCiS III    |    316 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 |           34 |   21529 |           19694 |         185831 | uuid:11acdc1a-8f77-4700-91c0-ed310ce73dc1 | f         | BRCiS III    |    316 | wp_depth 2.0 wp_ownership others
 858 | 2026-01-26 10:23:46.956007+03 |           34 |   21529 |           19694 |         185832 | uuid:11acdc1a-8f77-4700-91c0-ed310ce73dc1 | f

```


cleaning logic
1. drop waterpoints
2. drop plot_points
3. drop plot_polygon
4. drop plots
5. drop rangeland_entry


```sql
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
               rent.id AS rent_id,
               rent.plot_id AS plot_id
        FROM respi_rangeland_entry rent
        WHERE rent.collector_id = 34
          AND rent.recorded_dte BETWEEN
              '2026-01-26 10:23:32.633362+03'
          AND '2026-01-26 10:24:47.633362+03'
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        -- 1. waterpoints
        DELETE FROM respi_waterpoints WHERE rangleland_entry_id = r.rent_id;

        -- 2. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 3. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 4. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 5. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;

```




## Halfmoons

```sql
regreen_local_jan2026=# select rent.*, proj.project_name from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26T15:40:46.858534' and '2026-01-26T16:10:00.704079';
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
regreen_local_jan2026=# select rent.*, proj.project_name, est.id as microcatchment_establishement_id, curr.id as microcatchment_current_status_id  from respi_rangeland_entry rent left join respi_projects proj on proj.id=rent.project_id left join respi_microcatchment_establishment est on est.rangleland_entry_id=rent.id left join respi_mirocatchment_current curr on curr.rangleland_entry_id =rent.id where rent.collector_id = 34 and rent.recorded_dte between '2026-01-26T15:40:46.858534' and '2026-01-26T16:10:00.704079';
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

cleaning logic
1. drop rangeland trees - trees where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
2. drop rangeland grasses - grasses where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
3. drop microcatchments_current - has entries of interest(based on rent id). 
4. drop microcatchments_establishment - has entries of interest(based on rent id). 
5. drop plot points
6. drop plot polygon
7. drop plots
8. drop rangeland_entry


```sql

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.plot_id AS plot_id,
            est.id AS estab_id,
            curr.id AS curr_id

        FROM respi_rangeland_entry rent
            LEFT JOIN respi_microcatchment_establishment est  ON est.rangleland_entry_id = rent.id
            LEFT JOIN respi_mirocatchment_current curr ON curr.rangleland_entry_id = rent.id
        WHERE rent.collector_id = 34
          AND rent.recorded_dte BETWEEN
              '2026-01-26T15:40:46.858534'
          AND '2026-01-26T16:10:00.704079'
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE mirocatchment_curr_tree_id = r.curr_id OR mirocatchment_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE mirocatchment_curr_grass_id = r.curr_id OR mirocatchment_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_mirocatchment_current WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_microcatchment_establishment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;

```

## econtrol
### soil bunds
### get the records of interest based on plot name
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in ('uuid:2ca2ab31-bd46-4e9a-ab60-f5302fc183e9', 'uuid:41bbf3d3-c52d-4762-9891-1c0f741004df', 'uuid:df558d01-226f-4386-8489-6d93fc5bd57c', 'uuid:3e4fc751-d450-48f6-9381-4776f84813b3', 'uuid:678dc500-72ef-49ef-9466-45e835ed56c5', 'uuid:fb9ef9f3-f1c6-417c-aa89-c9df87a3bb71', 'uuid:8389e603-3c19-487b-891e-09be3216d068', 'uuid:c37c2898-5448-4fde-8f61-4b5f7574fec2', 'uuid:5c7ce128-3964-46a0-9d37-13199a1f8876', 'uuid:57a7e247-54e6-4250-871f-2f8332724077', 'uuid:eb1bef63-6909-4c81-9829-ec466c147c77', 'uuid:1e3fc6e8-4640-4f36-8a8c-d770e9c448d8'));
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


### econtrol cleaning logic
1. drop rangeland trees - trees where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
2. drop rangeland grasses - grasses where `curr_id = current status id` & `est_id = establishment_id`(that is matched to a rent id).
3. drop erosion_control_current - has entries of interest(based on rent id). 
4. drop erosion_control_establishment - has entries of interest(based on rent id). 
5. drop plot points
6. drop plot polygon
7. drop plots
8. drop rangeland_entry





```sql

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id IN (956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967)
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;

```


### swales
#### inspection
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in ('uuid:1331b5be-46d6-48e0-9214-20783c424198', 'uuid:87f62109-3378-4cf0-afab-a8b00d16c7a0', 'uuid:0d49cc6d-e895-4b7f-a552-0ea79857aa36', 'uuid:16e7dbfa-89ff-4c17-a937-378089985c66', 'uuid:3939d745-7ac3-4820-b988-7fb40649b22e', 'uuid:9c989ebe-ba11-4e2b-834e-dfe7615435c9', 'uuid:d2072d2d-97ca-4a83-834a-c27e99188b48', 'uuid:a4eae44f-b36c-4cae-8421-7378bc91914f', 'uuid:e5677b65-835c-46ce-b5cb-89f53918868f', 'uuid:db39d4f3-44d1-40d4-b9ad-eecc08f99689', 'uuid:c0a0a739-a9b7-45cd-a4f4-d5a6041bba7e', 'uuid:9bc08ead-66d6-416e-9cfd-73e634f31332', 'uuid:8996dbb6-0d60-4b2c-a1e9-f51b47f547e8', 'uuid:f48df7a1-f40a-4814-9d6f-9ba469b9492b', 'uuid:ea395672-2d6c-4b55-af83-05c2a08bf3f7', 'uuid:b97e5134-6f45-4e89-961d-da10eda03d8d', 'uuid:fc7b8211-9071-4fc9-94a9-cf230349b9cb', 'uuid:f1d66b19-ecf9-44ae-93c2-726d589d7507', 'uuid:99bd20e3-47c6-45b0-817f-1bdaaec5b772', 'uuid:ced5a8ec-c355-4e63-b78f-ceaf4adabfb5', 'uuid:e3d86805-1395-4ac0-82a0-5bed17b2c944', 'uuid:88700ace-dd82-4470-b4c4-8787180edfb4', 'uuid:13dbc9d1-0b45-471c-b590-e36b51780385', 'uuid:ad362004-5efb-4d98-a3cf-f8cf463d6fd7', 'uuid:11a82c12-e47a-44e5-bab7-18344ba4ad77', 'uuid:f13fe3b7-c5d3-4ced-bfa1-b23537e275b6', 'uuid:18957170-6ad1-437e-91d2-2e7eee65aae5', 'uuid:7a7df9e0-2c76-4842-a963-c513f14b3dce', 'uuid:d7f64eec-5435-4468-96cd-ca25834561b4', 'uuid:901943c9-a6e9-445a-aaf3-441397991c45', 'uuid:c8452e84-ab62-4002-93db-9fac83d8ae65', 'uuid:d3eb123b-3f83-4ba9-a834-407e8f313ed0', 'uuid:ce8e3710-14af-4b1c-90f4-1d7308d1a48d', 'uuid:13264977-558a-4501-803e-193a61ce7b93', 'uuid:ab40534c-e63e-4c6d-9079-58299b13b419', 'uuid:a23d76d2-a9fd-4a74-a414-d8b941f3b16e', 'uuid:ebaf8192-4369-430d-8965-f59f402e6246', 'uuid:e1d5f7d2-83af-4a3d-af33-9da6849add4f', 'uuid:3e7ca76a-7dd1-40b9-93d4-18a9f848dcfe', 'uuid:8624e7be-1d0c-4918-ba6f-94896ee7d1e0', 'uuid:b7d4c3bc-e83f-476b-b0bd-d8c3de6e2b0a', 'uuid:aba484fa-b677-4b57-8bae-d6182f94fe85', 'uuid:8c9152f4-c1e1-4d91-93ea-c7fc07806a94', 'uuid:fd451770-807d-468a-a30b-512f82e004af', 'uuid:c3b6a7b3-b381-4e96-b060-cabf49e7cec1'));
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
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id BETWEEN 900 AND 942
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;

```


### contours
#### inspection
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in
('uuid:202ce50b-2bb7-46df-ae2f-fc5dbf488be7', 'uuid:194825bd-d88e-4e43-90a9-f543d748eb07', 'uuid:600f692e-6a5e-406d-80a2-d95f2d417080', 'uuid:de055a13-caa7-4b2d-8f12-92c9dc1fa663', 'uuid:e924c3c5-b9fe-43c3-abd3-19699d1b3670', 'uuid:2bfcd705-4db8-4e02-bc3b-ead0e28d7461', 'uuid:a0084932-3068-4f63-9cc1-4f59b4ac6fa9', 'uuid:0a0153cb-9abe-49ac-9f40-3caabdbaa6d7', 'uuid:e0813f39-0683-4fd6-ac2b-52b610471e55'));
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
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id BETWEEN 952 AND 955
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;

```

### rock_dams

#### inspection
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in
('fbad898a87704c61a5aa2422b9cc2bd5'));
 id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | is_revisit
-----+-------------------------------+----------------+--------------+---------+------------+------------
 943 | 2026-01-26 15:16:52.708634+03 | 2025-04-23     |         5364 |   21630 |         93 | False
(1 row)

```
#### delete

```sql

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id = 943
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;
```


### gabions

#### inspection
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in
('4e05a03319874d9e8e6d6d93a98a8549', '28f5d92ab34f4e09997c70b9ac9c09b9', 'a2248eed0dcd4e30a3ff6127463d8cb7', '3ff55409a4d74ff580825c7cb24123c5', '4a7f1333762c4ab5a6c6a1df649bd5f7', '800cab0c32114810b522ac5106f397f6', '98cd5c6acf9f401982c5e7d37da33f59', 'd390d03baf254032b41860fadb72b950'));
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
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id BETWEEN 944 AND 951
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;
```

### terraces

#### inspection
```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in
('2c5e7bb635334f689694bb14eab49f27', 'b4ce1a6ab5374562a64a35af27cad3c4', 'f4d1dc15b03348f9acefbfe4dd5ed5f0'));
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
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            est.id  AS estab_id,
            curr.id AS curr_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_erosion_control_establisment est
            ON rent.id = est.rangleland_entry_id
        LEFT JOIN respi_erosion_control_currnt curr
            ON curr.rangleland_entry_id = rent.id
        WHERE rent.id BETWEEN 897 AND 899
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE econtrol_curr_tree_id = r.curr_id OR econtrol_estab_tree_id = r.estab_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE econtrol_curr_grass_id = r.curr_id OR econtrol_estab_grass_id = r.estab_id;

        --3 . microcatchment current
        DELETE FROM respi_erosion_control_currnt WHERE rangleland_entry_id = r.rent_id;

        --4. microcatchment establishment
        DELETE FROM respi_erosion_control_establisment WHERE rangleland_entry_id = r.rent_id;

        -- 5. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 6. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 7. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 8. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;
```


## iremoval

### inspection

```sql
regreen_local_jan2026=# select * from respi_rangeland_entry where plot_id in(select id from respi_plots where name in('uuid:067d64de-e69d-4f4b-bb9f-0ad8ce828677'));
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


#### deletion

```sql

DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN
        SELECT DISTINCT
            rent.id AS rent_id,
            rent.project_id  AS project_id,
            rent.plot_id AS plot_id,
            irm.id as iremoval_id
        FROM respi_rangeland_entry rent
        LEFT JOIN respi_invasive_species_removal irm
            ON rent.id = irm.rangleland_entry_id
        WHERE rent.id =968
          AND rent.project_id in (93, 131) -- BRCiS III & TERRA respectively
    LOOP
        --1. rangeland current & established trees
        DELETE FROM respi_rangeland_trees WHERE  invasive_species_removal_trees_id = r.iremoval_id;

        --2. rangeland current & established grasses
        DELETE FROM respi_rangeland_grasses WHERE invasive_species_removal_grass_id = r.iremoval_id;

        --3 invasives
        DELETE FROM respi_invasive_species_removal WHERE id = r.iremoval_id;

        -- 3. plot points
        DELETE FROM respi_plot_points WHERE plot_id = r.plot_id;

        -- 4. plot polygon
        DELETE FROM respi_plot_polygon WHERE plot_id = r.plot_id;

        -- 5. plots
        DELETE FROM respi_plots WHERE id = r.plot_id;

        -- 6. rangeland entry
        DELETE FROM respi_rangeland_entry WHERE id = r.rent_id;
    END LOOP;
END $$;
```

