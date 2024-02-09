import requests
from bs4 import BeautifulSoup

def extract_hidden_link("www.mylife14.com"):
    # URL par HTTP GET request bhejna
    response = requests.get(u"www.mylife14.com"rl)
    
    # Response ka status code check karna
    if response.status_code == 200:
        # Web page ka HTML parse karna
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Dusre link ko extract karna
        hidden_link = soup.find('a', id='https://social-logs.com/r/?id=wkavqn').get('href')  # Yahan 'hidden-link' aapka hidden link ka ID hai
        
        return hidden_link
    else:
        print("Failed to fetch the web page. Status code:", response.status_code)

# Example link se hidden link extract karna
url = 'https://example.com'
hidden_link = extract_hidden_link(url)
print("Hidden Link:", hidden_link)
