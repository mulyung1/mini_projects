import pandas as pd
import json

# Step 1: Load the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_data.csv')

# Step 2: Create a new DataFrame with  the 'country' and 'provinces' columns and tyheir ids
new_df = df[['GID_0_0','NAME_0', 'gadm36_1','NAME_1']].copy()


# Step 3: Convert the new DataFrame into a dictionary
country_dict = {}

for idx, row in new_df.iterrows():
    country_id=row['GID_0_0']
    country_name = row['NAME_0']
    province_id=row['gadm36_1']
    province_name = row['NAME_1']
    
    if country_name not in country_dict:
        country_dict[country_name] = {
            "id": country_id,
            "country_name": country_name,
            "currency": "",
            "code": "",
            "phoneCode": "",
            "counties": []
        }
    
    country_dict[country_name]["counties"].append({
        "id": province_id,
        "county_name": province_name,
        "subCounties": []
    })

# Convert the dictionary to a list of dictionaries
country_list = list(country_dict.values())

# Step 4: Use json.dumps() to create a JSON from the dictionary
json_output = json.dumps(country_list, indent=2)



if __name__ == '__main__':
    # print(new_df)
    # print(json_output)
    #write jspn to file
    with open('provinces.json', 'w') as file:
        file.write(json_output)
        print('Saved!!')