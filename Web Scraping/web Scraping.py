import requests
from bs4 import BeautifulSoup

# Wikipedia article ka URL
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# URL par HTTP GET request bhejna
response = requests.get(url)

# Response ka status code check karna
if response.status_code == 200:
    # Web page ka HTML parse karna
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Article ka title extract karna
    title = soup.find('h1', {'id': 'firstHeading'}).text
    print("Wikipedia Article Title:", title)

    # Article ke details extract karna
    details_paragraphs = soup.find('div', {'id': 'mw-content-text'}).find_all('p')
    details = '\n'.join([para.text for para in details_paragraphs])
    print("\nWikipedia Article Details:\n", details)
else:
    print("Failed to fetch the Wikipedia article. Status code:", response.status_code)
