import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])[0]
    intercept = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])[1]
    x= np.arange(1880,2051)
    plt.plot(x,x*slope+intercept)
    sea_level_rise_2050 = 2050*slope+intercept

    # Create second line of best fit
    df_new = df[df['Year']>=2000]
    new_slope = linregress(x=df_new['Year'],y=df_new['NOAA Adjusted Sea Level'])[0]
    new_intercept = linregress(x=df_new['Year'],y=df_new['NOAA Adjusted Sea Level'])[1]
    x = np.arange(2000,2051)
    plt.plot(x,x*new_slope+new_intercept)
    sea_level_rise_2050_new=2050*new_slope+new_intercept
    # Add labels and title
    x = np.arange(2000, 2051)
    plt.plot(x, x * new_slope + new_intercept, label='Sea Level Rise')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()