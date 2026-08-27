# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 1. Load data
df = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_final_schedule.csv')

# Create the 100% (Win) or 0% (Loss) column
df['win_pct'] = (df['margin'] > 0) * 100

# 2. Draw the barchart with seaborn
fig, ax = plt.subplots(figsize=(7, 5.5))
colors = ['#4C72B0', '#DD8452']

# sns.barplot automatically calculates the means and the 95% Confidence Intervals!
sns.barplot(data=df, x='fan_group', y='win_pct', ax=ax,
            order=['no_fans', 'limited_fans'], # Keeps No Fans on the left
            palette=colors, capsize=0.1, errorbar=('ci', 95),
            edgecolor='black', width=0.5)

# 3. Add baseline, labels and text 
historical_baseline = 57.6  

# Draw the red dashed baseline
ax.axhline(historical_baseline, color='crimson', linestyle='--',)

# Rename the x-axis ticks to look nice
ax.set_xticklabels(['No Fans\n(2020)', 'Limited Fans\n(2020)'])
ax.set_ylabel('Home Win Percentage (%)')
ax.set_ylim(0, 80)

# Statistical results
t_nofan, p_nofan = -2.249, 0.0260
t_limited, p_limited = -0.979, 0.3298

# Clean up layout and save
plt.tight_layout()
plt.savefig('test2_jei_graph.png', dpi=300, bbox_inches='tight')
plt.show()
