import requests
from bs4 import BeautifulSoup
from generate_url import generate_complete_url

def main(complete_url):
    # URL of the card page
    #complete_url = generate_complete_url()
    url = complete_url #input("Enter the URL of the card page: ") #"https://www.cardkingdom.com/mtg/foundations/prideful-parent"

    # Set up headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }

    # Send a request to fetch the HTML of the page
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check that the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the full title in the <h1> tag
    title_element = soup.find("h1")

    # Extract and split the title if found
    if title_element:
        full_title = title_element.get_text(strip=True)
        set_name, card_name = map(str.strip, full_title.split(":"))
        #print(f"Set Name:" + set_name)
        #print(f"Card Name:" + card_name)
        return set_name, card_name
    else:
        print("Title element not found.")
        return None, None  # Return None if title not found