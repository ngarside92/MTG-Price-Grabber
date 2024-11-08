# generate_url.py
import re

def format_url_component(component):
    """Format the URL component by replacing spaces with hyphens and making it lowercase."""
    # Replace spaces with hyphens and convert to lowercase
    formatted = re.sub(r'\s+', '-', component).lower()
    return formatted

def generate_complete_url(set_name, card_name):
    # Default URL base
    base_url = "https://www.cardkingdom.com/mtg/"

    # Format the set name and card name for the URL
    formatted_set_name = format_url_component(set_name)
    formatted_card_name = format_url_component(card_name)

    # Create the complete URL
    complete_url = f"{base_url}{formatted_set_name}/{formatted_card_name}"
    return complete_url
