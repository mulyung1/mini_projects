import pandas as pd
import json

# Step 1: Load the CSV file into a pandas DataFrame
df = pd.read_csv('cleaned_woredas.csv')

# Step 2: Create a new DataFrame with  the 'country' and 'provinces' columns and their ids
new_df = df[['COUNTRY', 'NAME_1']].copy()



# Step 3: Convert the new DataFrame into a dictionary
country_dict = {}
country_id_counter = 1  # Counter for country IDs
county_id_counter = 229  # Dictionary to store county counters for each country

for index, row in new_df.iterrows():
    #country_id=row['GID_0_0']
    country_name = row['COUNTRY']
    #province_id=row['gadm36_1']
    province_name = row['NAME_1']
    
    if country_name not in country_dict:
        country_dict[country_name] = {
            "id": country_id_counter,
            "country_name": country_name,
            "currency": "",
            "code": "",
            "phoneCode": "",
            "counties": []
        }
        country_id_counter += 1  
            
        
    country_dict[country_name]["counties"].append({
    "id": county_id_counter,  # Use the county counter for this country,
    "county_name": province_name,
    "subCounties": []
    })

    # Increment the county ID for this country
    county_id_counter += 1


# Convert the dictionary to a list of dictionaries
country_list = list(country_dict.values())

# Step 4: Use json.dumps() to create a JSON from the dictionary
json_output = json.dumps(country_list, indent=2)



if __name__ == '__main__':
    # print(new_df)
    # print(json_output)
    #write jspn to file
    with open('provinces_faulty.json', 'w') as file:
        file.write(json_output)
        print('Saved!!')