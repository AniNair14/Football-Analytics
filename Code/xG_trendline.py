# Importing the required libraries:
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import gridspec
import matplotlib.patheffects as path_effects
from highlight_text import HighlightText
from highlight_text import ax_text
from highlight_text import fig_text
from requests import head

# Loading in the Dataset:
df = pd.read_excel('Data/Chelsea_xG.xlsx')

# Calculating 10 game Rolling Average for xG For and xG Against:
df['roll_xGF'] = df['xG'].rolling(
    window=10,
    center=True
).mean()

df['roll_xGA'] = df['xGA'].rolling(
    window=10,
    center=True
).mean()

# Creating the Figure for the plot:
fig = plt.figure(figsize=(45, 20))

# 
spec = gridspec.GridSpec(ncols=3, nrows=1, figure=fig, wspace=0.03)

# Axis for the gridspec columns:
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

ax1.spines['left'].set_linestyle((0,(5,5)))
ax1.spines['right'].set_linestyle((0,(5,5)))

ax2.tick_params(left=False)
ax2.tick_params(labelleft=False)

ax3.tick_params(left=False)
ax3.tick_params(labelleft=False)

# Axis values:
y_axis = [0,0.5,1,1.5,2,2.5]
x1_axis = [10,20,30]
x_axis = [0, 10, 20, 30] # For Grids 2 and 3

# Axis Labels:
y_labels = ['0','0.5','1','1.5','2','2.5']
x1_labels = ['10', '20', '30']
x_labels = ['0','10','20','30'] # For Grids 2 and 3

# Setting the ticks for the first Grid:
ax1.set_xticks(x1_axis)
ax1.set_yticks(y_axis)

# Setting the ticks for the second Grid: 
ax2.set_xticks(x_axis)
ax2.set_yticks(y_axis)

# Setting the ticks for the third Grid:
ax3.set_xticks(x_axis)
ax3.set_yticks(y_axis)

# Setting the labels and color for the ticks in the first Grid:
ax1.set_xticklabels(
    x1_labels,
    color='white',
    size=12,
    fontweight='bold'
)

ax1.set_yticklabels(
    y_labels,
    color='white',
    size=12,
    fontweight='bold'
)

# Setting the labels and color for the ticks in the second Grid:
ax2.set_xticklabels(
    x_labels,
    color='white',
    size=12,
    fontweight='bold'
)

ax2.set_yticklabels(
    y_labels,
    color='white',
    size=12,
    fontweight='bold'
)

# Setting the labels and color for the ticks in the third Grid:
ax3.set_xticklabels(
    x_labels,
    color='white',
    size=12,
    fontweight='bold'
)

ax3.set_yticklabels(
    y_labels,
    color='white',
    size=12,
    fontweight='bold'
)

# Setting x-axis limits:
ax1.set_xlim(0,39)
ax2.set_xlim(0,39)
ax3.set_xlim(0,39)

# Setting y-axis limits:
ax1.set_ylim(0,2.7)
ax2.set_ylim(0,2.7)
ax3.set_ylim(0,2.7)

ax1.grid(zorder=1,color="white",alpha=0.5, linestyle=((0,(5,5))))
ax2.grid(zorder=1,color="white",alpha=0.5, linestyle=((0,(5,5))))
ax3.grid(zorder=1,color="white",alpha=0.5, linestyle=((0,(5,5))))

def split_seasons(dataframe: pd.DataFrame, season: str)-> pd.DataFrame:
    """Function to split the data based on the seasons
    
        Parameters:
            dataframe (pd.DataFrame): The dataframe containing the data
            season (str): Column name containing the season values
    """
    filt = dataframe['Season'] == season

    new_df = dataframe[filt]

    return new_df

# 2019/20 season:
first = split_seasons(
    dataframe=df, 
    season= '19/20'
)

# 2020/21 season:
second = split_seasons(
    dataframe=df, 
    season= '20/21'
)

# 2021/22 season:
third = split_seasons(
    dataframe=df, 
    season= '21/22'
)

# Function for plotting the data:
def line_plots(
    axis: matplotlib.axes, 
    dataframe: pd.DataFrame, 
    xG_for: str, 
    xG_against: str
)-> matplotlib.axes:
    """Function to create the lineplot for the xG trend graph

        Parameters:
            axis (matplotlib.axes): Plot axis
            dataframe (pd.DataFrame) Pandas Dataframe containing data
            xG_for (str): Column name for running xG scored
            xG_against (str) Column name for running xG conceded    
    """
    # xG for:-
    axis.plot(
        dataframe['Round'].tolist(),
        dataframe[xG_for].tolist(),
        color='#2F2FFF', 
        zorder=2, 
        lw=2, 
        mec=bg
    )

    axis.scatter(
        dataframe['Round'].tolist(),
        dataframe[xG_for].tolist(),
        s=100, 
        color='#2F2FFF', 
        edgecolors=bg, 
        zorder=3, 
        linewidth=1
    )

    # xG Against:
    axis.plot(
        dataframe['Round'].tolist(),
        dataframe[xG_against].tolist(),
        color='#FF0000', 
        zorder=2, 
        lw=2, 
        mec=bg
    )

    axis.scatter(
        dataframe['Round'].tolist(),
        dataframe[xG_against].tolist(),
        s=100, 
        color='#FF0000', 
        edgecolors=bg, 
        zorder=3, 
        linewidth=1
    )

    return axis

# Plotting the 2019-20 season data:
first_plot = line_plots(
    axis=ax1,
    dataframe=first,
    xG_for='roll_xGF',
    xG_against='roll_xGA'
)

# Plotting the 2020-21 season data:
second_plot = line_plots(
    axis=ax2,
    dataframe=second,
    xG_for='roll_xGF',
    xG_against='roll_xGA'
)

# Plotting the 2021-22 season data:
third_plot = line_plots(
    axis=ax3,
    dataframe=third,
    xG_for='roll_xGF',
    xG_against='roll_xGA'
)

# Axis Titles:
axis_1_text = ax1.text(
    17,
    2.75,
    "2019-20",
    color='white',
    fontfamily=body_font,
    size=17.5,
    fontweight='bold',
    zorder=2
)

axis_1_text.set_path_effects([path_effects.withStroke(
    linewidth=4,
    foreground=bg
)])

axis_2_text = ax2.text(
    17,
    2.75,
    "2020-21",
    color='white',
    fontfamily=body_font,
    size=17.5,
    fontweight='bold',
    zorder=2
)

axis_2_text.set_path_effects([path_effects.withStroke(
    linewidth=4,
    foreground=bg
)])

axis_3_text = ax3.text(
    17,
    2.75,
    "2021-22",
    color='white',
    fontfamily=body_font,
    size=17.5,
    fontweight='bold',
    zorder=2
)

axis_3_text.set_path_effects([path_effects.withStroke(
    linewidth=4,
    foreground=bg
)])

# Axis Label text:
y_text_label = ax1.text(
    -6,0.75,
    "Expected Goals per Game", 
    rotation=90, 
    color='white', 
    size=20, 
    fontfamily=body_font, 
    zorder=2
) 

y_text_label.set_path_effects([path_effects.withStroke(
    linewidth=4,
    foreground=bg
)])

x_text_label = ax1.text(
    55,-0.2, 
    "Match Number", 
    color='white', 
    size=20, 
    fontfamily=body_font, 
    zorder=2
)

x_text_label.set_path_effects([path_effects.withStroke(
    linewidth=4,
    foreground=bg
)])

# Title:
title =\
fig_text(
    s="How Chelsea's expected goals <for> & <against> trend over time",
    x=0.3,
    y=0.99,
    color='white',
    fontfamily=title_font,
    fontsize=25,
    highlight_textprops=[{'color': '#2F2FFF'},
                         {'color': '#FF0000'}],
    fontweight='bold'
)

fig.text(
    0.315,0.94, 
    "10 game rolling average | English Premier League | Seasons 2019/20 - 21/22", 
    color='white', 
    size=20, 
    fontfamily=body_font, 
    zorder=2
)

ax1.text(
    -3.5,
    -0.25, 
    "Data: Fbref | Statsbomb", 
    color='white', 
    size=15, 
    fontfamily=body_font
)

ax3.text(
    30,
    -0.25, 
    "By: Anish Nair\n(@AniNair14)", 
    ha='center', 
    color='white', 
    size=15, 
    fontfamily=body_font
)

# plt.savefig(
#     "Plots/Chelsea_Trend.jpg", 
#     facecolor=bg,
#     bbox_inches="tight", 
#     dpi=700
# )

plt.show()