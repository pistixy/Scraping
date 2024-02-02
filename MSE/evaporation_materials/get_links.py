def get_links(base_url, start_page, end_page):
    page_urls = []
    for page_number in range(start_page, end_page + 1):
        # Construct the URL with the current page number
        page_url = f"{base_url[:-1]}{page_number}"
        page_urls.append(page_url)
    return page_urls


