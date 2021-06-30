import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

"""
For Visualization # (Scatterplot w/ Line of Best Fit)
"""

#import data for bikes in Seoul, Korea from UCI's Repository
seoul_bike_data = pd.read_csv("SeoulBikeData.csv")

#create dictionary for colors
colors = {"Winter":"b","Summer":"g","Spring":"c","Autumn":"r"}

#setup new graph
fig, ax = plt.subplots()

#create lists from the columns in the .csv file
wind_column = seoul_bike_data["Wind speed (m/s)"]
hour_column = seoul_bike_data["Hour"]
rented_bikes_column = seoul_bike_data["Rented Bike Count"]
seasons_column = seoul_bike_data["Seasons"]

#prepare lists for data from the 12th hour of each day
wind_condensed_column = []
rented_bikes_condensed_column = []
seasons_condensed_column = []

#only store data from the 12th hour of each day (otherwise too much data)
for i in range(len(hour_column)):
    if hour_column[i] == 12:
        wind_condensed_column.append(wind_column[i])
        rented_bikes_condensed_column.append(rented_bikes_column[i])
        seasons_condensed_column.append(seasons_column[i])

#create the scatterplot
for i in range(len(wind_condensed_column)):
    ax.scatter(wind_condensed_column[i], rented_bikes_condensed_column[i], color = colors[seasons_condensed_column[i]])

#format graph
ax.set_title("Mid-Day Bike Rentals vs. Wind Speeds from January 2017 to November 2018 in Seoul, South Korea" , fontsize=10)
ax.set_xlabel("Wind speed during the 12th hour (m/s)",fontsize=8)
ax.set_ylabel("Number of Bikes Rented during the 12th hour",fontsize=8)

#set up legend and match the colors using the dictionary
winter_legend = mpatches.Patch(color = colors["Winter"], label = "Winter")
summer_legend = mpatches.Patch(color = colors["Summer"], label = "Summer")
spring_legend = mpatches.Patch(color = colors["Spring"], label = "Spring")
autumn_legend = mpatches.Patch(color = colors["Autumn"], label = "Autumn")

#create a legend based on the color of the dots
ax.legend(handles=[winter_legend, summer_legend, spring_legend, autumn_legend])

#create a line of best fit and color it black
plt.plot(np.unique(wind_condensed_column), np.poly1d(np.polyfit(wind_condensed_column, rented_bikes_condensed_column, 1))(np.unique(wind_condensed_column)), color = "k")


"""
For Visualization #2
"""

#import calories data from Princeton's repository
calories_data = pd.read_csv("calories.csv")

#make 2 lists from 2 of the columns
food_data = calories_data["Food"]
protein_data = calories_data["Protein (g)"]

#merge into a list of tuples
tuples = list(zip(food_data, protein_data))

#turn the list of tuples into a dataframe
df = pd.DataFrame(tuples)

#rename the dataframe's columns
df.columns = ["Name of Food Item","protein"]

#turn the protein column into a form in which we can calculate the average of
df["protein"] = df["protein"].apply(pd.to_numeric, errors="coerce")

#set up new graph
fig1, ax1 = plt.subplots()
ax1.set_title("Top 5 Foods with the Highest Amounts of Protein on Average")
ax1.set_ylabel("Average Amount of Protein (g)",fontsize = 8)
ax1.set_xlabel("Name of Food Item",fontsize = 8)


#sort and graph data by food name, find the average of the protein (in grams) and round to one decimal place
df.groupby("Name of Food Item").protein.mean().round(1).sort_values(ascending=False)[:5].plot.bar(rot = 45, fontsize = 8)


"""
For Visualization #3
"""

#import dow jones industrial average data from Princeton's repository
dow_jones_data = pd.read_csv("DJIA.csv")

#remove future based prediction data (e.g. data for year 2080)
select_dow_jones = dow_jones_data[:19137]

#create a new graph
fig2, ax2 = plt.subplots()

#format the graph
ax2.set(yticks=[0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000])
ax2.set_title("Dow Jones Industrial Average from January 2, 1930 to March 17, 2006")
ax2.set_ylabel("Price-Weighted Index Value",fontsize = 8)
ax2.set_xlabel("Day Number",fontsize = 8)

#plot only the Highs, Lows, and Adjusted Closing Prices
sns.lineplot(data = select_dow_jones.drop(["Date", "Volume","Open","Close"], axis = 1))

#show all 3 visualizations
plt.show()


