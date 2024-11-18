import pandas as pd

# Change the file path accordingly
file_path = 'patent_data.csv' # e.g. 'C:/Users/user1/Desktop/raw_patent_data.csv'

# Load the data to a dataframe
# 'skiprows=1' is needed if the first line in the data file is not the actual data
# i.e. in Google Patents raw CSV data file, first line shows what you searched for
# low_memory option is there to avoid mixed types, try removing if needed
patents_df = pd.read_csv(file_path, skiprows=1, low_memory=False)

# Display the first few rows
print("First few rows of the dataset:")
print(patents_df.head())
    
# Check the shape of the dataframe
print("\nDataset shape (rows, columns):", patents_df.shape)
    
# Display the column names
print("\nColumns in the dataset:")
print(patents_df.columns)

# Check the number of missing values in each column
print("\nMissing values in each column:")
print(patents_df.isnull().sum())

# Check data types of the columns
print("\nData types of each column:")
print(patents_df.dtypes)

# Display some statistics for the numerical columns (uncomment if wanted)
# print("\nBasic statistics for numerical columns:")
# print(patents_df.describe(include='all'))