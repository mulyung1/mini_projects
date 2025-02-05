import pandas as pd
import json

# Step 1: Load the CSV file into a pandas DataFrame
df=pd.read_csv("cleaned_sub_counties.csv")
print(df)
print("reading csv")

sub_county_dict={}
id_count=4000

for index, row in df.iterrows():
    country_name=row["name_0"]
    county_name=row["name_1"]
    sub_county_name=row["name_2"]

    if county_name not in sub_county_dict:
        sub_county_dict[county_name]={
            "country_name":country_name,
            "county_name":county_name,
            "subCounties":[]
        }

    sub_county_dict[county_name]["subCounties"].append({
        "id":id_count,
        "subcounty_name":sub_county_name
    })
    id_count+=1


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
    with open("sub_county_data.json", "w") as outfile:
        outfile.write(json_output)
        print("Saved")
        print(json_output)