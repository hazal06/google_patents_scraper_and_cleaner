# Make sure functions_scrap_from_gp.py is in the same folder 
from functions_scrap_from_gp import scrape_abstract, scrape_claims, scrape_citations, extract_citation_count, scrape_cited_by, scrape_cited_by_excl_families 

# Following packages should already be imported when the functions from functions_scrap_from_gp.py is imported:
# import requests
# from bs4 import BeautifulSoup

import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Using the functions defined in the file 'functions_scrap_from_gp.py'

# Note: You may want to apply all the functions separately 
# and save the data in each step to avoid any loss (which is what I did)

# Also make sure you have a stable internet connection the whole time

# Change the file paths accordingly
input_file_path = 'patent_data.csv' # e.g. 'C:/Users/user1/Desktop/cleaned_data.csv'
output_file_path = 'updated_patent_data.csv'

# Load the data
df = pd.read_csv(input_file_path)

# Apply the scrape_abstract function to the 'result link' column and save tha abstracts under a new column 'abstract'
df['abstract'] = df['result link'].apply(scrape_abstract)

# Apply the scrape_abstract function similarly
df['number of independent claims'] = df['result link'].apply(scrape_claims)

# Apply the scrape_cited_by function similarly
df['cited by'] = df['result link'].apply(scrape_cited_by)

# Apply the scrape_citations function
# Note: Use ThreadPoolExecutor for faster runtime. 
# This can be used for all the other functions as well. 
with ThreadPoolExecutor(max_workers=10) as executor:
    df['number of backward citations'] = list(executor.map(scrape_citations, df['result link']))

# Save the dataframe with the new columns to a new CSV file
df.to_csv(output_file_path, index=False)
print(f"Updated data saved to {output_file_path}")