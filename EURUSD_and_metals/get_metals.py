from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("C:/Users/User1/Dropbox/PhotonExport_Istvan/Scraping/EURUSD_and_metals/chromedriver-win64/chromedriver.exe")

# Choose Chrome Browser 
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = 'https://sempsajp.com/especial-online/cotizacion-de-metales-preciosos/'

# Fetch the page
driver.get(url)

# Wait for the data to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table.sin-borde.cotizacion")))

# Open a file to write the results
with open('EURUSD_and_metals/metals_data.txt', 'w', encoding='utf-8') as file:
    # Now that the page is fully loaded, you can start scraping
    table = driver.find_element(By.CSS_SELECTOR, "table.table.sin-borde.cotizacion")
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            file.write(cell.text + ' | ')
        file.write('\n')  # Newline after each row

# Close the browser
driver.quit()
