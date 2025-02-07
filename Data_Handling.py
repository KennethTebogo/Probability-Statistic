# CHPC Summer School 2025
# Working with data in Python

# Import packages
import pandas as pd
import os

# Change the file path to where the data is located on your device
os.chdir(r"/home/ironman/Desktop/Python/Probability_Statistic")

#%% 
# Import the data
racing = pd.read_csv("RacingGameData.csv")

#%% 
# Obtain the variable names included in the data set
print("Variable Names:", list(racing))

# Obtain the number of observations
print("Number of rows:", racing.shape[0])

# Obtain the number of columns
print("Number of columns:", racing.shape[1])

# Obtain the data types of each column
print("Data Types:", racing.dtypes)

#%% 
# Display the first 5 observations in the data set
print("First 5 observations:")
print(racing.head())

# Display the first 10 observations in the data set
print("First 10 observations:")
print(racing.head(10))

#%% 
# Extract the racing tracks column
tracks = racing["Track"]

# Show the unique values in the racing tracks column
track_types = racing["Track"].unique()
print("Unique Track Types:", track_types)

#%% 
# Extract row 5 of the data set
print("Row 5 of the dataset:")
print(racing.iloc[4])

# Extract the 5th, 7th and 10th row of the dataset.
print("Rows 5, 7, and 10 of the dataset:")
print(racing.iloc[[4, 6, 9]])

#%% 
# Subset the data set to only contain the races on the "OvalTrack"
racing_oval = racing.loc[racing["Track"] == "OvalTrack", :]
print("Races on the OvalTrack:")
print(racing_oval.head())

# Subset the data set to only contain the races on either the "StraightTrack" 
# or the "OvalTrack"
tr = ["StraightTrack", "OvalTrack"]
racing_oval_straight = racing.loc[racing["Track"].isin(tr), :]
print("Races on either the StraightTrack or OvalTrack:")
print(racing_oval_straight.head())

# Subset the data set to only contain the races on the "OvalTrack" and
# the car that had a "Bayes" engine
racing_oval_bayes = racing.loc[(racing["Track"] == "OvalTrack") & 
                               (racing["Engine"] == "Bayes"), :]
print("Races on OvalTrack with Bayes engine:")
print(racing_oval_bayes.head())

#%% 
# Sort the dataset by "TopSpeedReached" in ascending order
racing_sorted = racing.sort_values(by=['TopSpeedReached'])
print("Dataset sorted by TopSpeedReached (ascending):")
print(racing_sorted.head())

# Sort the dataset by "TopSpeedReached" in ascending order and then by 
# "FinishTime" in descending order.
racing_sorted2 = racing.sort_values(by=['TopSpeedReached', 'FinishTime'],
                                    ascending=[True, False])
print("Dataset sorted by TopSpeedReached (ascending) and FinishTime (descending):")
print(racing_sorted2.head())

#%% 
# Remove the "TopSpeedReached" column
racing_2 = racing.drop("TopSpeedReached", axis=1)
print("Dataset after removing TopSpeedReached column:")
print(racing_2.head())

# Remove the last 10 observations
racing_reduced = racing[:-10]
print("Dataset after removing the last 10 observations:")
print(racing_reduced.head())

#%% 
# Create a new variable in the racing dataset called "CheckPoint1to2" 
# which will contain the time it took to go from checkpoint 1 to  
# checkpoint 2.
racing["CheckPoint1to2"] = racing["CheckPoint2"] - racing["CheckPoint1"]
print("Dataset with CheckPoint1to2 variable:")
print(racing.head())

#%% 
#The variable "CheckPoint2_66" contains a 1 if checkpoint 2 was passed 
# within the first 66% of the completed race time  and a value of 0 if 
# this is not the case.
# Recode this variable to contain the words "yes" and "no"

# Create a dictionary
to_replace = {1: "Yes", 0: "No"}
racing["CheckPoint2_66"] = racing["CheckPoint2_66"].replace(to_replace)
print("Dataset with recoded CheckPoint2_66 variable:")
print(racing.head())

#%% 
# Create a new variable in the racing data set based on the "FinishTime" variable"
# If FinishTime > 25, the new variable display "slow"
# If FinishTime <= 25, the new variable display "fast"

def slow_fast(time):
    if time > 25:
        return "slow"
    else:
        return "fast"

racing["Indicator"] = racing["FinishTime"].apply(slow_fast)

print("Dataset with Indicator variable:")
print(racing.head())

#%% 
# Print all the duplicated rows
duplicates = racing.duplicated(keep=False)
print("Duplicated Rows:")
print(racing[duplicates])

# Remove the duplicated rows (but one of the rows should be kept in the 
# data frame)
no_dups = racing.drop_duplicates(keep="first")
print("Dataset after removing duplicates:")
print(no_dups.head())

