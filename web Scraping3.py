import requests
from bs4 import BeautifulSoup

def scrape_walmart(search_query):
    # Walmart ke search URL
    url = f'https://www.walmart.com/search/?query={search_query}'

    # URL par HTTP GET request bhejna
    response = requests.get(url)

    # Response ka status code check karna
    if response.status_code == 200:
        # Web page ka HTML parse karna
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Products ki listing ka container element ko dhoondna
        products_container = soup.find('div', class_='search-result-gridview-items')

        if products_container:
            # Products ki listing se individual product elements ko extract karna
            products = products_container.find_all('div', class_='search-result-gridview-item')

            # Har product ka data extract karna aur print karna
            for product in products:
                product_title = product.find('a', class_='product-title-link').text.strip()
                product_price = product.find('span', class_='price').text.strip()
                print("Product:", product_title)
                print("Price:", product_price)
                print("----------------------")
        else:
            print("Products container not found.")
    else:
        print("Failed to fetch Walmart search results. Status code:", response.status_code)

# Scraping ke liye search query ka istemal karein
search_query = 'laptop'  # Example: laptop, headphones, shoes, etc.
scrape_walmart(search_query)

