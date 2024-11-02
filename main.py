# main_script.py
import title_capture
import price_capture
from output import write_to_excel

def process_url(complete_url):
    # Extract set_name and card_name from the title on the page
    set_name, card_name = title_capture.main(complete_url)

    # Extract price from the page
    price = price_capture.main(complete_url)

    # Check if title extraction was successful
    if set_name and card_name:
        # Write the data to Excel
        write_to_excel(complete_url, set_name, card_name, price)
        
        # Return the data for Flask to use
        return {"set_name": set_name, "card_name": card_name, "price": price, "url": complete_url}
    else:
        return {"error": "Failed to extract set name and card name."}
