import pandas as pd
from datetime  import datetime, timedelta, timezone
import os

dir = os.path.join(os.path.expanduser('~'), 'Downloads','odkdata', 'ldsf_Kenya_LCA')
main_csv = 'ldsf_Kenya_LCA.csv'
data_dir = os.path.join(dir, main_csv)

df = pd.read_csv(data_dir)

#conver the submission date column to a datetime with UTC timezone
df['SubmissionDate'] = pd.to_datetime(df['SubmissionDate'], utc=True)

#get todays date & seven days ago date in UTC
date_today = datetime.now(timezone.utc)
seven_days_ago = (date_today - timedelta(days=7)).date()

#filter the dataframe to only include rows where the submission date is within the last week
df_a_week_ago = df[df['SubmissionDate'].dt.date >= seven_days_ago]

#get the keys
keys = df_a_week_ago['KEY'].tolist()

#get the csv filenames
filenames = [file for file in os.listdir(dir) if file.endswith('.csv') and file != main_csv] 

for name in filenames:
    #get the df to process 
    doi = pd.read_csv(os.path.join(dir,name))

    #constuct its new name
    new_filename = f'latest_{name}'

    #get the df row values for the keys matching a week ago
    recent_data = doi[doi['PARENT_KEY'].isin(keys)]
    print(recent_data)


    #save to csv
    recent_data.to_csv(new_filename, index=False)

    print(f'finished processing {name} >> saved to {new_filename} >> with {len(recent_data)} rows ')

#get recent data for main csv
recent_main = df[df['KEY'].isin(keys)]
recent_main.to_csv('latest_' + main_csv, index=False)
print(f'finished processing {main_csv} >> saved to latest_{main_csv} >> with {len(recent_main)} rows ')
