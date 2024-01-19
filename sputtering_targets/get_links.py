import requests
from bs4 import BeautifulSoup

def get_links(url, file_path):
    try:
        # Perform the GET request on the URL
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Select all elements with the class 'h3 mb-4'
        elements_with_links = soup.select('.h3.mb-4 a[href]')  # Update the selector to find <a> tags within elements with class 'h3 mb-4'

        # Extract href attributes from the selected elements
        links = [elem['href'] for elem in elements_with_links]

        # Prepend the base URL if necessary and filter out None
        base_url = 'https://www.lesker.com'
        full_links = [base_url + link if not link.startswith('http') else link for link in links]

        # Write the extracted links to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            for link in full_links:
                file.write(link + '\n')

        print(f'All links extracted and saved to {file_path}')
        return True

    except requests.HTTPError as http_err:
        print(f'HTTP error occurred while retrieving {url}: {http_err}')
        return False
        
    except Exception as err:
        print(f'An error occurred while retrieving {url}: {err}')
        return False
    
    
    
    
