# Importing the required packages:
import requests
from bs4 import BeautifulSoup
import json
import numpy as np
import pandas as pd

def scrape_shots(
        player_id: str
) -> pd.DataFrame:
    """
    Function to Scrape Shot x-y data from understat.com

        Parameters:
            player_id (str): Player ID as specified by understat
        
        Returns:
            df (pd.DataFrame): Dataframe containing the shot data of specified player

    """
    base_url = 'https://understat.com/player/'
    player = player_id

    # Generating the url: 
    url = base_url + player

    # Using requests to get the webpage and BeautifulSoup to parse the page
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    scripts = soup.find_all('script')

    # Getting the Shot data:
    strings = scripts[3].string

    # striping out the unnecessary symbols and get only JSON data:
    ind_start = strings.index("('")+2 
    ind_end = strings.index("')") 
    json_data = strings[ind_start:ind_end] 
    json_data = json_data.encode('utf8').decode('unicode_escape')

    # Converting the Strings to JSON:
    data = json.loads(json_data)

    # Converting the JSON data to a Pandas Dataframe:
    df = pd.DataFrame(data)

    return df

