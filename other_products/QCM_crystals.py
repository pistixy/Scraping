import requests
from bs4 import BeautifulSoup

links = ["https://www.lesker.com/newweb/process_instruments/qcm-deposition-rate-monitoring-crystals.cfm"]

data = []
i = 1
for link in links:
    print("Links visited: (", i, "/", len(links), ")")
    i += 1
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for tbody in soup.findAll('tbody'):
            for row in tbody.findAll('tr'):
                cells = row.findAll('td')
                # Filter out empty strings
                row_data = [cell.text.strip() for cell in cells if cell.text.strip()]
                row_data.append(row_data[0].replace(',',''))
                row_data.pop(0)
                if row_data:
                    data.append(row_data)

# Writing data to file
with open('other_products/QCM_crystals.txt', 'w', encoding='utf-8') as file:
    file.write('Material,Frequency,Diameter,Cut,Electrode Pattern,Dispenser,Crystals per pack,Part Number, Price, Description\n')  
    for row_data in data:
        file.write(','.join(row_data) + '\n')

print('Data successfully written to file.')
