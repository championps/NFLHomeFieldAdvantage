# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load The Data from CSV
df = pd.read_csv('C:\\Users\\sathi\\OneDrive\\Headwater Research\\code\\nfl_2020_final_schedule.csv')

# Create a win percentage column (If margin > 0, they won (100%), else they lost (0%))
df['win_pct'] = (df['margin'] > 0) * 100

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
colors = ['#4C72B0', '#DD8452']

# PANEL A: Box plot with jitter
ax1 = axes[0]

# Draw the boxes
sns.boxplot(data=df, x='fan_group', y='margin', ax=ax1,
            order=['no_fans', 'limited_fans'], # Keeps No Fans on the left
            palette=colors, width=0.5, showmeans=True, 
            boxprops={'alpha': 0.6}, # Makes boxes slightly see-through
            meanprops={'marker':'D', 'markerfacecolor':'white', 'markeredgecolor':'black'})

# Draw the dots right on top (stripplot adds the jitter automatically!)
sns.stripplot(data=df, x='fan_group', y='margin', ax=ax1,
              color='black', alpha=0.35, size=4, jitter=True)

# Add reference line and labels
ax1.axhline(0, color='gray', linestyle='--')
ax1.set_ylabel('Home Scoring Margin (points)')

# PANEL B: Bar chart (Win Percentage)
ax2 = axes[1]

# sns.barplot automatically calculates the 95% Confidence Interval!
sns.barplot(data=df, x='fan_group', y='win_pct', ax=ax2,
            order=['no_fans', 'limited_fans'], # Keeps No Fans on the left
            palette=colors, capsize=0.1, errorbar=('ci', 95), 
            edgecolor='black', width=0.5)

# Add reference line and labels
ax2.set_ylabel('Home Win Percentage (%)')
ax2.set_ylim(0, 80)

# Clean up layout and save
plt.tight_layout()
plt.savefig('test1_jei_graph.png', dpi=300, bbox_inches='tight')
plt.show()

