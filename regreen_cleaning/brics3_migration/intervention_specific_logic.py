import pandas as pd
from datetime import datetime
from shapely import wkt
from icecream import ic
import re


#dictionary to map odk values to RA app schema values
mapping_dict = {
    "STICKS_BRANCH":"STICKS_PROTECTION",
    "DEBRIS_REMOVAL":"DEBRIS_REMOVAL",
    "INVASIVE_SPECIES":"INVASIVE_CONTROL",
    "WEEDING":"WEEDING",
    "WATERING":"WATERING",
    "PLANTING_SEEDLING":"PLANTING_ANNUAL_PERENNIAL_CROPS"
}

def extract_contours_details(c, contours_df, idx):
    """
    Extract all contours intervention details from parent and child records.
    Returns list of contours econtrol objects.
    where c is the parent(plot) record
    """

    contours_econtrol = []
    contours_no_children = []


    j = 0
    #for idx, c in enumerate(records):
    j += 1
    all_grasses = []
    all_trees = []
    contours_child_list = []

    """-----------------------------------contours DETAILS-------------------------------------"""
    total_num_grasses_planted = 0
    total_kg_grass_seeds = 0.0
    total_num_tree_species = 0
    total_num_trees_planted = 0
    total_num_trees_survived = 0
    grass_present = []
    trees_present = []
    mngmts = []
    tree_status_list = []


    parent_base_contours_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "Contours",
        "established_date": datetime.strptime(str(c['contour-contour_details-date']), "%d/%m/%Y").strftime("%Y-%m") if str(c["contour-contour_details-date"]) != 'nan' else None,
        "material_used": [
            "OTHER"
        ],
        "other_material_used": "MIGRATED_NOT_KNOWN",
        "who_established": ["MALE", "FEMALE"] if c["contour-contour_details-manages"] == 'both' else ["MALE"] if c["contour-contour_details-manages"]=="male" else [],
        "other_who_established": "YOUTH" if c["contour-contour_details-youth_manages"] == 'yes' else "",
        "total_interventions": 0 if pd.isna(c["contour-contour_details-total"]) else c["contour-contour_details-total"],
        "length": 0 if pd.isna(c["contour-contour_details-length"]) else c["contour-contour_details-length"],
        "width": 0 if pd.isna(c["contour-contour_details-width"]) else c["contour-contour_details-width"],
        "depth": 0 if pd.isna(c["contour-contour_details-depth"]) else c["contour-contour_details-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": "" if pd.isna(c["contour-contour_details-paid_unpaid_labor"]) else c["contour-contour_details-paid_unpaid_labor"],
        # "has_grass": any(grass_present),
        # "total_number_grasses_planted": total_num_grasses_planted,
        # "kg_grass_seeds_planted": total_kg_grass_seeds,
        # "has_trees": any(trees_present),
        # "total_number_different_trees_planted": total_num_tree_species,
        # "total_number_trees_planted": total_num_trees_planted,
        # "total_number_trees_survived": total_num_trees_survived,
        # "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
        # "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2,
    #     "currentStatus": currentStatus,
        "grassEstablishment": all_grasses,
    #     "treeEstablishment":establishment_trees   
    }


    #if c['KEY'] == "uuid:1975a725-83a5-4bdd-8305-35ac65b2cce9":
    """-----------------------------------contours CHILD DETAILS-------------------------------------"""

    #for every record, get the matching child rows
    matching_child_rows = contours_df[contours_df['PARENT_KEY'] == c['KEY']]
    #matching_child_rows = cleaned_df[cleaned_df['PARENT_KEY'] == "uuid:91755b0a-6073-4d6d-88a8-55eaa382d3e6"]
    

    """-------------------------non-child details records extraction-------------------------"""
    #for rows with no child rows, create a default current status, add base parent details
    if matching_child_rows.empty:
        ic('no child rows for', c['KEY'])
        centroid = wkt.loads(c["geometry"]).centroid
        currentStatus = {
            "id": j,
            "key": c["KEY"],
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [],
            "other_erosion_type": "",
            "is_intervention_effective": False,
            "longitude": centroid.x,
            "latitude": centroid.y,
            "altitude": 0,
            "accuracy": 0,
            "photo_url": "test.jpg",
            "comments": f"state {c['geography-state_name']} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus": [],
            "treeCurrentStatus": []
        }
        contour_details = {
            **parent_base_contours_details,
            "has_grass":True if total_num_grasses_planted > 0 else False,
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees":True if total_num_trees_planted > 0 else False,
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "grassEstablishment": [],
            "treeEstablishment": []
        }

        # contours_no_children.append(contour_details)
        # #exit the child loop
        # continue
        contours_no_children.append(contour_details)

        return [
            {
                "econtrol": [contour_details],
                "key": c["KEY"]
            }
        ]



    k =0
    for x in matching_child_rows.to_dict(orient='records'):
        k += 1
        total_num_grasses_planted = 0 if pd.isna(x["grass_contour-num_grass_species"]) else x["grass_contour-num_grass_species"]
        total_kg_grass_seeds = 0 if pd.isna(x["grass_contour-kg_grass_seeds"]) else x["grass_contour-kg_grass_seeds"]
        total_num_tree_species = 0 if pd.isna(x["tree_contour-num_tree_species"]) else x["tree_contour-num_tree_species"]
        total_num_trees_planted = 0 if pd.isna(x["tree_contour-num_trees_planted"]) else x["tree_contour-num_trees_planted"]
        total_num_trees_survived = 0 if pd.isna(x["tree_contour-num_tree_survived"]) else x["tree_contour-num_tree_survived"]
        
        grass_present.append(True if str(x["tree_contour-planted_choice5"]).strip() in ["both", "grasses"] else False)
        trees_present.append(True if str(x["tree_contour-planted_choice5"]).strip() in ["both", "trees"] else False)
        mngmts.extend(str(x["managements_contour-management_practices"]).upper().split()) if not pd.isna(x["managements_contour-management_practices"]) else 'NAN'


        if pd.notna(x['gps-Longitude']):
            child_coords = {
                "longitude": x["gps-Longitude"],
                "latitude" : x['gps-Latitude'],
                "altitude" : x["gps-Altitude"],
                "accuracy" : x["gps-Accuracy"],
                "photo_url": x["photo"],
                "comments" : f"agric_field_state {x["managements_contour-agricultural_field_state"] if pd.notna(x["managements_contour-agricultural_field_state"]) else "MIGRATED_NOT_KNOWN"}"
            }


        """--------------TREE ESTABLISHMENT-------------"""
        
        if x['tree_contour-planted_choice5'] in ["both", "trees"]:
            trees_species_list = x["tree_contour-contour_trees_species"].split()
            j = 0 
            for idx3, raw in enumerate(trees_species_list):
                #ic("original",raw)
                #default
                scientific_name = ""
                local_name = ""
                
                #case1: check or other in the tree species list
                if raw == 'other':
                    #ic("other",raw)
                    other_val = str(x["tree_contour-other_contour_trees"]).strip()
                    #ic("other_val", other_val)

                    #split by comma & 'and'
                    names = re.split(r",| and ", other_val, flags=re.IGNORECASE)
                    #ic(names)
                    for idxx, val in enumerate(names):
                        local_name = val.strip()
                        #handle nan cases
                        if local_name != 'nan' and local_name != "":
                            tree_current_status = {
                                "id": idxx + 1,
                                "local_name": local_name.capitalize(),
                                "scientific_name": scientific_name,
                                "econtrol_status_id": 1
                            }
                            tree_status_list.append(tree_current_status)

                #case 2: scientific + local name extraction
                if "(" in raw and ")" in raw:
                    #scientific name cleaning
                    parts = raw.split("(")[0].strip().replace("_", " ").split()
                    #ic(parts)
                    if len(parts) >= 2:
                        scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                        #ic(scientific_name)

                    #local name cleaning
                    paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ").split()
                    #ic(paarts)
                    if len(paarts) >= 2:
                        local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                        #ic(local_name)
                    else:
                        local_name = paarts[0].capitalize()
                        #ic(local_name)


        all_trees.extend(tree_status_list)
        #ic(all_trees)

        
        """---------------GRASS_ESTABLISHMENT------------"""
        #no grasses 

        comms = f" state {c['geography-state_name'].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']}"

        """--------------------CURRENT STATUS--------------------"""
        currentStatus= {
            "id": k,
            "key":c["KEY"],            
            "herbaceous_cover": "Absent",
            "visible_erosion": True,
            "erosion_type": [
                "OTHER"
            ],
            "other_erosion_type": "NONE",
            "is_intervention_effective": True,
            "longitude": child_coords["longitude"] if child_coords else wkt.loads(c["geometry"]).centroid.x,
            "latitude": child_coords["latitude"]  if child_coords else wkt.loads(c["geometry"]).centroid.y,
            "altitude": child_coords["altitude"]  if child_coords else 0,
            "accuracy": child_coords["accuracy"]  if child_coords else 0,
            "photo_url": child_coords["photo_url"] if child_coords else 'test.jpg',
            "comments": child_coords["comments"] + comms if child_coords else comms,        
            "econtrolId": 1,
            "grassCurrentStatus":all_grasses,
            "treeCurrentStatus":tree_status_list
        }

        #edit establishment dictionary
        establishment_trees = []
        for i in enumerate(all_trees):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_trees.append(data)
        

        
        bunds_child_details = {
            **parent_base_contours_details,
            "has_grass":True if total_num_grasses_planted > 0 else False,
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees":True if total_num_trees_planted > 0 else False,
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "treeEstablishment": establishment_trees
        }
    

        contours_child_list.append(bunds_child_details)
    k = 0
    if contours_child_list:
        ic(f"For {c["KEY"]}, number of contour records = {len(contours_child_list)}")
        #add all child records
        contours_econtrol.append(
            {
                "econtrol": contours_child_list,
                "key": c['KEY']
            }
        )

    contours_econtrol.extend([{"econtrol": [i], "key" :i["key"]} for i in contours_no_children])
            
    return contours_econtrol


def extract_halfmoon_details(c, halfmoon_df, idx):
    microcatchment_list = []
    #for idx, c in enumerate(records):

    """---------------------------------------MICROCATCHMENT DETAILS---------------------------"""
  
    mcm_details = {
        'key':c['KEY'],
        "id": idx + 1,
        "microcatchment_type": "Halfmoons",
        "total_microcatchments": c['halfmoons-halfmoon_details-total_halfmoons'],
        "length": c['halfmoons-halfmoon_details-length_decimal'],
        "width": c['halfmoons-halfmoon_details-width_decimal'],
        "depth": c['halfmoons-halfmoon_details-depth_decimal'],
        "vertical_spacing": c['halfmoons-halfmoon_details_2-vertical_space'],
        "horizontal_spacing": c['halfmoons-halfmoon_details_2-horizontal_space'],
        "established_date": datetime.strptime(str(c['halfmoons-halfmoon_details-date']), "%d/%m/%Y").strftime("%Y-%m") if str(c["halfmoons-halfmoon_details-date"]) != 'nan' else None,
        #"reseeded": True if ,
        #"quantity_seeds_sown": 2.0,
        #"sow_unit": "KG",
        "seed_sources": ["Not_known"],
        "local_seed_bank_name": "",
        "other_seed_sources": "",
        "who_manages_microcatchment": ["MALE","FEMALE"] if c['halfmoons-halfmoon_details_2-manages'] == 'both' else ['MALE'],
        "other_who_manages": "",
        "management_practices": [
            "PLANTING_ANNUAL_PERENNIAL_CROPS"
        ],
        "other_managements": "",
        "usages": [],
        "other_usages": "",
        "rangeland_entry_id": 7,
        "completed": True,
    }
    
    if c['halfmoons-halfmoon_details_2-youth_manages'] == 'yes':
        mcm_details['who_manages_microcatchment'].append('YOUTH')

    '''--------------------------------------MANAGEMENT_PRACTICES--------------------------------'''
    #get only child rows for this record("KEY")    
    matching_mgmt_child_rows = halfmoon_df[halfmoon_df['PARENT_KEY'] == c['KEY']]
    ##check for matches
    # children = matching_mgmt_child_rows['PARENT_KEY'].tolist()
    # print(f"parent: ",c['KEY'], "child", len(children), children)

    practices = []
    child_records = matching_mgmt_child_rows.to_dict(orient='records')

    for  y in child_records:
        if y['additional_management'] == 'yes':
            vals = str(y['management_practices']).split(' ')
            practices.extend(vals)

    # make list a set - this removes duplicates/
    # the management practices in odk are halfmoon based,
    # in regreen app schema, they are microcatchment based
    # therefore we will be using unique management values only/
    set_practices = set(practices)
    #make all characters upper case(RA app schema requirement)
    ls_practices = [a.upper() for a in list(set_practices)]
    

    #map the odk values to accepted ra values
    normalised_practices = [v for k,v in mapping_dict.items() if k in ls_practices]
    mcm_details['management_practices'] = normalised_practices
    
    other_mngmts = []
    #for values not in ra, append them to other managements
    for x in ls_practices:

        if x not in mapping_dict.keys():
            other_mngmts.append(x)
    other_management = ', '.join(other_mngmts)

    mcm_details['other_managements'] = other_management

    """----------------------------------------seeded??----------------------------------------------"""

    # initialize aggregated values
    total_seeds = 0.0
    any_reseeded = False

    for k in child_records:

        # update global reseeded flag if this row is reseeded
        if  k['halfmoon_trees-planted_choice1'] in ['both', 'grasses']:
            any_reseeded = True

        # add seed quantity if numeric
        qty = k['halfmoon_grasses-kg_grass_seeds']
        if isinstance(qty, (int, float)) and not pd.isna(qty):
            total_seeds += qty

    # final aggregated dictionary
    seed_info = {
        "reseeded": any_reseeded,
        "quantity_seeds_sown": total_seeds if total_seeds > 0 else 0,
        "sow_unit": "KG" if any_reseeded else ""
    }

    #print(seed_info)

    # attach to mcm_details
    mcm_details.update(seed_info)




    #     seeded.extend(reseeded)

    """----------------------------------------CURRENT_STATUS-----------------------------------------"""

    cureent_status_list = []
    count = 0
    all_grasses = []
    all_trees = []

    for i, j in enumerate(child_records):
        #mapping dictionary for herbacious cover
        hb_cover_mapping = {
            1: "LESS_FOUR",
            2: "FOUR_FIFTEEN",
            3: "FIFTEEN_FOURTY",
            4: "FOURTY_SIXTFIVE",
            5: "SIXTHFIVE_ABOVE"
        }

        current_status = {
            'key':j['KEY'],
            "id": i + 1,
            "percentage_herbaceous_cover_in": hb_cover_mapping[j['herbaceous_cover']],
            "percentage_herbaceous_cover_between": hb_cover_mapping[j['herbaceous_cover_between']],
            "intact": True if j['halfmoon_intact'] == 'yes' else False,
            "protected": False,
            "protection_type": [],
            "other_protection_type": "",
            "visible_erosion": True if j['visible_erosion'] == 'yes' else False,
            "erosion_type_inside": [],
            "other_erosion_type_inside": "",
            "erosion_type_outside": [],
            "other_erosion_type_outside": "",
            "longitude": j['gps-Longitude'],
            "latitude": j['gps-Latitude'],
            "altitude": j['gps-Altitude'],
            "accuracy": j['gps-Accuracy'], 
            "photo_url": j['photo'],
            "comments": f"labor {c['halfmoons-halfmoon_details_2-paid_unpaid_labor']} state {c['geography-state_name'].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']} type {c['halfmoons-halfmoon_details_2-type_halfmoons']}",
            "microcatchment_id": 7,
            "grassCurrentStatus": []
        }

        comments_parts = []
        """----------------------------grass establishment---------------------------------------"""
        #initiate a list for grasses in one halfmoon
        grass_status_list = []

        if j['halfmoon_trees-planted_choice1'] in  ['grasses', 'both']:
            comments_parts.append(f"grassSpecies {j['halfmoon_grasses-num_grass_species']}")

            grass_species_list = str(j['halfmoon_grasses-halfmoon_grass_species']).split()
            #default
            scientific_name = ""
            local_name = ""

            for idx2 ,raw in enumerate(grass_species_list):
                #case 1: others
                if raw.strip() == 'other':
                    other_raw = str(j['halfmoon_grasses-other_halfmoon_grass'])

                    #split by comma & 'and'
                    names = re.split(r",| and ", other_raw, flags=re.IGNORECASE)

                    #loop through local names
                    for idx, name in enumerate(names):
                        cleaned = name.strip()
                        if cleaned != 'nan':
                            grass_current_status_1 = ({
                                "id": idx + 1,
                                "local_name": cleaned,
                                "scientific_name": "",
                                "microcatchment_status_id": 5
                            })
                            grass_status_list.append(grass_current_status_1)

                    continue
                
                #case2: ends with other and also has nan in other colun
                elif raw.strip().endswith('other'):
                    #use the 'other' column
                    local_name = str(j['halfmoon_grasses-other_halfmoon_grass']).strip()
                #case 3: split local name from scientific name
                else:
                    #split scientific and local names
                    if "(" in raw and ")" in raw:
                        #scientific name cleaning
                        parts = raw.split("(")[0].strip().replace("_", " ").split()
                        if len(parts) == 2:
                            scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                        else:
                            scientific_name = raw.split("(")[0].strip().replace("_", " ")

                        #local name cleaning
                        paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").split()
                        if len(paarts) == 2:
                            local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                        else:
                            local_name = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ")#[1].lower()
                    else:
                        scientific_name = raw.strip()

                if local_name != 'nan':
                    grass_current_status = {
                        "id": idx2 + 1,
                        "local_name": local_name,
                        "scientific_name": scientific_name,
                        "microcatchment_status_id": 5
                    }
            
                #append the current status for ths record to the empty list
                grass_status_list.append(grass_current_status)
        #add every status to the to serve as establishment        
        all_grasses.extend(grass_status_list)

        #set the grass establishments to current status
        current_status['grassCurrentStatus'] = grass_status_list
        #print(f"parent:{j['PARENT_KEY']}, child:{j['KEY']}")


        """---------------------------------tree establishment--------------------------------------"""
        tree_status_list = []
        if j['halfmoon_trees-planted_choice1'] in  ['trees', 'both']:
            comments_parts.append(f"treeSpecies {j['halfmoon_trees-num_tree_species']}")
            comments_parts.append(f"plantedTrees {j['halfmoon_trees-num_trees_planted']}")
            comments_parts.append(f"survivedTrees {j['halfmoon_trees-num_tree_survived']}")

            trees_species_list = j['halfmoon_trees-halfmoon_trees_species'].split()
            #ic(c['KEY'])
            #ic(trees_species_list)
            
            for idx3, raw in enumerate(trees_species_list):

                #default
                scientific_name = ""
                local_name = ""
                 
                #case1: check or other in the tree species list
                if raw == 'other':
                    other_val = str(j['halfmoon_trees-other_halfmoon_trees']).strip()

                    #split by comma & 'and'
                    names = re.split(r",| and ", other_val, flags=re.IGNORECASE)

                    for idxx, val in enumerate(names):
                        local_name = val.strip()
                        #handle nan cases
                        if local_name != 'nan' and local_name != "":
                            tree_current_status = {
                                "id": idxx + 1,
                                "local_name": local_name.capitalize(),
                                "scientific_name": scientific_name,
                                "microcatchment_status_id": 8
                            }
                            #ic(tree_current_status)
                            tree_status_list.append(tree_current_status)
                        

                #case 2: scientific + local name extraction
                if "(" in raw and ")" in raw:
                    #scientific name cleaning
                    parts = raw.split("(")[0].strip().replace("_", " ").split()
                    
                    if len(parts) >= 2:
                        scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                        #ic(scientific_name)

                    #local name cleaning
                    paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ").split()
                    #ic(paarts)
                    if len(paarts) >= 2:
                        local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                        #ic(local_name)
                    else:
                        local_name = paarts[0].capitalize()
                        #ic(local_name)

                #case2: handle other trees 
                #elif raw.endswith('other') or 'other' in raw:
                    #ic(raw)

                tree_current_status = {
                    "id": idx3 + 1,
                    "local_name": local_name,
                    "scientific_name": scientific_name,
                    "microcatchment_status_id": 8
                }
                #ic(tree_current_status)
                tree_status_list.append(tree_current_status)
        
        #buld final comment string
        final_coment = " ".join(comments_parts)
        current_status["comments"] = current_status["comments"] + " " + final_coment

        # add every tree status to establishment list
        all_trees.extend(tree_status_list)
        #ic(all_trees)
        #append tree status list to key in status dictionary
        current_status['treeCurrentStatus'] = tree_status_list
        
        #a list of all current status fields from tree to grasses
        cureent_status_list.append(current_status)
            
    
    #x = [print(dict(i[1])) for i in enumerate(all_grasses)]

        ## update establishment grasses and trees with microcatchment_id key
    establishment_grasses = []
    for i in enumerate(all_grasses):
        data = dict(i[1])
        data['microcatchment_id'] = data.pop('microcatchment_status_id')
        establishment_grasses.append(data)
    

    establishment_trees = []
    for i in enumerate(all_trees):
        data = dict(i[1])
        data['microcatchment_id'] = data.pop('microcatchment_status_id')
        establishment_trees.append(data)
    

    mcm_details['currentStatus'] = cureent_status_list
    mcm_details['grassEstablishment'] = establishment_grasses
    mcm_details['treeEstablishment'] = establishment_trees



    microcatchment_info = {
        "microcatchment":[mcm_details], 
        'key':j['PARENT_KEY']
    }
    #ic(j['PARENT_KEY'])
    microcatchment_list.append(microcatchment_info)

    return microcatchment_list
    
    
def extract_wp_details(c, idx):
    waterpoint_list = []

    #for idx, c in enumerate(records):

    #if c['KEY'] == "uuid:1975a725-83a5-4bdd-8305-35ac65b2cce9":
    """-----------------------------------WPS CHILD DETAILS-------------------------------------"""
    #no invasve child detail

    """-----------------------------------WPS DETAILS-------------------------------------"""

    wps_details = {
        "key": c["KEY"],
        "id": idx,
        "water_point_type": c["waterpoints-wp_type"].capitalize(),
        "water_usage": [i.capitalize() for i in c["waterpoints-wp_usage"].split()],
        "water_condition": [c["waterpoints-wp_condition"].capitalize()],
        "water_facilities": [i.capitalize() for i in c["waterpoints-wp_facilities"].split()],
        "other_facility": "",
        "average_distance": [c["waterpoints-wp_avg_distance"]],
        "water_point_season": [c["waterpoints-wp_availability"].capitalize()],
        "contamination_sources": [c["waterpoints-wp_contami_sources"].capitalize()],
        "water_point_protection": [i.capitalize() for i in c["waterpoints-wp_protection"].split()],
        "photo_url": c["waterpoints-photo"],
        "longitude": c["waterpoints-gps-Longitude"],
        "latitude": c["waterpoints-gps-Latitude"],
        "altitude": c["waterpoints-gps-Altitude"],
        "accuracy": c["waterpoints-gps-Accuracy"],
        "comments": f"wp_depth {c["waterpoints-wp_depth"]} wp_ownership {c["waterpoints-wp_ownership"]}",
        "rangelandEntryId": 2
    }

    waterpoint_list.append(wps_details)
    

    wps_list = [{ "waterpoint": [i],  "key" :i["key"]} for i in waterpoint_list]
    #ic(wps_list)
    return wps_list


def extract_rockdam_details(c, idx):
    rock_dams_list = []

    #for idx, c in enumerate(records):

    """-----------------------------------rockdams CHILD DETAILS-------------------------------------"""
    #not present
    """-----------------------------------rockdams DETAILS-------------------------------------"""

    rock_dams_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "rock_dams",
        "established_date": datetime.strptime(str(c['rock_dams-date']), "%d/%m/%Y").strftime("%Y-%m") if str(c["rock_dams-date"]) != 'nan' else None,
        "material_used": [
            "Rocks"
        ],
        "other_material_used": "",
        "who_established": ["MALE", "FEMALE"] if c["rock_dams-manages"] == 'both' else ["MALE"] if c["rock_dams-manages"]=="male" else [],
        "other_who_established": "YOUTH" if c["rock_dams-youth_manages"] == 'yes' else "",
        "total_interventions": c["rock_dams-total"],
        "length": c["rock_dams-length"],
        "width": c["rock_dams-width"],
        "depth": c["rock_dams-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": c["rock_dams-paid_unpaid_labor"],        
        "has_grass": False,
        "total_number_grasses_planted": 0,
        "kg_grass_seeds_planted": 0,
        "has_trees": False,
        "total_number_different_trees_planted": 0,
        "total_number_trees_planted": 0,
        "total_number_trees_survived": 0,
        "management_practices":  [],
        "other_managements": " ",
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2,
        "currentStatus": {
            "id": 1,
            "key":c["KEY"],            
            "herbaceous_cover": "Absent",
            "visible_erosion": True,
            "erosion_type": [
                "OTHER"
            ],
            "other_erosion_type": "NONE",
            "is_intervention_effective": True,
            "longitude": c["rock_dams-gps-Longitude"],
            "latitude": c["rock_dams-gps-Latitude"],
            "altitude": c["rock_dams-gps-Altitude"],
            "accuracy": c["rock_dams-gps-Accuracy"],
            "photo_url": c["rock_dams-photo"],
            "comments": f"state {c["geography-state_name"].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus":[],
            "treeCurrentStatus":[]
        },
        "grassEstablishment": [],
        "treeEstablishment":[]  
    }

    rock_dams_list.append(rock_dams_details)
    
    #construct the correct json structure
    rdams_econtrol = [{"econtrol": [i],  "key" :i["key"]} for i in rock_dams_list]
    return rdams_econtrol


def extract_swales_details(c, swales_df, idx):
    swales_no_children =[]
    swales_econtrol = []


    #for idx, c in enumerate(records):
    cureent_status_list = []
    all_grasses = []
    all_trees = []
    swales_child_list = []

    """-----------------------------------SWALES DETAILS-------------------------------------"""

    total_num_grasses_planted = 0
    total_kg_grass_seeds = 0.0
    total_num_tree_species = 0
    total_num_trees_planted = 0
    total_num_trees_survived = 0
    grass_present = []
    trees_present = []
    mngmts = []


    parent_base_swales_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "Swales",
        "established_date": datetime.strptime(str(c['swales-swales_details-date']), "%d/%m/%Y").strftime("%Y-%m") if str(c["swales-swales_details-date"]) != 'nan' else None,
        "material_used": [
            "OTHER"
        ],
        "other_material_used": "MIGRATED_NOT_KNOWN",
        "who_established": ["MALE", "FEMALE"] if c["swales-swales_details-manages"] == 'both' else ["MALE"] if c["swales-swales_details-manages"]=="male" else [],
        "other_who_established": "YOUTH" if c["swales-swales_details-youth_manages"] == 'yes' else "",
        "total_interventions": c["swales-swales_details-total"],
        "length": c["swales-swales_details-length"],
        "width": c["swales-swales_details-width"],
        "depth": c["swales-swales_details-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": c["swales-swales_details-paid_unpaid_labor"],        
        # "has_grass": any(grass_present),
        # "total_number_grasses_planted": total_num_grasses_planted,
        # "kg_grass_seeds_planted": total_kg_grass_seeds,
        # "has_trees": any(trees_present),
        # "total_number_different_trees_planted": total_num_tree_species,
        # "total_number_trees_planted": total_num_trees_planted,
        # "total_number_trees_survived": total_num_trees_survived,
        # "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
        # "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2,
        # "currentStatus": cureent_status_list,
        # "grassEstablishment": all_grasses,
        # "treeEstablishment":all_trees   
    }


    #if c['KEY'] == "uuid:1975a725-83a5-4bdd-8305-35ac65b2cce9":
    """-----------------------------------SWALES CHILD DETAILS-------------------------------------"""

    
    #for every record, get the matching child rows
    matching_child_rows = swales_df[swales_df['PARENT_KEY'] == c['KEY']]
    #matching_child_rows = swales_df[swales_df['PARENT_KEY'] == "uuid:91755b0a-6073-4d6d-88a8-55eaa382d3e6"]
    

    """-------------------------non-child details records extraction-------------------------"""
    #for rows with no child rows, create a default current status, add base parent details
    if matching_child_rows.empty:
        ic('no child rows for', c['KEY'])
        centroid = wkt.loads(c["geometry"]).centroid
        currentStatus = {
            "id": idx + 1,
            "key": c["KEY"],
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [],
            "other_erosion_type": "",
            "is_intervention_effective": False,
            "longitude": centroid.x,
            "latitude": centroid.y,
            "altitude": 0,
            "accuracy": 0,
            "photo_url": "test.jpg",
            "comments": f"state {c['geography-state_name']} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus": [],
            "treeCurrentStatus": []
        }
        
        swales_no_child_details = {
            **parent_base_swales_details,
            "has_grass": any(grass_present),
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees": any(trees_present),
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "grassEstablishment": [],
            "treeEstablishment": []
        }

        swales_no_children.append(swales_no_child_details)
        #exit the child loop
        #continue
        return [
            {
                "econtrol": [swales_no_child_details],
                "key": c["KEY"]
            }
        ]




    idxx =0
    for x in matching_child_rows.to_dict(orient='records'):

        total_num_grasses_planted = 0 if pd.isna(x["grass_swales-num_grass_species"]) else x["grass_swales-num_grass_species"]
        total_kg_grass_seeds = 0 if pd.isna(x["grass_swales-kg_grass_seeds"]) else x["grass_swales-kg_grass_seeds"]
        total_num_tree_species = 0 if pd.isna(x["tree_swales-num_tree_species"]) else x["tree_swales-num_tree_species"]
        total_num_trees_planted = 0 if pd.isna(x["tree_swales-num_trees_planted"]) else x["tree_swales-num_trees_planted"]
        total_num_trees_survived = 0 if pd.isna(x["tree_swales-num_tree_survived"]) else x["tree_swales-num_tree_survived"]
        grass_present.append(True if str(x["tree_swales-planted_choice2"]).strip() in ["both", "grasses"] else False)
        trees_present.append(True if str(x["tree_swales-planted_choice2"]).strip() in ["both", "trees"] else False)
        mngmts.extend(str(x["managements_swales-management_practices"]).upper().split()) if not pd.isna(x["managements_swales-management_practices"]) else 'NAN'


        if pd.notna(x['gps-Longitude']):
            child_coords = {
                "longitude": x["gps-Longitude"],
                "latitude" : x['gps-Latitude'],
                "altitude" : x["gps-Altitude"],
                "accuracy" : x["gps-Accuracy"],
                "photo_url": x["photo"],
                "comments" : f"agric_field_state {x["managements_swales-agricultural_field_state"] if pd.notna(x["managements_swales-agricultural_field_state"]) else "MIGRATED_NOT_KNOWN"}"
            }
        
        """--------------TREE ESTABLISHMENT-------------"""
        tree_status_list = []
        if x['tree_swales-planted_choice2'] in ["both", "trees"]:
            trees_species_list = x["tree_swales-swales_trees_species"].split()
            
            for idx3, raw in enumerate(trees_species_list):
                #ic("original",raw)
                #default
                scientific_name = ""
                local_name = ""
                
                #case1: check or other in the tree species list
                if raw == 'other':
                    #ic("other",raw)
                    other_val = str(x["tree_swales-other_swales_trees"]).strip()
                    #ic("other_val", other_val)

                    #split by comma & 'and'
                    names = re.split(r",| and ", other_val, flags=re.IGNORECASE)
                    #ic(names)
                    for idxx, val in enumerate(names):
                        local_name = val.strip()
                        #handle nan cases
                        if local_name != 'nan' and local_name != "":
                            tree_current_status = {
                                "id": idxx + 1,
                                "local_name": local_name.capitalize(),
                                "scientific_name": scientific_name,
                                "econtrol_status_id": 1
                            }
                            #ic(tree_current_status)
                            tree_status_list.append(tree_current_status)

                #case 2: scientific + local name extraction
                if "(" in raw and ")" in raw:
                    #scientific name cleaning
                    parts = raw.split("(")[0].strip().replace("_", " ").split()
                    #ic(parts)
                    if len(parts) >= 2:
                        scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                        #ic(scientific_name)

                    #local name cleaning
                    paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ").split()
                    #ic(paarts)
                    if len(paarts) >= 2:
                        local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                        #ic(local_name)
                    else:
                        local_name = paarts[0].capitalize()
                        #ic(local_name)

                #case2: handle other trees 
                #elif raw.endswith('other') or 'other' in raw:
                    #ic(raw)

                tree_current_status = {
                    "id": idx3 + 1,
                    "local_name": local_name,
                    "scientific_name": scientific_name,
                    "econtrol_status_id": 1
                }
                #ic(tree_current_status)
                tree_status_list.append(tree_current_status)

        #ic(tree_status_list)
        all_trees.extend(tree_status_list)

        grass_status_list = []
        """---------------GRASS_ESTABLISHMENT------------"""
        #get all grasses 
        if x["tree_swales-planted_choice2"] in ["both", "grasses"]:
            grass_species_list = str(x["grass_swales-swales_grass_species"]).split()
            #default
            scientific_name = ""
            local_name = ""

            for idx2 ,raw in enumerate(grass_species_list):
                #case 1: others
                if raw.strip() == 'other':
                    other_raw = str(x["grass_swales-other_swales_grass"])

                    #split by comma & 'and'
                    names = re.split(r",| and ", other_raw, flags=re.IGNORECASE)

                    #loop through local names
                    for idx, name in enumerate(names):
                        cleaned = name.strip()
                        if cleaned != 'nan':
                            grass_current_status_1 = ({
                                "id": idx + 1,
                                "local_name": cleaned,
                                "scientific_name": "",
                                "econtrol_status_id": 1
                            })
                        grass_status_list.append(grass_current_status_1)

                    continue
                
                #case2: ends with other and also has nan in other colun
                elif raw.strip().endswith('other'):
                    #use the 'other' column
                    local_name = str(j['halfmoon_grasses-other_halfmoon_grass']).strip()
                #case 3: split local name from scientific name
                else:
                    #split scientific and local names
                    if "(" in raw and ")" in raw:
                        #scientific name cleaning
                        parts = raw.split("(")[0].strip().replace("_", " ").split()
                        if len(parts) == 2:
                            scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                        else:
                            scientific_name = raw.split("(")[0].strip().replace("_", " ")

                        #local name cleaning
                        paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").split()
                        if len(paarts) == 2:
                            local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                        else:
                            local_name = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ")#[1].lower()
                    else:
                        scientific_name = raw.strip()

                if local_name != 'nan':
                    grass_current_status = {
                        "id": idx2 + 1,
                        "local_name": local_name,
                        "scientific_name": scientific_name,
                        "econtrol_status_id": 1
                    }
            
                #append the current status for ths record to the empty list
                grass_status_list.append(grass_current_status)
        
        """--------------------CURRENT STATUS--------------------"""
        idxx += 1
        currentStatus= {
            "id": idxx,
            "key":c["KEY"],            
            "herbaceous_cover": "",
            "visible_erosion": True,
            "erosion_type": [
                "OTHER"
            ],
            "other_erosion_type": "NONE",
            "is_intervention_effective": True,
            "longitude": x["gps-Longitude"],
            "latitude": x["gps-Latitude"],
            "altitude": x["gps-Altitude"],
            "accuracy": x["gps-Accuracy"],
            "photo_url": x["photo"],
            "comments": f"agric_field_state {x["managements_swales-agricultural_field_state"] if pd.notna(x["managements_swales-agricultural_field_state"]) else "MIGRATED_NOT_KNOWN"} state {c["geography-state_name"].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus":grass_status_list,
            "treeCurrentStatus":tree_status_list
        }
        
        #add every status to the to serve as establishment        
        all_grasses.extend(grass_status_list)


        ## update establishment grasses and trees with econtrol_id key
        establishment_grasses = []
        for i in enumerate(all_grasses):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_grasses.append(data)
        

        establishment_trees = []
        for i in enumerate(all_trees):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_trees.append(data)
        #ic(establishment_trees)
        
        swales_child_details = {
            **parent_base_swales_details,
            "has_grass": True if total_num_grasses_planted > 0 else False,
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees": True if total_num_trees_planted > 0 else False,
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "grassEstablishment": establishment_grasses,
            "treeEstablishment": establishment_trees
        }
    

        swales_child_list.append(swales_child_details)
    
    if swales_child_list:
        #ic(f"For {c["KEY"]}, number of swales records = {len(swales_child_list)}")
        swales_econtrol.append(
            {
                "econtrol": swales_child_list,
                "key": c['KEY']
            }
        )

    swales_econtrol.extend([{"econtrol": [i],"key" :i["key"] } for i in swales_no_children])
    #ic(swales_econtrol)
    return swales_econtrol


def extract_terraces_details(c, idx):
    terraces_list = []

    #for idx, c in enumerate(records):
    """-----------------------------------Terracing CHILD DETAILS-------------------------------------"""
    #not present
    """-----------------------------------Terracing DETAILS-------------------------------------"""
    centroid = wkt.loads(c["geometry"]).centroid

    terraces_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "Terraces",
        "established_date": datetime.strptime(str(c['terracing-terrace_details-date']), "%d/%m/%Y").strftime("%Y-%m") if str(c["terracing-terrace_details-date"]) != 'nan' else None,
        "material_used": [
            "OTHER"
        ],
        "other_material_used": "MIGRATED_NOT_KNOWN",
        "who_established": ["MALE", "FEMALE"] if c["terracing-terrace_details-manages"] == 'both' else "MALE" if c["terracing-terrace_details-manages"]=="male" else "",
        "other_who_established": "YOUTH" if c["terracing-terrace_details-youth_manages"] == 'yes' else "",
        "total_interventions": c["terracing-terrace_details-total"],
        "length": c["terracing-terrace_details-length"],
        "width": c["terracing-terrace_details-width"],
        "depth": c["terracing-terrace_details-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": c["terracing-terrace_details-paid_unpaid_labor"],        
        "has_grass": False,
        "total_number_grasses_planted": 0,
        "kg_grass_seeds_planted": 0,
        "has_trees": False,
        "total_number_different_trees_planted": 0,
        "total_number_trees_planted": 0,
        "total_number_trees_survived": 0,
        "management_practices":  [],
        "other_managements": " ",
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2,
        "currentStatus": {
            "id": idx + 1,
            "key": c["KEY"],
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [],
            "other_erosion_type": "",
            "is_intervention_effective": False,
            "longitude": centroid.x,
            "latitude": centroid.y,
            "altitude": 0,
            "accuracy": 0,
            "photo_url": "test.jpg",
            "comments": f"state {c['geography-state_name']} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus": [],
            "treeCurrentStatus": []
        },
        "grassEstablishment": [],
        "treeEstablishment":[]  
    }

    terraces_list.append(terraces_details)
    terraces_econtrol = [{ "econtrol": [i], "key" :i["key"]} for i in terraces_list]

    return terraces_econtrol


def extract_iremoval_details(c, idx):
    invasivs_list = []


    #for idx, c in enumerate(records):

    #if c['KEY'] == "uuid:1975a725-83a5-4bdd-8305-35ac65b2cce9":
    """-----------------------------------INVASIVES CHILD DETAILS-------------------------------------"""
    #no invasve child detail

    """-----------------------------------INVASIVES DETAILS-------------------------------------"""

    invasives_details = {
        "key":c["KEY"],
        "id": idx,
        "removal_date": datetime.strptime(c['invasive_removal-removal_date'], "%d/%m/%Y").strftime("%Y-%m"),
        "removal_methods": c["invasive_removal-removal_methods"].split(),
        "other_removal_methods": "",
        "photo_url": "", #no photo column
        "comments": f"Invasive_species NONE, iremoval_severity {c["invasive_removal-severity"].upper()}",
        "rangelandEntryId": 8,
        "grassCurrentStatus": [],
        "treeCurrentStatus": []
    }

    invasivs_list.append(invasives_details)
    

    ic(invasivs_list)
    iremoval_list = [{"iremoval": [i], "key" :i["key"]} for i in invasivs_list]

    return iremoval_list


def extract_gabions_details(c, gabions_df, idx):
    gabions_no_children = []
    gabions_econtrol = []


    #for idx, c in enumerate(records):

    all_grasses = []
    all_trees = []
    gabions_child_list = []


    """-----------------------------------gabions DETAILS-------------------------------------"""
    # collect row gabion details, will be used to create list of gabion detail+current status for each repeating record
    parent_base_gabions_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "Gabions",
        "established_date": datetime.strptime(c['gabions-gabions_details-date'], "%d/%m/%Y").strftime("%Y-%m"),
        "material_used": [
            "Rocks"
        ],
        "other_material_used": "",
        "who_established": ["MALE", "FEMALE"] if c["gabions-gabions_details-manages"] == 'both' else ["MALE"] if c["gabions-gabions_details-manages"]=="male" else [],
        "other_who_established": "YOUTH" if c["gabions-gabions_details-youth_manages"] == 'yes' else "",
        "total_interventions": c["gabions-gabions_details-total"],
        "length": c["gabions-gabions_details-length"],
        "width": c["gabions-gabions_details-width"],
        "depth": c["gabions-gabions_details-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": c["gabions-gabions_details-paid_unpaid_labor"],        
        # "has_grass": any(grass_present),
        # "total_number_grasses_planted": total_num_grasses_planted,
        # "kg_grass_seeds_planted": total_kg_grass_seeds,
        # "has_trees": any(trees_present),
        # "total_number_different_trees_planted": total_num_tree_species,
        # "total_number_trees_planted": total_num_trees_planted,
        # "total_number_trees_survived": total_num_trees_survived,
        # "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
        # "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2
        # "currentStatus": cureent_status_list,
        # "grassEstablishment": all_grasses,
        # "treeEstablishment":all_trees   
    }



    #if c['KEY'] == "uuid:1975a725-83a5-4bdd-8305-35ac65b2cce9":
    """-----------------------------------gabions CHILD DETAILS-------------------------------------"""

    #for every record, get the matching child rows
    matching_child_rows = gabions_df[gabions_df['PARENT_KEY'] == c['KEY']]


    total_num_grasses_planted = 0
    total_kg_grass_seeds = 0.0
    total_num_tree_species = 0
    total_num_trees_planted = 0
    total_num_trees_survived = 0
    grass_present = []
    trees_present = []
    mngmts = []
    
    """-------------------------non-child details records extraction-------------------------"""
    #for rows with no child rows, create a default current status, add base parent details
    if matching_child_rows.empty:
        ic('no child rows for', c['KEY'])
        centroid = wkt.loads(c["geometry"]).centroid
        currentStatus = {
            "id": idx + 1,
            "key": c["KEY"],
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [],
            "other_erosion_type": "",
            "is_intervention_effective": False,
            "longitude": centroid.x,
            "latitude": centroid.y,
            "altitude": 0,
            "accuracy": 0,
            "photo_url": "test.jpg",
            "comments": f"state {c['geography-state_name']} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus": [],
            "treeCurrentStatus": []
        }
        gabions_details = {
            **parent_base_gabions_details,
            "has_grass": True if total_num_grasses_planted > 0 else False,
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees": True if total_num_trees_planted > 0 else False,
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "grassEstablishment": [],
            "treeEstablishment": []
        }

        gabions_no_children.append(gabions_details)
        #exit the child loop
        return [
            {
                "econtrol": [gabions_details],
                "key": c["KEY"]
            }
        ]



    idxx =0
    for x in matching_child_rows.to_dict(orient='records'):

        total_num_grasses_planted = 0 if pd.isna(x["grass_gabions-num_grass_species"]) else x["grass_gabions-num_grass_species"]
        total_kg_grass_seeds = 0 if pd.isna(x["grass_gabions-kg_grass_seeds"]) else x["grass_gabions-kg_grass_seeds"]
        total_num_tree_species = 0 if pd.isna(x["tree_gabion-num_tree_species"]) else x["tree_gabion-num_tree_species"]
        total_num_trees_planted = 0 if pd.isna(x["tree_gabion-num_trees_planted"]) else x["tree_gabion-num_trees_planted"]
        total_num_trees_survived = 0 if pd.isna(x["tree_gabion-num_tree_survived"]) else x["tree_gabion-num_tree_survived"]
        grass_present.append(True if str(x["tree_gabion-planted_choice9"]).strip() in ["both", "grasses"] else False)
        trees_present.append(True if str(x["tree_gabion-planted_choice9"]).strip() in ["both", "trees"] else False)
        mngmts.extend(str(x["managements_gabions-management_practices"]).upper().split()) if not pd.isna(x["managements_gabions-management_practices"]) else 'NAN'

        
        if pd.notna(x['gps-Longitude']):
            child_coords = {
                "longitude": x["gps-Longitude"],
                "latitude" : x['gps-Latitude'],
                "altitude" : x["gps-Altitude"],
                "accuracy" : x["gps-Accuracy"],
                "photo_url": x["photo"],
                "comments" : f"agric_field_state {x["managements_gabions-agricultural_field_state"] if pd.notna(x["managements_gabions-agricultural_field_state"]) else "MIGRATED_NOT_KNOWN"}"
            }
                

        """--------------TREE ESTABLISHMENT-------------"""
        tree_status_list = []
        #no trees
        grass_status_list = []
        """---------------GRASS_ESTABLISHMENT------------"""
        #no grasses
       
        """--------------------CURRENT STATUS--------------------"""
        idxx += 1
        comms = f" state {c['geography-state_name'].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']}"
        currentStatus= {
            "id": idxx,
            "key":c["KEY"],            
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [
            ],
            "other_erosion_type": "NONE",
            "is_intervention_effective": True,
            "longitude": child_coords["longitude"] if child_coords else wkt.loads(c["geometry"]).centroid.x,
            "latitude": child_coords["latitude"]  if child_coords else wkt.loads(c["geometry"]).centroid.y,
            "altitude": child_coords["altitude"]  if child_coords else 0,
            "accuracy": child_coords["accuracy"]  if child_coords else 0,
            "photo_url": child_coords["photo_url"] if child_coords else 'test.jpg',
            "comments": child_coords["comments"] + comms if child_coords else comms,
            "econtrolId": 1,
            "grassCurrentStatus":grass_status_list,
            "treeCurrentStatus":tree_status_list
        }
        
        #add every status to the to serve as establishment        
        all_grasses.extend(grass_status_list)

        ## update establishment grasses and trees with econtrol_id key
        establishment_grasses = []
        for i in enumerate(all_grasses):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_grasses.append(data)
        

        establishment_trees = []
        for i in enumerate(all_trees):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_trees.append(data)
            

        gabions_details = {
            **parent_base_gabions_details,
            "has_grass": True if total_num_grasses_planted > 0 else False,
            "total_number_grasses_planted": total_num_grasses_planted,
            "kg_grass_seeds_planted": total_kg_grass_seeds,
            "has_trees": True if total_num_trees_planted > 0 else False,
            "total_number_different_trees_planted": total_num_tree_species,
            "total_number_trees_planted": total_num_trees_planted,
            "total_number_trees_survived": total_num_trees_survived,
            "management_practices":  [v for k, v in mapping_dict.items() if k in mngmts] + (["OTHER"] if any(k not in mapping_dict.keys() for k in mngmts) else []),
            "other_managements": " ".join([c for c in mngmts if c not in mapping_dict.keys()]),
            "currentStatus": currentStatus,
            "grassEstablishment": establishment_grasses,
            "treeEstablishment": establishment_trees   
        }

        gabions_child_list.append(gabions_details)
    
    if gabions_child_list:
        ic(c["KEY"], len(gabions_child_list))
        gabions_econtrol.append(
            {
                "econtrol": gabions_child_list,
                "key": c['KEY']
            }
        )

    gabions_econtrol.extend([{"econtrol": [i],  "key" :i["key"]} for i in gabions_no_children])
    return gabions_econtrol


def extract_bunds_details(c, bunds_df, idx):
    bunds_no_children = []
    bunds_econtrol = []

    #for idx, c in enumerate(records):
    all_grasses = []
    bunds_child_list = []
    """-----------------------------------BUNDS DETAILS-------------------------------------"""

    total_num_grasses_planted = 0
    total_kg_grass_seeds = 0.0
    grass_present = []
    mngmts = []
    grass_status_list = []

    parent_base_bunds_details = {
        "id": idx + 1,
        "key":c["KEY"],
        "erosion_control_type": "Bunds",
        "established_date": datetime.strptime(str(c['bunds-bunds_details-date']), "%d/%m/%Y").strftime("%Y-%m") if pd.notna(c["bunds-bunds_details-date"]) else '',
        "material_used": [
            "Soil"
        ],
        "other_material_used": "",
        "who_established": ["MALE", "FEMALE"] if c["bunds-bunds_details-manages"] == 'both' else ["MALE"] if c["bunds-bunds_details-manages"]=="male" else [],
        "other_who_established": "YOUTH" if c["bunds-bunds_details-youth_manages"] == 'yes' else "",
        "total_interventions": c["bunds-bunds_details-total"],
        "length": c["bunds-bunds_details-length"],
        "width": c["bunds-bunds_details-width"],
        "depth": c["bunds-bunds_details-depth"],
        "vertical_spacing": 0,
        "horizontal_spacing": 0,
        "labor_payment": c["bunds-bunds_details-paid_unpaid_labor"],        
        "has_grass": any(grass_present),
        "total_number_grasses_planted": total_num_grasses_planted,
        "kg_grass_seeds_planted": total_kg_grass_seeds,
        "has_trees": False,
        "total_number_different_trees_planted": 0,
        "total_number_trees_planted": 0,
        "total_number_trees_survived": 0,
        "management_practices":  [],
        "other_managements": " ",
        "usages":["MIGRATED_NOT_KNOWN"],
        "other_usages": "",
        "rangelandEntryId": 2,
        # "currentStatus": currentStatus,
        # "grassEstablishment": establishment_grasses,
        "treeEstablishment":[]  
    }


    """-----------------------------------BUNDS CHILD DETAILS-------------------------------------"""

    matching_child_rows = bunds_df[bunds_df['PARENT_KEY'] == c['KEY']]


    """-------------------------non-child details records extraction-------------------------"""
    #for rows with no child rows, create a default current status, add base parent details
    if matching_child_rows.empty:
        ic('no child rows for', c['KEY'])
        centroid = wkt.loads(c["geometry"]).centroid
        currentStatus = {
            "id": idx + 1,
            "key": c["KEY"],
            "herbaceous_cover": "ABSENT",
            "visible_erosion": False,
            "erosion_type": [],
            "other_erosion_type": "",
            "is_intervention_effective": False,
            "longitude": centroid.x,
            "latitude": centroid.y,
            "altitude": 0,
            "accuracy": 0,
            "photo_url": "test.jpg",
            "comments": f"state {c['geography-state_name']} community {c['geography-community_name']}",
            "econtrolId": 1,
            "grassCurrentStatus": [],
            "treeCurrentStatus": []
        }
        bunds_details = {
            **parent_base_bunds_details,
            "currentStatus": currentStatus,
            "grassEstablishment": [],
            "treeEstablishment": []
        }

        bunds_no_children.append(bunds_details)
        #exit the child loop
        return [
            {
                "econtrol": [bunds_details],
                "key": c["KEY"]
            }
        ]


    for x in matching_child_rows.to_dict(orient='records'):
        total_num_grasses_planted = 0 if pd.isna(x["grass_bunds-num_grass_species"]) else x["grass_bunds-num_grass_species"]
        total_kg_grass_seeds = 0 if pd.isna(x["grass_bunds-kg_grass_seeds"]) else x["grass_bunds-kg_grass_seeds"]
        grass_present.append(True if str(x["tree_bunds-planted_choice3"]).strip() in ["both", "grasses"] else False)
        
        if pd.notna(x['gps-Longitude']):
            child_coords = {
                "longitude": x["gps-Longitude"],
                "latitude" : x['gps-Latitude'],
                "altitude" : x["gps-Altitude"],
                "accuracy" : x["gps-Accuracy"],
                "photo_url": x["photo"],
                "comments" : f"agric_field_state {x["managements_bunds-agricultural_field_state"] if pd.notna(x["managements_bunds-agricultural_field_state"]) else "MIGRATED_NOT_KNOWN"}"
            }
        
        """---------------TREE ESTABLISHMENT------------"""
        #no tree available.
        
        """---------------GRASS_ESTABLISHMENT------------"""
        #get all grasses 
        if x["tree_bunds-planted_choice3"] in ["both", "grasses"]:
            grass_species_list = str(x["grass_bunds-bunds_grass_species"]).split()
            #default
            scientific_name = ""
            local_name = ""

            for idx2 ,raw in enumerate(grass_species_list):
                #case 1: others: not there

                #case2: ends with other and also has nan in other colun

                #split scientific and local names
                if "(" in raw and ")" in raw:
                    #scientific name cleaning
                    parts = raw.split("(")[0].strip().replace("_", " ").split()
                    if len(parts) == 2:
                        scientific_name = f"{parts[0].capitalize()} {parts[1].lower()}"
                    else:
                        scientific_name = raw.split("(")[0].strip().replace("_", " ")

                    #local name cleaning
                    paarts = raw.split("(")[1].split(")")[0].strip().replace("_", " ").split()
                    if len(paarts) == 2:
                        local_name = f"{paarts[0].capitalize()} {paarts[1].lower()}"
                    else:
                        local_name = raw.split("(")[1].split(")")[0].strip().replace("_", " ").replace(",", " ")#[1].lower()
                else:
                    scientific_name = raw.strip()

                if local_name != 'nan':
                    grass_current_status = {
                        "id": idx2 + 1,
                        "local_name": local_name,
                        "scientific_name": scientific_name,
                        "econtrol_status_id": 1
                    }
            
                #append the current status for ths record to the empty list
                grass_status_list.append(grass_current_status)
            #ic(grass_status_list)
        
        
        #add every status to the to serve as establishment        
        all_grasses.extend(grass_status_list)
        #cureent_status_list.append(currentStatus)
        
        """--------------------CURRENT STATUS--------------------"""

        comms = f" state {c['geography-state_name'].replace("â€¦", "").replace(".", "").replace("..", "")} community {c['geography-community_name']}"
        currentStatus= {
            "id": idx,
            "key":c["KEY"],            
            "herbaceous_cover": "Absent",
            "visible_erosion": True,
            "erosion_type": [
                "OTHER"
            ],
            "other_erosion_type": "NONE",
            "is_intervention_effective": True,
            "longitude": child_coords["longitude"] if child_coords else wkt.loads(c["geometry"]).centroid.x,
            "latitude": child_coords["latitude"]  if child_coords else wkt.loads(c["geometry"]).centroid.y,
            "altitude": child_coords["altitude"]  if child_coords else 0,
            "accuracy": child_coords["accuracy"]  if child_coords else 0,
            "photo_url": child_coords["photo_url"] if child_coords else 'test.jpg',
            "comments": child_coords["comments"] + comms if child_coords else comms,
            "econtrolId": 1,
            "grassCurrentStatus":grass_status_list,
            "treeCurrentStatus":[]
        }
        
        #ic(currentStatus)
        establishment_grasses = []
        for i in enumerate(all_grasses):
            data = dict(i[1])
            data['econtrol_id'] = data.pop('econtrol_status_id')
            establishment_grasses.append(data)
        
        bunds_child_details = {
            **parent_base_bunds_details,
            "currentStatus": currentStatus,
            "grassEstablishment": establishment_grasses,
            "treeEstablishment": []
        }
    

        bunds_child_list.append(bunds_child_details)
    
    if bunds_child_list:
        #ic(f"for {c["KEY"]}, no of child records = {len(bunds_child_list)}")
        bunds_econtrol.append(
            {
                "econtrol": bunds_child_list,  "key": c['KEY']
            }
        )
    
    bunds_econtrol.extend([{"econtrol": [i],  "key" :i["key"]} for i in bunds_no_children])
    return bunds_econtrol

