from bs4 import BeautifulSoup
import requests

# URL of the page
url = 'https://markets.ft.com/data/currencies/tearsheet/summary?s=EURUSD'

# Send a GET request to the page
response = requests.get(url)

# If the GET request is successful, the status code will be 200
if response.status_code == 200:
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the element containing the data you want to scrape
    # Replace 'element_class' with the actual class you're looking for
    data_elements = soup.find_all(class_='element_class')

    # Extract and print the data
    for element in data_elements:
        print(element.get_text().strip())
else:
    print("Failed to retrieve the webpage")

