import pandas as pd

# Change the file paths accordingly
input_file_path = 'raw_patent_data.csv' # e.g. 'C:/Users/user1/Desktop/raw_patent_data.csv'
output_file_path = 'cleaned_patent_data.csv' # e.g. 'C:/Users/user1/Desktop/cleaned_patent_data.csv'

# Read the file
patents_df = pd.read_csv(input_file_path, skiprows=1, low_memory=False)

# Remove duplicate rows (normally not needed for google patents data, but just in case)
patents_df.drop_duplicates(inplace=True)

# Drop columns that are not useful (adjust according to need)
columns_to_drop = ['priority date', 'representative figure link']
patents_df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Drop rows with any missing values
patents_df = patents_df.dropna()

# Standardize text data
# Remove extra whitespace, convert to lower case
patents_df['title'] = patents_df['title'].str.strip()
patents_df['inventor/author'] = patents_df['inventor/author'].str.strip()
patents_df['title'] = patents_df['title'].str.lower()
patents_df['inventor/author'] = patents_df['inventor/author'].str.lower()

# Display the first few rows of the cleaned dataframe
#print("Cleaned DataFrame:")
#print(patents_df.head())

# Check the shape and any remaining missing values
print("\nCleaned dataset shape (rows, columns):", patents_df.shape)
print("\nMissing values in each column:")
print(patents_df.isnull().sum())

# Save the cleaned data to a new file
patents_df.to_csv(output_file_path, index=False)
print(f"Updated data saved to {output_file_path}")

