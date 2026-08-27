# -*- coding: utf-8 -*-
import pandas as pd
import requests
import time
import numpy as np

def get_attendance_espn(espn_id):
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/summary"
    params = {'event': int(espn_id)}
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout = 15)
            
            if resp.status_code == 200:
                data = resp.json()
                attendance = data['gameInfo']['attendance']
                awayname = data['boxscore']['teams'][0]['team']['abbreviation']
                homename = data['boxscore']['teams'][1]['team']['abbreviation']
                print(f"Attendance for ESPN IF {espn_id} {awayname} vs {homename} = {attendance}")
                if attendance is not None:
                    return int(attendance)
                else: 
                    return 0 
            elif resp.status_code == 504:
                # Gateway timeout - wait longer for each retry
                wait = (attempt + 1) * 5
                print(f" 504 timeout for {espn_id}, attempt {attempt+1}/3, waiting {wait} secs")
                time.sleep(wait)
                continue
            else:
                print(f" HTTP {resp.status_code} for {espn_id}")
                return None
        
        except requests.exceptions.Timeout:
            wait = (attempt + 1)  *5
            print(f" Failed after 3 attempts: {espn_id}, attempt {attempt+1}/3, waiting {wait} secs")
            return None
        
    print(f" Failed after 3 attempts: espn_id {espn_id}")
    return None

schedule = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_cleaned_schedule.csv')

attendances = []
total = len(schedule)
for idx, each_row in schedule.iterrows():
    att = get_attendance_espn(each_row['espn'])
    attendances.append(att)
    
    games_done = len(attendances)
    if games_done % 10 == 0:
        print(f"Progress: {games_done}/{total} - {each_row['home_team']} attendance={att}")
    time.sleep(3)

# update the schedule pandas dataframe to include a new column for attendance. 
schedule['attendance'] = attendances

schedule.to_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_with_attendance_schedule.csv', index = False)
print("Done saving csv with attendance")
print("Failed scrapes: ", schedule['attendance'].isna().sum())
# Fan group split
schedule['fan_group'] = np.where(schedule['attendance'] == 0, 'no_fans','limited_fans')
print(schedule['fan_group'].value_counts())
