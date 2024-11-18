import pandas as pd

# Uncomment lines as needed

# Change the file paths accordingly
input_file_path = 'raw_patent_data.csv' # e.g. 'C:/Users/user1/Desktop/raw_patent_data.csv'
output_file_path = 'cleaned_patent_data.csv' # e.g. 'C:/Users/user1/Desktop/cleaned_patent_data.csv'

# Read the file
df = pd.read_csv(input_file_path)

# only keep the needed columns
df = df[['title', 'abstract', 'number of independent claims', 'number of inventors', 
         'number of backward citations', 'average annual forward citations']]

# print("\nDirty dataset shape (rows, columns):", df.shape)
#print("\nMissing values in each column before:")
#print(df.isnull().sum())

# Drop rows with any missing values
df = df.dropna()

# Instead use this if you want to drop rows with a specific info missing 
# e.g. filter rows where 'claims' column has missing values
#missing_claims = df[df['number of independent claims'].isnull()]

#print("\nCleaned Dataset shape (rows, columns):", df.shape)
#print("\nMissing values in each column now:")
#print(df.isnull().sum())

# convert types if necessary
df['number of independent claims'] = df['number of independent claims'].astype(int)
#df['title'] = df['title'].astype(str)
#df['abstract'] = df['abstract'].astype(str)

# Standardize abstract text
# Remove extra whitespace, convert to lower case
# df['abstract'] = df['abstract'].str.strip()
# df['abstract'] = df['abstract'].str.lower()

df.to_csv(output_file_path, index=False)
print(f"Updated data saved to {output_file_path}")