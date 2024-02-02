import requests
from bs4 import BeautifulSoup
from write_to_file import write_to_file 

import requests
from bs4 import BeautifulSoup
from write_to_file import write_to_file 

def extract_prices(url):
    prices = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all price information containers
        price_containers = soup.find_all('small')
        
        for container in price_containers:
            # Find the sup tag and get its text separately
            sup = container.find('sup')
            sup_text = ''
            if sup:
                sup_text = sup.get_text()
                # Detach the sup element from the tree to avoid duplicating the text
                sup.extract()
            
            # Now get the text of the small tag, without the sup part
            price = container.get_text(strip=True) +','+ sup_text
            prices.append(price)

    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

    return prices





# Example usage
url_to_scrape = 'https://www.msesupplies.com/collections/evaporation-materials?page=1&sort_by=title-ascending'  # Replace this with the actual URL
prices = extract_prices(url_to_scrape)
print(prices)

# Assuming the 'prices' list is already populated
file_path = 'D:\PhotonExport\Scraping\MSE\evaporation_materials\data\output.txt'  # Specify your desired file path
write_to_file(prices, file_path)
