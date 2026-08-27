# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

schedule = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_with_attendance_schedule.csv')
# FAN GROUP
#Create new column for fan group
schedule['fan_group'] = np.where(schedule['attendance'] == 0, 'no_fans', 'limited_fans')
print(schedule['fan_group'].value_counts())
# HOME WIN MARGIN
#Create new column for margin
schedule['margin'] = schedule['home_score'] - schedule['away_score']
# HOME WIN 
#Create new column for home win
schedule['home_win'] = (schedule['home_score'] > schedule['away_score']).astype(int)
print(schedule['home_win'].value_counts())
limited_fan_games = schedule[schedule['fan_group'] == 'limited_fans']
no_fan_games = schedule[schedule['fan_group'] == 'no_fans']
schedule.to_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_final_schedule.csv', index = False)
