## problem
some tp data in UKPact_Nbs project is from the countries
- Ghana
- Guinea

## findings
### find the tp data based on uploaded_date and user first_name

```sql
regreen=> select tpe.*, prj.project_name, prj.country_name, usr.first_name, usr.last_name from respi_tree_planting_entry tpe inner join respi_projects prj on prj.id=tpe.project_id  inner join respi_regreeningusers usr on usr.id=tpe.collector_id where tpe.recorded_dte::text like '2025-05-07 15:57%' and usr.first_name='Mohamed Fanta';
  id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | project_name | country_name |  first_name   | last_name 
------+-------------------------------+----------------+--------------+---------+------------+--------------+--------------+---------------+-----------
 6109 | 2025-05-07 15:57:11.963571+03 | 2025-03-28     |         3268 |   12293 |         12 | UKPact_NbS   | Kenya        | Mohamed Fanta | TOUNKARA
(1 row)


regreen=> select tpe.*, prj.project_name, prj.country_name, usr.first_name, usr.last_name from respi_tree_planting_entry tpe inner join respi_projects prj on prj.id=tpe.project_id  inner join respi_regreeningusers usr on usr.id=tpe.collector_id where tpe.recorded_dte::text like '2025-05-08%' and usr.first_name='Jackson';
  id  |         recorded_dte          | date_collected | collector_id | plot_id | project_id | project_name | country_name | first_name | last_name 
------+-------------------------------+----------------+--------------+---------+------------+--------------+--------------+------------+-----------
 6548 | 2025-05-08 21:19:43.324251+03 | 2025-05-08     |         3708 |   12747 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6550 | 2025-05-08 21:20:11.616127+03 | 2025-05-08     |         3708 |   12749 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6551 | 2025-05-08 21:20:23.678467+03 | 2025-05-08     |         3708 |   12750 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6552 | 2025-05-08 21:20:35.400684+03 | 2025-05-08     |         3708 |   12751 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6554 | 2025-05-08 21:21:39.801166+03 | 2025-05-08     |         3708 |   12753 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6556 | 2025-05-08 21:21:50.787785+03 | 2025-05-08     |         3708 |   12755 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
 6558 | 2025-05-08 21:22:04.837314+03 | 2025-05-08     |         3708 |   12757 |         12 | UKPact_NbS   | Kenya        | Jackson    | Ankrah
(7 rows)

```

## solution
- update the project ids from UKPact_Nbs to NbS_Guinean_Forests??


```sql
-- for Mohamed Fanta TOUNKARA
update respi_tree_planting_entry set project_id = 115 where id=6109;
-- for Jackson Ankrah
update respi_tree_planting_entry set project_id = 115 where id = 6548;
update respi_tree_planting_entry set project_id = 115 where id = 6550;
update respi_tree_planting_entry set project_id = 115 where id = 6551;
update respi_tree_planting_entry set project_id = 115 where id = 6552;
update respi_tree_planting_entry set project_id = 115 where id = 6554;
update respi_tree_planting_entry set project_id = 115 where id = 6556;
update respi_tree_planting_entry set project_id = 115 where id = 6558;
```

