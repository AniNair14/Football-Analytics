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

# 