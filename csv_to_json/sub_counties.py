import pandas as pd
import json
import os


dir='/home/victor/Documents/projects/mini_projects/csv_to_json/data'

#Initialize an empty list to store individual DataFramesdfs=[]
dfs = []

# Loop through each file in the directory
for file in os.listdir(dir):
    # Check if the file is a CSV file
    if file.endswith('.csv'):
        # Create the full file path
        file_path = os.path.join(dir, file)
        print(f"Reading file: {file}")
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        dfs.append(df)

# Combine all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Display the combined DataFrame
print(combined_df)


sub_county_dict={}
country_id_counter = 1  # Counter for country IDs
county_id_counter = 1000  # Dictionary to store county counters for each country
id_count=4000


for index, row in combined_df.iterrows():
    country_name=row["COUNTRY"]
    county_name=row["NAME_1"]
    sub_county_name=row["NAME_2"]


    # If the country is not in the dictionary, add it
    if country_name not in sub_county_dict:
        sub_county_dict[country_name] = {
            "id": country_id_counter,
            "country_name": country_name,
            "currency": "",
            "code": "",
            "phoneCode": "",
            "counties": []
        }
        country_id_counter += 1

    # Check if the county already exists in the country's counties list
    county_exists = False
    for county in sub_county_dict[country_name]["counties"]:
        if county["county_name"] == county_name:
            county_exists = True
            # Append the sub-county to the existing county's subCounties list
            county["subCounties"].append({
                "id": id_count,
                "subcounty_name": sub_county_name
            })
            id_count += 1
            break

    # If the county does not exist, add it
    if not county_exists:
        sub_county_dict[country_name]["counties"].append({
            "id": county_id_counter,
            "county_name": county_name,
            "subCounties": [{
                "id": id_count,
                "subcounty_name": sub_county_name
            }]
        })
        county_id_counter += 1
        id_count += 1

sub_county_list=list(sub_county_dict.values())


json_output = json.dumps(sub_county_list, indent=2)

"""
SCRAPPING CODE
# Step 1: Load the CSV file into a pandas DataFrame
#
df=pd.read_csv("gadm36_2.csv")

# Step 2: Create a new DataFrame with  the "country" and "provinces" and "sub-counties"columns and tyheir ids
new_df=df[["gid_0_0","name_0","gid_1_1","name_1","gadm36_2","name_2"]].copy()

#step3: extract data for these countries
countries = ["Kenya", "Rwanda", "Somalia", "Ghana", "Côte d"Ivoire", "Ethiopia", "Guinea", "Senegal", "Mali", "Niger"]
filtered_df = new_df[new_df["name_0"].isin(countries)]

file=filtered_df.to_csv()
print("converted to csv")

"""


if __name__ =="__main__":
    with open("sub_county_data2_.json", "w") as outfile:
        outfile.write(json_output)
        print("Saved")
        print(json_output)