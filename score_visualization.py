import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
w1 = 0.5
w2 = 0.5

os.chdir('C:\\Users\\GU\\Desktop') 
df = pd.read_excel('Wordle_cleaned.xlsx')
#print(df)

df['score'] = w2 * df['7 or more tries (X)'] + w1 * (1*df['1 try'] + 2*df['2 tries'] + 3*df['3 tries'] + 4*df['4 tries'] + 5*df['5 tries'] + 6*df['6 tries'])


scores = df['score'].values
min_score, max_score = min(scores), max(scores)

num_bins = 20
bin_edges = np.linspace(min_score, max_score, num_bins+1)

colors = LinearSegmentedColormap.from_list('', ['#6cac64', '#ccb45c'])

plt.figure(figsize=(12, 6))
n, bins, patches = plt.hist(scores, bins=bin_edges, edgecolor='black')

for i, patch in enumerate(patches):
    color = colors(i / len(patches))
    patch.set_facecolor(color)

plt.xlabel('Score', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Wordle Scores', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# 添加颜色条
sm = plt.cm.ScalarMappable(cmap=colors, norm=plt.Normalize(vmin=min_score, vmax=max_score))
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label('Score Value', rotation=270, labelpad=15)

plt.tight_layout()
plt.show()