from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def convert_to_number(string_value):
    # Remove dots for thousand separator
    no_thousands = string_value.replace(".", "")
    # Replace comma with dot for decimal separator
    decimal_fixed = no_thousands.replace(",", ".")
    # Convert to float and format it as string again to remove trailing .0
    return str(decimal_fixed)

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL certificate errors


# Set path to chromedriver as per your configuration
webdriver_service = Service("C:/Users/User1/Dropbox/PhotonExport_Istvan/Scraping/precious_metals/chromedriver-win64/chromedriver.exe")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = 'https://sempsajp.com/especial-online/cotizacion-de-metales-preciosos/'

# Fetch the page
driver.get(url)

# Wait for the data to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table.sin-borde.cotizacion")))

# Now that the page is fully loaded, we can start scraping
table = driver.find_element(By.CSS_SELECTOR, "table.table.sin-borde.cotizacion")
rows = table.find_elements(By.TAG_NAME, "tr")
delimiter = " | "

table_list = []


# Start from the second row to skip the header
with open('precious_metals/metals_data.txt','w', encoding='utf-8') as file:
    table_list.append([' ','bid','ask'])
    file.write(delimiter.join(['','bid','ask']))
    file.write('\n')
    for row in rows[1:]:  # assuming the first row is the header
        row_list = []
        # Grab only the first four cells (METAL, BID, ASK, AM) of each row
        cells = row.find_elements(By.TAG_NAME, "td")[:4]
        for cell in cells[1:]:
            row_list.append(convert_to_number(cell.text))
        # Only append and write to the file if row_list is not empty
        if row_list:
            table_list.append(row_list)
            file.write(delimiter.join(row_list) + '\n')

# Close the browser        
driver.quit()

# Print the table list after closing the browser
print('Preious metal prices are: ', table_list)
