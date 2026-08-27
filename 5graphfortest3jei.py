#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1. Load data
df = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_final_schedule.csv')

# Create a column for Win % (100 for a win, 0 for a loss)
df['win_pct'] = (df['margin'] > 0) * 100

# 2. DRAW THE BAR CHART WITH SEABORN
fig, ax = plt.subplots(figsize=(7, 5.5))
colors = ['#4C72B0', '#DD8452']

sns.barplot(data=df, x='fan_group', y='win_pct', ax=ax,
            order=['no_fans', 'limited_fans'], # Keeps No Fans on the left
            palette=colors, capsize=0.1, errorbar=('ci', 95),
            edgecolor='black', width=0.5)

# 3. Add baseline
recent_baseline = 55.0  

# Draw the red dashed baseline for the recent era (2016-2025)
ax.axhline(recent_baseline, color='crimson', linestyle='--', )

# Clean up the text on the axes
ax.set_xticklabels(['No Fans\n(2020)', 'Limited Fans\n(2020)'])
ax.set_ylabel('Home Win Percentage (%)')

# Add extra space at the top so labels fit perfectly
ax.set_ylim(0, 80)

# Statistical results
t_nofan, p_nofan = -1.620, 0.1073
t_limited, p_limited = -0.445, 0.6570

# Clean up layout and save
plt.tight_layout()
plt.savefig('test3_jei_graph.png', dpi=300, bbox_inches='tight')
plt.show()
