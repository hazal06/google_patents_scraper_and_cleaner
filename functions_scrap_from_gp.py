import requests
from bs4 import BeautifulSoup
# from concurrent.futures import ThreadPoolExecutor

def scrape_abstract(url):
    """Scrape the patent abstract from the given Google patents URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            abstract_section = soup.find('section', itemprop='abstract')
            if abstract_section:
                return ' '.join(div.get_text(strip=True) for div in abstract_section.find_all('div', class_='abstract'))
            else:
                return None  # Leave entry empty in case an abstract is not found
        else:
            return None  # Leave entry empty in case the URL is not reachable
    except Exception:
        return None  # Leave entry empty in case of an exception


def scrape_claims(url):
    """Scrape the number of independent claims from the given Google patents URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
        
            # Find the main claims container
            claims_section = soup.find('div', class_='claims')
    
            # Count direct child claims with class 'claim' (independent claims)
            independent_claims = claims_section.find_all('div', class_='claim', recursive=False)
        
            number_of__independent_claims = len(independent_claims)
            return number_of__independent_claims
        else:
            return None
    except Exception:
        return None

def scrape_citations(url):
    """Scrape the number of citations (backward citations) in a patent from Google Patents"""
    session = requests.Session()
    try:
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            citation_num_1 = extract_citation_count(soup, 'Citations')
            citation_num_2 = extract_citation_count(soup, 'Family Cites Families')
            return citation_num_1 + citation_num_2
    except requests.RequestException:
        pass
    return None  # return None if the URL is not reachable

def extract_citation_count(soup, header_text):
    header = soup.find('h2', string=lambda x: x and header_text in x)
    if header:
        try:
            return int(header.get_text().strip().split('(')[1].replace(')', ''))
        except (IndexError, ValueError):
            return 0
    return 0

# Note:
# Use ThreadPoolExecutor for faster runtime. Like this:
# with ThreadPoolExecutor(max_workers=10) as executor:
#    df['number of backward citations'] = list(executor.map(scrape_citations, df['result link']))

def scrape_cited_by(url):
    """Scrape the number of forward citations ('cited by') of a patent from Google Patents."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            cited_by_header = soup.find('h2', string=lambda x: x and 'Cited By' in x)
            cited_by_header_f = soup.find('h2', string=lambda x: x and 'Families Citing this family' in x)
            if cited_by_header:
                # Extract the number from the text in the format "Cited By (number)"
                cited_by_number = cited_by_header.get_text().strip().split('(')[1].replace(')', '')
                cited_num_1 = int(cited_by_number)  # Return as integer
            else:
                cited_num_1 = 0  # Return 0 if "Cited By" section is not found
            if cited_by_header_f:
                # Extract the number from the text in the format "Cited By (number)"
                cited_by_number_2 = cited_by_header_f.get_text().strip().split('(')[1].replace(')', '')
                cited_num_2 = int(cited_by_number_2)  # Return as integer
            else:
                cited_num_2 = 0  # Return 0 if "Cited By" section is not found
            return cited_num_1 + cited_num_2
        else:
            return None  # Leave entry empty if page is not reachable
    except Exception:
        return None  # Leave entry empty in case of an exception


# If you do not want to include family-to-family forward citations, use this function instead.
def scrape_cited_by_excl_families(url):
    """Scrape the number of forward citations ('cited by') of a patent from Google Patents,
    excluding the Family-to-Family citations."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            cited_by_header = soup.find('h2', string=lambda x: x and 'Cited By' in x)
            if cited_by_header:
                cited_by_number = cited_by_header.get_text().strip().split('(')[1].replace(')', '')
                return int(cited_by_number)  # Return as integer
            else:
                return 0
        else:
            return None
    except Exception:
        return None