# app.py
from flask import Flask, request, jsonify, render_template
from generate_url import generate_complete_url
from main import process_url  # Ensure this is the correct import path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get data from the form
    set_name = request.form['set_name']
    card_name = request.form['card_name']
    
    # Generate the URL with the provided set name and card name
    complete_url = generate_complete_url(set_name, card_name)
    
    # Call the function to process the URL and get the results
    result = process_url()
    result["url"] = complete_url  # Include the generated URL in the result
    
    # Render the output using an HTML template
    return render_template('result.html', **result)


if __name__ == '__main__':
    app.run(debug=True)
