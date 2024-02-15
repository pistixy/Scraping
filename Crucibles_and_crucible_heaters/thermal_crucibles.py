import requests
from bs4 import BeautifulSoup

base_url = 'https://www.lesker.com'

# Specific page URL
url = base_url + '/evaporation-sources.cfm?section=thermal-crucibles'


# Send a GET request to the page
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    a_tags = soup.findAll('a', class_="lesker-app-enabled")

    links = []
    bad_links = ["/newweb/evaporation_sources/evaporation_tempvspower.cfm?pgid=0",
                 "/newweb/evaporation_sources/evaporation_technicalnotes_1.cfm?pgid=0",
                 "/newweb/faqs/index.cfm?category=evaporation sources"]

    for a_tag in a_tags:
        href = a_tag.get('href')
        if href and href not in links and href not in bad_links:
            links.append(base_url + href)

    data = []
    i=1
    for link in links:
        print("Links visited: (",i,"/", len(links),")")
        i+=1
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.findAll('tr'):
                cells = row.findAll('td')
                # Filter out empty strings
                row_data = [cell.text.strip() for cell in cells if cell.text.strip()]
                if row_data:    
                    data.append(row_data)


    # Writing data to file
    with open('other_products/thermal_crucibles.txt', 'w', encoding='utf-8') as file:
        file.write('Description,Wall Thickness,Part Number,Price\n')  # Corrected header names and added newline
        for row_data in data:
            file.write(','.join(row_data) + '\n')



    print('Data successfully written to file.')

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
