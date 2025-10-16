# views

### 1. all duplicates view
- all duplicates in `duplicates` view are based on exactly same lat, lon.

visualise the view like
```sql
select * from duplicates;
```

#### view definition `\d+ duplicates`
```sql
CREATE OR REPLACE VIEW duplicates AS
View definition:
SELECT trm.id,
    trm.latitude,
    trm.longitude,
    trm.comment,
    trm.accuracy,
    trm.rcc_cbh,
    trm.cohort_id,
    trm.fmnr_species_id,
    dpls.grouped_species_ids,
    dpls.grouped_cohort_ids
   FROM respi_tree_measurement trm
    JOIN ( SELECT respi_tree_measurement.latitude,
            respi_tree_measurement.longitude,
            array_agg(respi_tree_measurement.fmnr_species_id) AS grouped_species_ids,
            array_agg(respi_tree_measurement.cohort_id) AS grouped_cohort_ids
           FROM respi_tree_measurement
          GROUP BY respi_tree_measurement.latitude, respi_tree_measurement.longitude
        HAVING count(*) > 1) dpls ON trm.latitude = dpls.latitude AND trm.longitude = dpls.longitude
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
### 3. tp_dpls view `\d+ fmnr_duplicates`

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
    - respi_tp_management_practices
    - respi_tree_measurement
    - respi_cohort
    - respi_tree_planting_entry
    - respi_plot_points    
    - respi_plot_polygon   
    - respi_plots 
