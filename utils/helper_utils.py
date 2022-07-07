# Importing the required packages:
import numpy as np
import pandas as pd

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
            df (pd.DataFrame): Updated Dataframe with Statsbomb X-Y coordinates
    
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
