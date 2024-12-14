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

This repository contains weekly assignments and tasks completed as part of the Programming for Data Analytics module. Each notebook demonstrates various Python programming techniques, data analysis approaches, and problem-solving strategies. It describes the weekly tasks and explains how I solved them and what research I did . I include reference resources that I used to come to the solution.


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

The task requires the user to import, export and manipulate data. It shows how to handle time data, how to clean and preprocess data and also creates an informative visualisation. I imported the necessary libraries (pandas and matplotlib) and read the CSV file into a DataFrame. I created an excel file to view the data first and check if there was any missing data. The file weatherreadings1.csv contains time and temperature data, which I cleaned and prepare for visualization. I created a stem plot whicd displayed the temperature (°C) on the y-axis and time on the x-axis. It showed the fluctuations in temperature over time, with annotations highlighting the highest and lowest temperatures.

### Task 3:

#### Task Description: Pie
Create a notebook called assignment03-pie.ipynb. The note book should have a nice pie chart of peoples email domains in the csv file at the url

#### Task Solution:

The task requires the user to create a Jupyter notebook that generates a visually appealing pie chart from a CSV file containing information about 1000 people. The focus of the task is on extracting and visualizing the email domains from this dataset. The dataset is available via a Google Drive link, and I read it into a dataframe using the url . I viewed the data in excel, there were no empty cells under the email domain.The dataset contains an "Email" column. I extracted the domain of each email by splitting the email string at the "@" symbol. This gives me the domain, which I stored in a new column called 'domain'.To visualize the distribution of email domains, I grouped the data by the 'domain' column and counted how many people have each domain.Using the matplotlib library, I created a pie chart of the domain counts. I ensured that the chart was easy to read by adjusting the labels and adding a title. I also added percentage annotations on each slice to provide more insight into the data.

### Task 4:

#### Task Description: Risk
The task involves simulating a series of individual battle rounds from the board game Risk, specifically the battle between an attacker with 3 dice and a defender with 2 dice. The goal is to simulate 1000 battle rounds and analyze the outcome.

#### Task Solution:
The program learns how to simulate random dice rolls for both the attacker and the defender. It helps you practice random number generation, conditional logic, iteration, and data visualization. By simulating many rounds, you can observe and analyze the distribution of troop losses for both sides in a Risk battle. 
I used numpy for array manipulation and random number generation. I defined a standard 6-sided die and represemted the dice using a NumPy array, dice, containing values from 1 to 6. Then I used a function to simulate rolling the dice . It uses np.random.choice() to randomly select values from the dice array. I used n_battle = 1000 to set the number of battle rounds to simulate (1000 rounds). I used counters to track how many rounds the attacker wins, the defender wins, and how many rounds end in a tie. This loop runs 1000 times, simulating one battle round per iteration. Inside the loop, the variables attacker_wins and defender_wins are reset to 0 at the start of each round. In each battle round, the attacker rolls 3 dice and the defender rolls 2 dice, with both sets of rolls being sorted in descending order using np.sort() and then reversed to ensure the highest values are compared first. This sorting makes it easier to evaluate the dice values from highest to lowest. The code then checks if both the attacker and defender win at least one comparison, which would indicate a tie. If the defender doesn't win any comparisons, the attacker wins that round (attacker_total is incremented). Otherwise, the defender wins (defender_total is incremented).After all rounds are completed, the program prints the total number of wins for the attacker, defender, and ties. I visualised the data in a Pie Chart showings the proportion of wins for the attacker, defender, and ties. 
I found this task extremely difficult, I changed it several times before I found a solution that worked correctly and calculated only 1000 rounds.

### Task 5:

#### Task Description: Weather
The task is to create a python file or notebook called assignment_6_Weather (.py or .ipynb) by importing a csv file and plotting the data. 
#### Task Solution:

The purpose of this task is to work with weather data and perform basic data analysis and visualization using Python. YOu will analyze temperature data by calculating daily and monthly averages.Learn how to load, manipulate, and analyze time series data from a CSV file. Analyze temperature trends over time, including calculating daily mean temperatures and monthly averages.Use time series plotting techniques to visualize temperature changes over time, including the daily and monthly mean temperatures. It is designed to help develop skills in handling real-world data, performing aggregation, and using libraries like Pandas and Matplotlib to generate informative visualizations. 

I first pulled in the weather data from the provided URL using the Pandas library. I opened the file in Excel and identified the rows to skip. Afterward, I used pd.read_csv() to load the data, and selected only the relevant columns: "date", "temp", and "wdsp". Next, I converted the 'date' column into a proper datetime format using pd.to_datetime() to ensure that the dates were correctly parsed for time series analysis. I also renamed the columns to more readable names ("Date", "Temperature", "Wind Speed").
For the temperature task, I aimed to analyze the temperature data over time and visualize trends by year. To begin, I extracted the year and month from the 'Date' column and created separate columns for each, which will be useful for future analysis and grouping.
I added the 'year' and 'month' columns by using the .dt.year and .dt.month attributes of the Date column. This step makes it easier to group the data by year and month in future analyses.Next, I calculated the average temperature for each year by grouping the data by the 'year' column and then calculating the mean temperature for each group using groupby() and mean(). This aggregation allows me to focus on the yearly temperature trends without being overwhelmed by the daily fluctuations.
Finally, I printed the first few rows of the dataset to verify the addition of the 'year' and 'month' columns. This step sets up the data for plotting the temperature trends over the years.





## Prerequisites
- Python 3.x
- Anaconda
- Visual Studio Code
