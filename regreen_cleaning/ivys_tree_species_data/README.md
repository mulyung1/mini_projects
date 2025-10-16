# get all tree species data from all 4 modules


- scientific name
- local name
- lat, lon

## tp
cohort has scientific and local names

```sql
regreen=> select ch.id as cohort_id, ch.scientific_name, ch.local_name, trm.latitude, trm.longitude, trm.altitude from respi_cohort ch join respi_tree_measurement trm on trm.cohort_id=ch.id;
 cohort_id |                scientific_name                 |            local_name            |  latitude  |  longitude  | altitude 
-----------+------------------------------------------------+----------------------------------+------------+-------------+----------
       108 | calodendrum                                    | calidendrum                      |  -1.235546 |   36.819032 | 1686.400
       108 | calodendrum                                    | calidendrum                      |  -1.271342 |   36.782093 |    0.000
       112 | Acacia abyssinica                              | test                             |  -1.271342 |   36.782093 |    0.000
       113 | Croton megalocarpus                            | Croton                           |  -1.235611 |   36.818748 | 1683.500
       116 | Croton megalocarpus                            | croton                           |  -1.235990 |   36.819014 | 1686.300
       116 | Croton megalocarpus                            | croton                           |  -1.235927 |   36.818921 | 1686.300
       119 | Unknown                                        | tree1                            |  -1.271342 |   36.782093 |    0.000
       119 | Unknown                                        | tree1                            |  -1.271342 |   36.782093 |    0.000
       124 | Acacia abyssinica                              | tree1                            |  -1.271342 |   36.782093 |    0.000
       126 | Croton megalocarpus                            | Croton                           |  -1.271342 |   36.782093 |    0.000
       129 | Croton megalocarpus                            | croton                           |  -1.225393 |   36.828636 |  798.500
       132 | Pinus patula                                   | pine                             |   9.015076 |   38.813982 | 2360.800
       135 | Unknown                                        | warbugia                         |  -1.235488 |   36.819077 | 1684.500
       138 | Acacia abyssinica                              | test                             |  -1.235503 |   36.819320 | 1683.800
       139 | Acacia ancistroclada                           | test                             |  -1.235484 |   36.819118 | 1683.800
       142 | Acacia ankokib                                 | trees                            |  -1.235856 |   36.818907 | 1683.800
       146 | Unknown                                        | warbugia                         |  -1.235488 |   36.819077 | 1684.500
       149 | Acacia abyssinica                              | test                             |  -1.271342 |   36.782093 |    0.000
       155 | Acacia abyssinica                              | bhh                              |  -1.271342 |   36.782093 |    0.000
       156 | Acacia ancistroclada                           | hyh                              |  -1.271342 |   36.782093 |    0.000
       162 |                                                | mti                              |  -1.271342 |   36.782093 |    0.000
       110 | Euphorbia kamerunica                           | Mgome                            |  37.422114 | -122.082661 |    0.000
       114 | Mangifera indica                               | Mango                            |  -1.235676 |   36.818688 | 1686.400
       121 | Unknown                                        | trees                            |  -1.271342 |   36.782093 |    0.000
       125 | Acacia abyssinica                              | tree 2                           |  -1.271342 |   36.782093 |    0.000
:
```

## 2. fmnr

fmnr_species has scientific and local names

```sql
regreen=> select sp.id as species_id, sp.scientific_name, sp.local_name, trm.latitude, trm.longitude, trm.altitude from respi_fmnr_species sp join respi_tree_measurement trm on trm.fmnr_species_id=sp.id;
 species_id |                       scientific_name                       |        local_name        |  latitude  | longitude  | altitude 
------------+-------------------------------------------------------------+--------------------------+------------+------------+----------
         32 | Croton megalocarpus                                         | croton                   |  -1.271342 |  36.782093 |    0.000
         33 | Croton megalocarpus                                         | croton                   |  -1.271342 |  36.782093 |    0.000
         40 | Ficus barteri                                               | Java fig                 |  -1.235499 |  36.818746 | 1680.500
         41 | Ficus barteri                                               | Java fig                 |  -1.235499 |  36.818746 | 1680.500
         42 | Ficus barteri                                               | Java fig                 |  -1.235499 |  36.818746 | 1680.500
         51 | Pterocarpus tessmannii                                      | nooooow                  |  -1.271342 |  36.782093 |    0.000
         52 | Terminalia brownii                                          | nooooooiw 222222         |  -1.271342 |  36.782093 |    0.000
         54 | Pterocarpus tessmannii                                      | 1                        |  -1.271342 |  36.782093 |    0.000
         55 | Dorstenia tenera                                            | 2                        |  -1.271342 |  36.782093 |    0.000
         56 | Warburgia ugandensis                                        | warbugia                 |  -1.235459 |  36.819128 | 1684.800
         57 | Cunonia capensis                                            | calodendrum              |  -1.235512 |  36.818980 | 1686.300
         58 | Warburgia ugandensis                                        | warbugia                 |  -1.235459 |  36.819128 | 1684.800
         59 | Cunonia capensis                                            | calodendrum              |  -1.235512 |  36.818980 | 1686.300
         60 | Croton megalocarpus                                         | June 30                  |  -1.235645 |  36.818805 | 1686.300
         61 | Mangifera indica                                            | June 30 2                |  -1.235650 |  36.818706 | 1686.300
         62 | Unknown                                                     | land unit                |  -1.271342 |  36.782093 |    0.000
         63 | Warburgia ugandensis                                        | warbugia                 |  -1.235459 |  36.819128 | 1684.800
         64 | Cunonia capensis                                            | calodendrum              |  -1.235512 |  36.818980 | 1686.300
         65 | Croton megalocarpus                                         | Croton                   |  -1.235402 |  36.818848 | 1685.700
         66 | Mangifera indica                                            | Mango                    |  -1.235451 |  36.818859 | 1685.700
         67 | Warburgia ugandensis                                        | warbugia                 |  -1.235459 |  36.819128 | 1684.800
         68 | Cunonia capensis                                            | calodendrum              |  -1.235512 |  36.818980 | 1686.300
         69 | Unknown                                                     | test                     |  -1.271342 |  36.782093 |    0.000
         70 | New name                                                    | test                     |  -1.271342 |  36.782093 |    0.000
         71 | Croton megalocarpus                                         | Croton                   |  -1.235950 |  36.818806 | 1686.200
:

```

## 3. rangeland
- microcatchment trees has scientific and local name
- indivindual microcatchment has lat, lon
```sql
regreen=> select mt.id as microcatchment_id, mt.scientific_name, mt.local_name, im.latitude, im.longitude, im.altitude from respi_microcatchment_trees mt join respi_individual_mirocatchment im on im.id=mt.individual_mirocatchment_id;
 microcatchment_id |            scientific_name             |          local_name           | latitude  | longitude | altitude 
-------------------+----------------------------------------+-------------------------------+-----------+-----------+----------
                 1 | tree                                   | tree                          | -1.271342 | 36.782093 |    0.000
                 2 | tree                                   | tree                          | -1.271342 | 36.782093 |    0.000
                 3 | melia volkensii                        | mukau                         | -1.235734 | 36.818662 | 1685.700
                 4 | melia volkensii                        | mukau                         | -1.235602 | 36.818754 | 1675.979
                 5 | melia volkensii                        | mukau                         | -1.235692 | 36.818886 | 1685.700
                 6 | melia volkensii                        | mukau                         | -1.235706 | 36.818883 | 1685.700
                 7 | melia volkensii                        | mukau                         | -1.235690 | 36.818927 | 1685.700
                 8 | melia volkensii                        | mukau                         | -1.235780 | 36.819110 | 1685.700
                 9 | melia volkensii                        | mukau                         | -1.235698 | 36.819056 | 1685.700
                10 | melia volkensii                        | mukau                         | -1.235706 | 36.819016 | 1685.700
                11 | melia volkensii                        | mukau                         | -1.235711 | 36.818986 | 1685.700
                12 | melia volkensii                        | mukau                         | -1.235705 | 36.819031 | 1685.700
                13 | melia volkensii                        | mukau                        +| -1.235638 | 36.819165 | 1685.700
                   |                                        | mukau                         |           |           | 
                14 | melia volkensii                        | mukau                        +| -1.235636 | 36.819140 | 1685.700
                   |                                        | mukau                         |           |           | 
                15 | melia volkensii                        | mukau                        +| -1.235626 | 36.819093 | 1685.700
                   |                                        | mukau                         |           |           | 
                16 | melia volkensii                        | mukau                        +| -1.235595 | 36.819042 | 1685.700
                   |                                        | mukau                         |           |           | 
                17 | melia volkensii                        | mukau                        +| -1.235623 | 36.818982 | 1685.700
                   |                                        | mukau                         |           |           | 
                18 | melia volkensii                        | mukau                        +| -1.235584 | 36.818980 | 1685.700
                   |                                        | mukau                         |           |           | 
                19 | melia volkensii                        | mukau                        +| -1.235564 | 36.818938 | 1685.700
                   |                                        | mukau                         |           |           | 
                20 | melia volkensii                        | mukau                        +| -1.235586 | 36.818918 | 1685.700
                   |                                        | mukau                         |           |           | 
                21 | melia volkensii                        | mukau                        +| -1.235550 | 36.818894 | 1685.700
                   |                                        | mukau                         |           |           | 
:

```

## 4. nursery
- nurserie_specie has scientific_name, local name


- read queries to df
- concat the dfs
-  drop duplicate rows based on latitude













