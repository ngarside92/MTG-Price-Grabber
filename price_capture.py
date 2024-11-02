import requests
from bs4 import BeautifulSoup
from generate_url import generate_complete_url

def main(complete_url):
    # URL of the card page
    #complete_url = generate_complete_url()
    url = complete_url 

    # Set up headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }

    # Send a request to fetch the HTML of the page
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check that the request was successful

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use the CSS path to find the price element
    price_element = soup.select_one("body.cardDetailView div#appWrapper div#ckmain.container.mainWrapper div#main.shopMain div.row.cardDetail div.shopMain div.col-md-4.cardDetailSub.addToCartSub div.addToCartWrapper ul.addToCartByType li.itemAddToCart.NM.active form.addToCartForm div.amtAndPrice span.stylePrice")

    # Extract the text (price) from the element, if it exists
    if price_element:
        price = price_element.get_text(strip=True)
        #print(f"Price:" + price)
        return price
    else:
        print("Price element not found.")
        return None