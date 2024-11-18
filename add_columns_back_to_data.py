# Use this code if after the data cleaning and processing, you want to include 
# some columns that you deleted in the initial cleaning

import pandas as pd

# Change the file paths accordingly
file_path_original = 'raw_patent_data.csv'
file_path_cleaned = 'cleaned_patent_data.csv'
file_path_output_merged = 'new_output_data.csv'

# Load the data
patents_df_original = pd.read_csv(file_path_original, skiprows=1, low_memory=False)
patents_df_cleaned = pd.read_csv(file_path_cleaned, low_memory=False)

# Change accordingly
column_to_add_back = 'assignee'
# Match the wanted feature to the correct row using the patent id
merged_df = pd.merge(patents_df_cleaned, patents_df_original[['id', column_to_add_back]], on='id', how='left')

# Save the merged dataframe to a new file
merged_df.to_csv(file_path_output_merged, index=False)
print(f"Updated data saved to {file_path_output_merged}")
