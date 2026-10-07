# -*- coding: utf-8 -*-
import pandas as pd
from scipy.stats import ttest_ind
import nflreadpy as nfl
from statsmodels.stats.proportion import proportions_ztest

# load csv
schedule = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_final_schedule.csv')

no_fans = schedule[schedule['fan_group'] == 'no_fans']
limited = schedule[schedule['fan_group'] == 'limited_fans']


# Test 1 
# Welch t-test on Win Margin
print("\n\n********* TEST 1 - NO FANS VS LIMITED FANS - T TEST AND Z TEST *********")
print("********* WELCH's T TEST - ON WIN MARGIN *********")
t_score, p_value = ttest_ind(
    limited['margin'],
    no_fans['margin'],
    equal_var=False # For Welch t-test
    )
print(f"No fans average margin {no_fans['margin'].mean(): .3f}")
print(f"limited fans average margin {limited['margin'].mean(): .3f}")
print("T test output")
print(f"t_score for Home margin is {t_score: .3f}")
print(f"p_value for home margin is {p_value: .3f}")

# Proportions Z-Test on Win Percentage
print("\n********* Z TEST - ON WIN PERCENTAGE *********")
z_stat, p_value = proportions_ztest(
    [limited['home_win'].sum(), no_fans['home_win'].sum()],
    [len(limited), len(no_fans)] 
    )
print("Proportions Z-test output")
print(f"No fans win percentage {no_fans['home_win'].mean()*100: .2f}%")
print(f"limited fans win percentage {limited['home_win'].mean()*100: .2f}%")
print(f"z-statistic = {z_stat: .3f}")
print(f"p-value: {p_value: .3f}")


# Test 2 
# Comparing historical fans to No and Limited Fans 
historical_win_pct = 0.576  # Ehrlich et al. confirmed historical average (1970-2019)
# Test if no-fan win% differs significantly from historical
print("\n\n\n********* TEST 2 - 2020 VS HISTORICAL WIN PERCENTAGE - PROPORTIONS Z-TEST FOR NO FANS AND FOR LIMITED FANS *********")
z_historical_stat_no, p_historical_value_no = proportions_ztest(
    no_fans['home_win'].sum(),
    len(no_fans),
    value=historical_win_pct
    )
print(f"No fans vs historical: z_stat = {z_historical_stat_no:.3f}, p_value = {p_historical_value_no:.4f}")

# Test if limited-fan win% differs significantly from historical
z_historical_stat_lt, p_historical_value_lt = proportions_ztest(
    limited['home_win'].sum(),
    len(limited),
    value=historical_win_pct
    )
print(f"Limited fans vs historical: z_stat = {z_historical_stat_lt:.3f}, p_value = {p_historical_value_lt:.4f}")


# Test 3 
# Load multiple seasons
print("\n\n\n********* TEST 3 - 2020 VS RECENT ERA WIN PERCENTAGE FROM 2016-2025 - PROPORTIONS Z TEST FOR NO FANS AND FOR LIMITED FANS *********")
recent_seasons = nfl.load_schedules(seasons=[2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024,2025]).to_pandas()
recent_seasons = recent_seasons[recent_seasons['game_type'] == 'REG']
# Exclude any neutral site / international games
recent_seasons = recent_seasons[recent_seasons['location'] != 'Neutral']
print(f"Total games 2016-2019, 2021-2025: {len(recent_seasons)}")

recent_seasons['home_win'] = (recent_seasons['home_score'] > recent_seasons['away_score']).astype(int)
recent_win_pct = recent_seasons['home_win'].mean()
print(f"Home win% across these 9 seasons: {recent_win_pct*100:.1f}%")

z_stat_recent_no, p_val_recent_no = proportions_ztest(
    no_fans['home_win'].sum(),
    len(no_fans),
    value=recent_win_pct
    )
print(f"No fans vs recent era baseline for win percentage: z={z_stat_recent_no:.3f}, p={p_val_recent_no:.4f}")

z_stat_recent_lt, p_val_recent_lt = proportions_ztest(
    limited['home_win'].sum(),
    len(limited),
    value=recent_win_pct
    )
print(f"Limited fans vs 2016-19/2021-2022 baseline for win percentage: z={z_stat_recent_lt:.3f}, p={p_val_recent_lt:.4f}")



