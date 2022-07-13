# Importing the required libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import gridspec
import matplotlib.patheffects as path_effects
from highlight_text import HighlightText
from highlight_text import ax_text
from highlight_text import fig_text

# Loading in the Dataset:
df = pd.read_excel('Data/Chelsea_xG.xlsx')

# Calculating 10 game Rolling Average for xG For and xG Against:
df['roll_xGF'] = df['xG'].rolling(
    window=10,
    min_periods=0
).mean()

df['roll_xGA'] = df['xGA'].rolling(
    window=10,
    min_periods=0
).mean()

# Creating the Figure for the plot:
fig = plt.figure(figsize=(45, 20))

# 
spec = gridspec.GridSpec(ncols=3, nrows=1, figure=fig, wspace=0.03)

# Ax for the gridspec columns:
ax1 = fig.add_subplot(spec[0,0])
ax2 = fig.add_subplot(spec[0,1])
ax3 = fig.add_subplot(spec[0,2])

# Setting the background colour for the plot:
bg = "#141414"

# Assigning Tiltle and Body fonts
title_font = "Open Sans"
body_font = 'Calibri'

fig.set_facecolor(bg)

ax1.patch.set_facecolor(bg)
ax2.patch.set_facecolor(bg)
ax3.patch.set_facecolor(bg)


ax1.spines['bottom'].set_color('white')
ax1.spines['left'].set_color('white')

ax2.spines['bottom'].set_color('white')

ax3.spines['bottom'].set_color('white')


for side in ['right','left','top','bottom']:
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['top'].set_visible(False)
    ax3.spines['left'].set_visible(False)

plt.show()