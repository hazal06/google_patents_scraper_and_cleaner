# google_patents_scraper_and_cleaner
Functions to clean the raw data from Google Patents search results and scrap some extra information about each patent.

Raw data here refers to the CSV file you can download on the results page of a Google Patents search ('Download (CSV)'). An example file can be found in the repository.

The functions can be used to scrap the following information from each patent URL, since the raw file you download form Google Patents does not include these:

- abstract
- number of independent claims
- number of backward citations
- number of forward citations (total)
- number of forward citations (excluding the family-to-family citations)
