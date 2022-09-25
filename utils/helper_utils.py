# Importing the required packages:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from mplsoccer import Pitch, VerticalPitch

def convert_to_statsbomb(
    data: pd.DataFrame,
    x_cords: str,
    y_cords: str
):
    """
    Function to convert understat X and Y coordinate data to Statsbomb coordinates

        Parameters:
            data (pd.DataFrame): Dataframe containing X-Y data 
            x_cords (str): X coordinate column name
            y_cords (str): Y coordinate column name
        
        Returns:
            df (pd.DataFrame): Updated Dataframe with Statsbomb X-Y 
            coordinates
    
    """
    df = data.copy()

    # Convert X and Y coordinate values to numeric type:
    df[x_cords] = pd.to_numeric(df[x_cords])
    df[y_cords] = pd.to_numeric(df[y_cords])

    # Rescaling the coordinates from 0-1 to 0-100:
    df[x_cords] = df[x_cords] * 100
    df[y_cords] = df[y_cords] * 100

    df['xx'] = df[y_cords]
    df['yy'] = df[x_cords]

    df[x_cords] = df['xx']
    df[y_cords] = df['yy']

    # Rescaling the X-Y coordinates to the statsbomb scale:
    df[x_cords] = df[x_cords] * .8
    df[y_cords] = df[y_cords] * 1.2

    return df


def statsbomb_pitch_vert(
    ax: plt.Axes,
    bg: str,
    grid: bool = False
)->plt.Axes:
    """
    Function to plot a Vertical Statsbomb football pitch

        Parameters:
            ax (plt.Axes): Axes specified for the Statsbomb pitch
            bg (str): Background color 
            grid (bool): Specifing whether grid lines should be drawn on the pitch or not

        Returns:
            ax (plt.Axes): Vertical pitch with Statsbomb coordinates
    """
    pitch = VerticalPitch(
        half=True,
        pitch_type= 'statsbomb',
        pitch_color=bg,
        goal_type='box',
        line_color='grey',
    )

    pitch.draw(ax = ax)

    if grid:
        y_lines = [120 - 6.5*x for x in range(1,10)]
        x_lines = [80 - 8.0*x for x in range(1,10)]

        for i in x_lines:
            ax.plot(
                [i, i], [45, 120],
                color='grey',
                ls = '--',
                lw=0.75,
                zorder=1
            )

        for j in y_lines:
            ax.plot(
                [0, 80], [j, j],
                color='grey',
                ls='--',
                lw='0.75',
                zorder=1
            )

    return ax

def shot_map(
    axis: plt.Axes,
    data: pd.DataFrame,
    situation: str,
    x_pos: str,
    y_pos: str,
    color: str,
    edge_col: str
)->plt.axes:
    """
    Function to plot a shot map on a football pitch

        Parameters:
            axis (plt.Axes): Axes specified for the football pitch
            data (pd.DataFrame): Dataframe containing the Shot data
            situation (str): Result after the shot (Goal or not)
            x_pos (str): Values of x-coordinate of the shot
            y_pos (str): Values of y-coordinate of the shot
            color (str): Color for the scatter plots of the shot
            edge_col (str): Color for the edges of the scatter plots

        Returns:
            axis (plt.Axes): Shot Map
    """
    if situation == 'Goal':
        filt = data['result'] == situation

        data = data[filt]

        size = np.sqrt(data['xG'].astype(float))*500

        axis.scatter(
            data[x_pos].tolist(),
            data[y_pos].tolist(),
            s=size,
            alpha=0.7,
            color=color,
            edgecolor=edge_col,
            zorder=4,
            lw=2.2
        )

    else:
        filt = data['result'] != 'Goal'

        data = data[filt]

        size = np.sqrt(data['xG'].astype(float))*500

        axis.scatter(
            data[x_pos].tolist(),
            data[y_pos].tolist(),
            s=size,
            alpha=0.45,
            color=color,
            edgecolor=edge_col,
            zorder=3,
            lw=1.25
        )

    return axis