# problem

3 records, user says they did not upload. 
- failed upload for plot name `26b98006-7917-4a6e-90b0-e69baa120c34`
- success upload for `ace0a876-94ae-48d0-a7f7-c979a7008747`  - to check record completeness
- suceess upload for `de8a8d08-7f28-46f7-a8d4-6355fb43ad7f`  - to check record completeness



## plot 2: `ace0a876-94ae-48d0-a7f7-c979a7008747` findings

### conflicting entries
|   entry       |   db side                  |   record side                |
|:-------------:|:--------------------------:|:----------------------------:|
| county name   | 55: `Eastern Province`     |  368: `Iburasirazuba`        | 
| 


### record completeness check

```sql
select 
    plt.*, scty.*, cty.*, ctry.*,  prj.*, farmer.*, ent.*, ch.*, tpmgt.*, trus.*, tparea.*, tpmst.*
	--plps.*
	
	-- scty.subcounty_name, scty.county_id, 
	-- farmer.first_name, farmer.last_name, farmer.organization, 
	-- ent.collector_id, usr.first_name, usr.username, ent.project_id, prj.project_name, 
	-- ch.scientific_name, ch.local_name, ch.date_planted, ch.trees_planted, ch.trees_survived

from 
    respi_plots plt 
inner join respi_subcounties scty on scty.id=plt.subcounty_id 
inner join respi_counties cty on cty.id=scty.county_id
inner join respi_countries ctry on ctry.id=cty.country_id
inner join respi_tree_planting_entry ent on ent.plot_id=plt.id 
inner join respi_regreeningusers usr on usr.id=ent.collector_id
inner join respi_farming_entity farmer on farmer.id=plt.farming_entity_id 
inner join respi_projects prj on prj.id=ent.project_id
inner join respi_cohort ch on ch.tp_entry_id=ent.id
inner join respi_tp_management_practices tpmgt on tpmgt.cohort_id = ch.id
inner join respi_tp_tree_usage trus on trus.cohort_id = ch.id
inner join respi_tp_plantingarea_type tparea on tparea.cohort_id = ch.id
inner join respi_tree_measurement tpmst on tpmst.cohort_id = ch.id

--inner join respi_plot_points plps on plps.plot_id=plt.id
where name='ace0a876-94ae-48d0-a7f7-c979a7008747';
```

## judgment

record comlete

# solution
- api post request

