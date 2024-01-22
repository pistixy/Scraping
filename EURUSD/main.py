import requests
from bs4 import BeautifulSoup

# URL of the page
url = 'https://markets.ft.com/data/currencies/tearsheet/summary?s=EURUSD'

# Send a GET request to the page
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, 'html.parser')

    a_tag = soup.find('a', class_="mod-ui-link", href="/data/currencies/tearsheet/summary?s=eurusd")
    print(a_tag)
    
    EURUSD=a_tag.get_text()
   
    
    with open('EURUSD/EURUSD.txt', 'w', encoding='utf-8') as file:
        file.write(EURUSD)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
