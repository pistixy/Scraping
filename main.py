from format_data import format_data
from process_data import process_data
from process_and_append_data import process_and_append_data
from get_links import get_links
from scrape_and_save_data import scrape_and_save_data
from append_data import process_data2, append_data



if __name__ == "__main__":
    # Code here will only execute when the module is run directly, not when imported
    url = 'https://www.lesker.com/materials-division.cfm?section=sputtering-targets'
    extracted_links="D:/PhotonExport/Scraping/data/extracted_links.txt"
    raw_data="D:/PhotonExport/Scraping/data/raw_data.txt"
    formatted_data="D:/PhotonExport/Scraping/data/formatted_data.txt"
    formatted_correct_data="D:/PhotonExport/Scraping/data/formatted_correct_data.txt"
    formatted_incorrect_data="D:/PhotonExport/Scraping/data/formatted_incorrect_data.txt"
    final_data="D:/PhotonExport/Scraping/data/final_data.txt"
    temp_processed_data= "D:/PhotonExport/Scraping/data/temp_processed_data.txt"
    get_links(url, extracted_links)
    scrape_and_save_data(extracted_links, raw_data)
    format_data(raw_data, formatted_data)
    process_data(formatted_data, formatted_correct_data, formatted_incorrect_data)
    process_data2(formatted_incorrect_data, temp_processed_data)
    append_data(temp_processed_data, formatted_correct_data)



 

