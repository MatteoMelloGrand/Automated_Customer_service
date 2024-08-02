# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:57:07 2024

@author: lenovo
"""

import replicate
import Front
from flask import Flask, request, jsonify
from flask_cors import CORS  # For handling CORS
import os


app = Flask(__name__)
CORS(app)  # Allow Cross-Origin requests

API_TOKEN = "your_API_token" #?

@app.route('/chat', methods = ['POST'])
def chat():
    input_data = request.json
    input_message = input_data.get('message', '')
    with open('Input_LLM.txt','a+') as file: #reading the file and adding the question
        file.write(f"Reply to the following client message: {input1}\n")
        file.seek(0)
        content = file.read() #creating a variable with the text

    client = replicate.Client(token="your_API_token") #creation of the variable containing the token
    try:
        response = client.models.get("meta/meta-llama-3-70b-instruct").predict(prompt=content) #creation of the response

        output = response.get("output", "")
        if output.endswith("..."):
            print("Response incomplete. Notifying customer service.")

        return jsonify({'response': output})
            #write an email to the customer service with the question saying to enter the platform and reply as soon as possible
    except Exception as e:
        print(f"An error occured. Please try again. {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)