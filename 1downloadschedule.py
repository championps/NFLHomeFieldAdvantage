# -*- coding: utf-8 -*-
import nflreadpy as nfl

#Loading 2020 schedule
schedule_polar = nfl.load_schedules(2020)
#making it pandas
schedule = schedule_polar.to_pandas()
schedule = schedule[schedule['game_type'] == 'REG']

schedule.to_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_schedule.csv', index=False)

schedule = schedule[schedule['location'] !=  'Neutral']
schedule['pfr_url'] = ('https:/www.pro-football-reference.com/boxscores/' + 
                       schedule['pfr'] + '.htm')

cols = ['game_id', 'week', 'gameday', 'home_team', 'away_team', 'home_score', 'away_score', 
        'spread_line', 'home_rest', 'away_rest', 'pfr_url', 'espn']
schedule = schedule[cols]
print("Saving the updated schedule to csv")
schedule.to_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_cleaned_schedule.csv', index = False)
print("Saved to C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_cleaned_schedule.csv")
