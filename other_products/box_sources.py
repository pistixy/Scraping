import requests
from bs4 import BeautifulSoup

base_url = 'https://www.lesker.com'

links = ["https://www.lesker.com/newweb/evaporation_sources/box-sources-rechargeable-baffled-boxes.cfm",
         "https://www.lesker.com/newweb/evaporation_sources/box-sources-non-rechargeable-baffled-boxes.cfm",
         "https://www.lesker.com/newweb/evaporation_sources/box-sources-tantalum-box-heaters.cfm"]


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
with open('other_products/box_sources_covers.txt', 'w', encoding='utf-8') as box_sources_covers:
    box_sources_covers.write('Description,No. per Pack, Part Number,Price\n')  # Corrected header names and added newline
    for row_data in data:
        if len(row_data)<=5:
            box_sources_covers.write(','.join(row_data) + '\n')
print('Data successfully written to covers file.')

# Writing data to file
with open('other_products/box_sources_boxes.txt', 'w', encoding='utf-8') as box_sources_boxes:
    box_sources_boxes.write('Description,No. per Pack,Volts,Amps,Watts,Temp.,Plume direction, Weight, Part Number,Price\n')  # Corrected header names and added newline
    for row_data in data:
        if len(row_data) > 0:  # Check if the list is not empty
            if isinstance(row_data[0], str) and row_data[0].isdigit():  # Check if the first item is a string representation of a number
                row_data.insert(0, 'name')  # Insert 'name' at the beginning of the list
            box_sources_boxes.write(','.join(row_data) + '\n')
print('Data successfully written to boxes file.')



