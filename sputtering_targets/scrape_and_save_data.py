import requests
from bs4 import BeautifulSoup

def scrape_and_save_data(file_input_path, file_output_path):
    # Open the file and read the lines into a list
    with open(file_input_path, 'r') as file:
        urls = file.read().splitlines()

    # Initialize a list to hold all rows of data
    all_data = []
    i=1
    for link in urls:
        try:

            # Perform the GET request on the current URL
            response = requests.get(link)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code

            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the 'tbody' within the table; this is where you want to extract the data
            tbody = soup.find('tbody')
            if tbody:
                # Assuming each row 'tr' contains the data of interest
                rows = tbody.find_all('tr')
                for row in rows:
                    # Extract the text from each row
                    text = row.get_text(separator=',', strip=True)  # Use a comma as separator between cells
                    all_data.append(text)
                print("link visited. ",i,"/",len(urls))
                i=i+1
            else:
                print(f"No data found in the table for URL: {link}")

        except requests.HTTPError as http_err:
            print(f'HTTP error occurred while retrieving {link}: {http_err}')
        except Exception as err:
            print(f'An error occurred while retrieving {link}: {err}')

    # Once all URLs have been processed, write to the file once
    with open(file_output_path, 'w', encoding='utf-8') as file:
        for data in all_data:
            # Write the text data to the file, each row on a new line
            file.write(data + '\n')

    print(f'All data extracted and saved to {file_output_path}')
    return True

