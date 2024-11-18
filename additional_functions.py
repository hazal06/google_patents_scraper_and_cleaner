import pandas as pd

def calculate_average_annual_forward_citations(df):
    """Calculate average annual forward citations and add it as a new column."""
    current_year = 2024
    df['average annual forward citations'] = df['cited by'] / (current_year - pd.to_datetime(df['publication date']).dt.year)
    return df

def count_number_of_inventors(df):
    """Count number of inverntors/authors and add it as a new column."""
    df['number of inventors'] = df['inventor/author'].apply(lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)
    return df


# Example use:

# Change the paths accordingly
input_file_path = 'patent_data.csv' # e.g. 'C:/Users/user1/Desktop/patent_data.csv'
output_file_path = 'updated_patent_data.csv'  # e.g. 'C:/Users/user1/Desktop/updated_patent_data.csv'

# Load the data to a dataframe
df = pd.read_csv(input_file_path)

# Apply the function calculate_average_annual_forward_citations
df_updated = calculate_average_annual_forward_citations(df)
print("Column 'average annual forward citations' was added.")

# Apply the function count_number_of_inventors
df_updated_2 = count_number_of_inventors(df)                                                 
print("Column 'number of inventors' was added.")

# Save the final dataframe to a new file
df_updated_2.to_csv(output_file_path, index=False)
print(f"Updated data is saved to {output_file_path}")