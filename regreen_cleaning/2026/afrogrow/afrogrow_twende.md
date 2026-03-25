# problem
user collected a tp entry of id 12712 under twende, that was meant for Afrogrow

# solution
update the entry from project_id `11` to project_id ``


- get tp entry of interest
```sql
regreen=> select ent.*, usr.username, prj.project_name from respi_tree_planting_entry ent inner join respi_regreeningusers usr on usr.id=ent.collector_id join respi_projects prj on prj.id=ent.project_id where ent.id = 12712;
  id   |         recorded_dte          | date_collected | collector_id | plot_id | project_id | username | project_name
-------+-------------------------------+----------------+--------------+---------+------------+----------+--------------
 12712 | 2026-03-17 20:06:26.970349+03 | 2026-03-17     |         1056 |   22306 |         11 | Muthuri  | TWENDE
(1 row)
```

- get afrogrow project

```sql
regreen=> select * from respi_projects where project_name='Afrogrow';
 id  |         recorded_dte         | project_name | project_description | project_logo_url | country_id | country_name | created_by_id | organization_id |     project_website_url      | qr_code_name
-----+------------------------------+--------------+---------------------+------------------+------------+--------------+---------------+-----------------+------------------------------+--------------
 154 | 2026-03-16 17:12:00.42634+03 | Afrogrow     | Afrogrow project    |                  |            |              |            35 |               1 | https://www.cifor-icraf.org/ | Afrogrow.png
(1 row)
```

- update project is to 154

```sql
update respi_tree_planting_entry set project_id=154 where id = 12712;
```