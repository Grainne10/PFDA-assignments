# PFDA-assignments

**by Grainne Boyle**

**Contents:** 

1. [Overview](#Ooverview)
2. [Tasks](#Tasks)
3. [Overview](#overview
4. [Overview](#overview
5. [Overview](#overview

## Overview

I work at [TE Connectivity] (https://www.te.com/usa-en/home.html)

I am a student at the [Atlantic Technological University] (https://www.atu.ie/), Galway, studying the Higher Diploma in Science in Data Analytics on a part-time basis over 2 years.

This repository contains weekly assignments completed as part of the Programming for Data Analytics module. Each notebook demonstrates various Python programming techniques, data analysis approaches, and problem-solving strategies. It describes the weekly assignments and explains how I solved them and what research I did.   


## Tasks 

### Task 1: Repository Setup

#### Task Description:
Create a repository for this module, and upload a link to where you will put your handups.  

#### Task Solution:
For this module, I created three repositories following the course guidelines:  

- `PFDA-assignments`: Folder/Repository for course assignments  
- `PFDA-mywork/`: Folder/Repository for additional work and exercises  
- `PFDA-project/`: Folder/Repository for module project work  
 
 The objectives of this task were to familiarize students with GitHub repository creation, learn basic repository and folder management and understand the process of pushing work to GitHub.

### Task 2: Weather 

#### Task Description:
Read in a CSV file and create a jupyter notebook assignment2-weather.ipynb that has a nice plot of the temperature over time  

#### Task Solution:

The task requires the user to import, export and manipulate data. I show how to handle time data, how to clean and preprocess data and also create an informative visualisation. I imported the necessary libraries (pandas and matplotlib) and read the CSV file into a DataFrame. I created an excel file to view the data first and check if there was any missing data. The file weatherreadings1.csv contains time and temperature data, which I cleaned and prepare for visualization. I decided to use a stem plot as I thought it was a very clear visual which displayed the temperature (°C) on the y-axis and time on the x-axis. It showed the fluctuations in temperature over time, with annotations highlighting the highest and lowest temperatures.

### Task 3:

#### Task Description: Pie
Create a notebook called assignment03-pie.ipynb. The note book should have a nice pie chart of peoples email domains in the csv file at the url.

#### Task Solution:

The task requires the user to create a Jupyter notebook that generates a visually appealing pie chart from a CSV file containing information about 1000 people. The focus of the task is on extracting and visualizing the email domains from this dataset. The dataset is available via a Google Drive link, and I read it into a dataframe using the url . I viewed the data in excel, there were no empty cells under the email domain.The dataset contains an "Email" column. I extracted the domain of each email by splitting the email string at the "@" symbol. This gives me the domain, which I stored in a new column called 'domain'.To visualize the distribution of email domains, I grouped the data by the 'domain' column and counted how many people have each domain. Using the matplotlib library, I created a pie chart of the domain counts. I added percentage annotations on each slice to provide more insight into the data.

### Task 4:

#### Task Description: Risk
The task involves simulating a series of individual battle rounds from the board game Risk, specifically the battle between an attacker with 3 dice and a defender with 2 dice. The goal is to simulate 1000 battle rounds and analyze the outcome.

#### Task Solution:
The program require the user to simulate random dice rolls for both the attacker and the defender. It helps you practice random number generation, conditional logic, iteration, and data visualization. By simulating many rounds, you can observe and analyze the distribution of troop losses for both sides in a Risk battle. 
I used numpy for array manipulation and random number generation. I defined a standard 6-sided die and represemted the dice using a NumPy array, dice, containing values from 1 to 6. Then I used a function to simulate rolling the dice . It uses np.random.choice() to randomly select values from the dice array. I used n_battle = 1000 to set the number of battle rounds to simulate (1000 rounds). I used counters to track how many rounds the attacker wins, the defender wins, and how many rounds end in a tie. This loop runs 1000 times, simulating one battle round per iteration. Inside the loop, the variables attacker_wins and defender_wins are reset to 0 at the start of each round. In each battle round, the attacker rolls 3 dice and the defender rolls 2 dice, with both sets of rolls being sorted in descending order using np.sort() and then reversed to ensure the highest values are compared first. The code then checks if both the attacker and defender win at least one comparison, which would indicate a tie. If the defender doesn't win any comparisons, the attacker wins that round (attacker_total is incremented). Otherwise, the defender wins (defender_total is incremented).After all rounds are completed, the program prints the total number of wins for the attacker, defender, and ties. I visualised the data in a Pie Chart showings the proportion of wins for the attacker, defender, and ties. 
I found this task extremely difficult, I changed it several times before I found a solution that worked correctly and calculated only 1000 rounds.

### Task 5:

#### Task Description: Weather
The task is to create a python file or notebook called assignment_6_Weather (.py or .ipynb) by importing a csv file and plotting the data. 
#### Task Solution:

The purpose of this task is to work with weather data and perform basic data analysis and visualization using Python. I analyse temperature data by calculating daily and monthly averages. I load, manipulate, and analyze time series data from a CSV file. Use time series plotting techniques to visualize temperature changes over time, including the daily and monthly mean temperatures. The task helps develop skills in handling real-world data, performing aggregation, and providing informative visualizations. 

Firstly , I pull in the weather data from the provided URL using the Pandas library. Since there were unnecessary rows at the beginning of the file, I used the skiprows parameter to bypass them. I then selected the relevant columns: "date", "temp", and "wdsp". After loading the data, I converted the 'date' column to a datetime format using pd.to_datetime() for accurate time series analysis. Finally, I renamed the columns to more readable names: "Date", "Temperature", and "Wind Speed".

I extracted the 'year' and 'month' from the 'Date' column to make future analysis easier. I created separate columns for 'year' and 'month' to facilitate grouping by these time periods. Then, I calculated the average temperature for each year to observe long-term trends.

For the temperature task, I plotted the average temperature for each year to visualize temperature trends over time. The plot highlights significant temperature fluctuations, with a notable drop in 2010 and an increase in temperatures from 2020 to 2024. The highest average temperature recorded since 1995 occurred in 2024.

In the mean daily temperature task, I compare the coldest year (2010) and the hottest year (2024) by plotting the daily mean temperatures for each year. Two subplots are created: one showing the daily temperatures for 2010 and the other for 2024, highlighting the temperature trends in both years.

In the mean monthly temperature task, I analyze the average monthly temperatures from 2020 to 2024. Using resampling, I calculated the monthly mean temperature and visualized the trends with a line plot to show temperature changes over the selected years.

In the windspeed task, I checked for missing values in the dataset and found that there were some blank entries in the 'Wind Speed' column. I replaced the blank values with NaN and then removed all rows with missing data. Finally, I converted the 'Wind Speed' column to a numerical data type (float) for consistency in further analysis. Then, I calculated the average wind speed for each year by grouping the data by the 'year' column and computing the mean wind speed for each group. I created a plot to visualize the average wind speed over the years. The plot reveals a decline in wind speed from 2020 to 2024, which is notable because, during the same period, temperatures were rising.






## Prerequisites
- Python 3.x
- Anaconda
- Visual Studio Code
