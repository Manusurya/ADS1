# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 12:03:10 2023

@author: manus
"""

# importing pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt

# read the data from the plt1 excel file for ploting the bar chart
cf = pd.read_excel("plt1.xlsx")
# read the data from the plt2 excel file for plotting the line plot
df = pd.read_excel('plt2.xlsx')
# read data from the plt3 excel file for plotting the scatter plot
ef = pd.read_excel('plt3.xlsx')


# define a function bargraph to represent the above data as a barchart
def bargraph():
    # print plt1 dataset as output
    print("Dataset for horizontal bar plot:")
    print(cf)
    # defining a list with colours for different regions in the bar plot
    colours = ['red', 'blue', 'brown', 'green', 'orange', 'violet']
    # assigning dataset values into lists region and conc
    region = cf['Region']
    conc = cf['Concentration']
    # calling barh function for plotting horizontal bar plot
    plt.figure()
    plt.barh(region, conc, color=colours)
    # calling xlabel function to set X axis label to Concentration in units of microgram/meter cube
    plt.xlabel('Concentration (micro gram/m^3)')
    # calling ylabel function to set Y axis label to Regions
    plt.ylabel('Regions')
    # calling the title funtion to set a title name for the plot
    plt.title('Contribution of PM2.5 by Mainlands during the Year 2019')
    plt.show()  # calling the show function to dsiplay the plot


# define a function linegraph to represent the above data as a line plot
def linegraph():
    # print plt2 dataset as output
    print("Dataset for line plot:")
    print(df)
    # calling plot function for plotting the line plot
    plt.figure()
    plt.plot(df['Year'], df['UK'], label='UK')
    plt.plot(df['Year'], df['Germany'], label='Germany')
    plt.plot(df['Year'], df['Ukraine'], label='Ukraine')
    plt.plot(df['Year'], df['Italy'], label='Italy')
    plt.legend()
    plt.xlabel('Year')  # calling xlabel function to set X axis label to Year
    # calling ylabel function to set Y axis label to Concentration in units of microgram/meter cube
    plt.ylabel('Concentration (micro gram/m3)')
    # calling the title function to set a title name for the plot
    plt.title('Change in concentration of PM2.5 over the years')
    plt.show()  # calling the show function to display the plot


# define a function scatterplot to represent the above data as a scatter plot
def scatterplot():
    # print plt3 dataset as output
    print("Dataset for scatter plot:")
    print(ef)
    # defining a dictionary with different colours for different residential areas
    colors = {'Rural': 'red', 'Towns': 'green',
              'Urban': 'yellow', 'Cities': 'blue'}
    # calling scatter function for plotting the scatter plot
    plt.scatter(ef['Region'], ef['Conc.'], c=ef['Residence Area'].map(colors))
    # printing colors dictionary to act as a legend for the plot
    print(colors)
    # calling xlabel function to set X axis label to Regions
    plt.xlabel('Regions')
    # calling ylabel function to set Y axis label to Concentration in units of microgram/meter cube
    plt.ylabel('Concentration (micro gram/m3)')
    # calling the title function to set a title name for the plot
    plt.title('Concentration of PM25 in different Residence Areas for 2019')
    plt.show()  # calling the show function to display the plot
    
bargraph() #function call for bar plot
linegraph() #function call for line plot
scatterplot() #function call for scatter plot
