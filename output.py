import openpyxl

def write_to_excel(complete_url, set_name, card_name, price, file_name="magic_cards.xlsx"):
    # Create a new workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    # Add headers to the Excel sheet
    sheet["A1"] = "Set Name"
    sheet["B1"] = "Card Name"
    sheet["C1"] = "Complete URL"
    
    # Write the variable values into the first row
    sheet["A2"] = set_name
    sheet["B2"] = card_name
    sheet["C2"] = price
    sheet["D2"] = complete_url
    
    # Save the workbook to a file
    workbook.save(file_name)
    print(f"Data saved to {file_name}")

