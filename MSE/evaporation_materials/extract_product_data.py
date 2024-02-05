import requests
from bs4 import BeautifulSoup

def extract_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'An error occurred: {err}')  # Python 3.6
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []

        # Find all divs with class 'grid-item large--one-quarter medium--one-third small--one-half'
        product_divs = soup.find_all('div', class_='grid-item large--one-quarter medium--one-third small--one-half')
        

        for div in product_divs:
            product_info = div.find('p')
            price_info = div.find('small')
            sup = price_info.find('sup')
            sup_text = ''
            if sup:
                sup_text = sup.get_text()
                # Detach the sup element from the tree to avoid duplicating the text
                sup.extract()
            
            # Now get the text of the small tag, without the sup part
            price = price_info.get_text(strip=True) +'.'+ sup_text
            

            if product_info and price_info:
                product_text = product_info.get_text(strip=True)
                products.append({'description': product_text, 'price': price})

                
        
        return products