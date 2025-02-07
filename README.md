# CHPC Summer School 2025: Working with Data in Python

This repository contains Python code and a dataset used in the CHPC Summer School 2025 course focused on **working with data in Python**. The course covers various data manipulation, exploration, and analysis techniques using the **pandas** library.

## Project Overview

The goal of this project is to analyze a dataset related to a racing game and perform various data manipulation and cleaning tasks. The code demonstrates how to:
- Import and explore data
- Subset, filter, and sort the data
- Create new variables and modify existing ones
- Handle duplicates and missing values
- Visualize and analyze race performance metrics

## Dataset

The dataset used in this project is `RacingGameData.csv`. This dataset contains information on racing events, including:
- Track type
- Engine used
- Speed and performance metrics
- Race times and checkpoints

### Variables in the Dataset:
- `Track`: Type of racing track (e.g., "OvalTrack", "StraightTrack")
- `Engine`: Type of engine used in the race
- `TopSpeedReached`: Maximum speed reached during the race
- `FinishTime`: Time taken to complete the race
- `CheckPoint1`, `CheckPoint2`: Times at specific checkpoints in the race
- `CheckPoint2_66`: Indicates if the second checkpoint was passed in the first 66% of the race time

## Requirements

To run the Python scripts, you will need to have the following libraries installed:
- `pandas`

You can install them using `pip`:

```
pip install pandas
```

## How to Use the Code

Clone the repository to your local machine:
```
git clone https://github.com/yourusername/CHPC_Summer_School_2025.git
```
Change the working directory to where the dataset is located:
```
import os
os.chdir('path_to_directory')
```
Import the dataset into a pandas DataFrame:
```
import pandas as pd
racing = pd.read_csv('RacingGameData.csv')
```
Run the Python scripts to explore and analyze the dataset. The scripts perform the following tasks:

- Display basic information about the dataset (e.g., number of rows, columns, data types).
- Subset and filter the data based on track type, engine, and other criteria.
- Sort the dataset by performance metrics such as speed and finish time.
- Create new variables for analysis and recode existing variables.

## Key Code Features
- Data Exploration: Overview of dataset structure, number of observations, and data types.
- Data Subsetting: Filtering data based on specific criteria (e.g., race track type, engine type).
- Sorting Data: Sorting the dataset based on different performance metrics.
- Creating New Variables: New variables based on race data (e.g., time between checkpoints, speed performance).
- Handling Duplicates: Detecting and removing duplicate rows.

## Example Output
Here are some of the key outputs that the code will generate:

- First 5 rows of the dataset to check the structure.
- A subset of the dataset filtered by track type or engine type.
- Sorted dataset based on speed and finish time.
- A new variable categorizing races as "fast" or "slow".

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

If you wish to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please ensure that your code adheres to the style and conventions outlined in the existing scripts.

## Contact
For any questions or feedback, please reach out to Kenneth at kennethtebogo17@gmail.com





