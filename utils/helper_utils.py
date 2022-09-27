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
)-> pd.DataFrame:
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
        y_lines = [120 - 6.2*x for x in range(1,10)]
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

# Defining zone areas for shot zone plot:
zone_areas = {
    'zone_1': {
        'x_lower_bound': 0.0, 'x_upper_bound': 18.0,
        'y_lower_bound': 102.0, 'y_upper_bound': 120.0,
    },
    'zone_2': {
        'x_lower_bound': 62.0, 'x_upper_bound': 80.0,
        'y_lower_bound': 102.0, 'y_upper_bound': 120.0,
    },
    'zone_3': {
        'x_lower_bound': 0.0, 'x_upper_bound': 18.0,
        'y_lower_bound': 55.0, 'y_upper_bound': 102.0,        
    },
    'zone_4': {
        'x_lower_bound': 62.0, 'x_upper_bound': 80.0,
        'y_lower_bound': 55.0, 'y_upper_bound': 102.0,
    },
    'zone_5': {
        'x_lower_bound': 50.0, 'x_upper_bound': 62.0,
        'y_lower_bound': 102.0, 'y_upper_bound': 120.0,
    },
    'zone_6': {
        'x_lower_bound': 18.0, 'x_upper_bound': 30.0,
        'y_lower_bound': 102.0, 'y_upper_bound': 120.0,
    },
    'zone_7': {
        'x_lower_bound': 30.0, 'x_upper_bound': 50.0,
        'y_lower_bound': 102.0, 'y_upper_bound': 114.0,
    },
    'zone_8': {
        'x_lower_bound': 30.0, 'x_upper_bound': 50.0,
        'y_lower_bound': 114.0, 'y_upper_bound': 120.0,
    },
    'zone_9': {
        'x_lower_bound': 50.0, 'x_upper_bound': 62.0,
        'y_lower_bound': 85.8, 'y_upper_bound': 102.0,
    },
    'zone_10': {
        'x_lower_bound': 18.0, 'x_upper_bound': 30.0,
        'y_lower_bound': 85.8, 'y_upper_bound': 102.0,
    },
    'zone_11': {
        'x_lower_bound': 30.0, 'x_upper_bound': 50.0,
        'y_lower_bound': 85.8, 'y_upper_bound': 102.0,
    },
    'zone_12': {
        'x_lower_bound': 18.0, 'x_upper_bound': 62.0,
        'y_lower_bound': 55.0, 'y_upper_bound': 85.8,
    }
}

def assign_shot_zones(
    x: float,
    y: float
)-> str:
    """
    Function to assign shot zones based on x and y coordinate values of the shot

        Parameters:
            x (float): x coordinate of the shot
            y (float): y coordinate of the shot

        Returns:
            zone (str): Shot zone based on x and y coordinate values of the shot 
    """
    global zone_areas

    for zone in zone_areas:
        if (
            (x >= zone_areas[zone]['x_lower_bound']) 
            & (x <= zone_areas[zone]['x_upper_bound'])
        ):
            if (
                (y >= zone_areas[zone]['y_lower_bound']) 
                & (y <= zone_areas[zone]['y_upper_bound'])
            ):
                return zone

def plot_shot_zones(
    axis: plt.Axes,
    bg: str,
    grid_col: str,
    zone_col: str,
    text_col: str,
    font: str,
    data: pd.DataFrame,
)-> plt.Axes:
    """
    Function to plot the shot zones on a shot map

        Parameters:
            axis (plt.Axes): Axes to plot the shot zone map
            bg (str): Background color of the pitch
            grid_col (str): Color of the grids on the pitch for the zones
            zone_col (str): Color of the zone regions on the pitch
            text_col (str): Color of the text on the plot
            font (str): Font of the text
            data (pd.DataFrame): Dataframe containing the shot and zone information of the player

        Returns:
            axis (plt.Axes): Shot zone plot 

    """
    global zone_areas

    pitch = VerticalPitch(
        half=True,
        pitch_type= 'statsbomb',
        pitch_color=bg,
        goal_type='box',
        line_color='grey',
    )

    pitch.draw(ax = axis)

    # Plotting the grids:
    axis.plot(
        [62.0, 62.0], [40.0, 102.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [18.0, 18.0], [40.0, 102.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [30.0, 30.0], [102.0, 114.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [50.0, 50.0], [102.0, 114.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [62.0, 80.0], [102.0, 102.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [18.0, 0.0], [102.0, 102.0], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )
    axis.plot(
        [18.0, 62.0], [85.8, 85.8], 
        ls='--', 
        color=grid_col, 
        lw=0.75
    )

    max_value = data['pct'].max()

    for zone in data['zone_area']:
        shot_pct = data[
            data['zone_area'] == zone
        ]['pct'].iloc[0]
        
        x_lim = [
            zone_areas[zone]['x_lower_bound'], 
            zone_areas[zone]['x_upper_bound']
        ]
        
        y1 = zone_areas[zone]['y_lower_bound']
        y2 = zone_areas[zone]['y_upper_bound']
        
        axis.fill_between(
            x=x_lim, 
            y1=y1, 
            y2=y2, 
            color=zone_col, 
            alpha=(shot_pct/max_value),
            zorder=0, 
            ec='None'
        )
       
        if shot_pct > 0.05:
            x_pos = x_lim[0] + abs(x_lim[0] - x_lim[1])/2
            y_pos = y1 + abs(y1 - y2)/2
            text_ = axis.annotate(
                xy=(x_pos, y_pos),
                text=f'{shot_pct:.0%}',
                ha='center',
                va='center',
                color=text_col,
                fontfamily=font,
                weight='bold',
                size=16
            )
            text_.set_path_effects(
                [
                    path_effects.Stroke(
                        linewidth=1.5, foreground='black'
                    ), 
                    path_effects.Normal()
                ]
            )
    
    return axis
