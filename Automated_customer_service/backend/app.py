# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:57:07 2024

@author: lenovo
"""

from groq import Groq # type: ignore
from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS  # type: ignore # For handling CORS
import os


app = Flask(__name__)
CORS(app)  # Allow Cross-Origin requests

#API_TOKEN = "your_API_token" #?

@app.route('/chat', methods = ['POST'])
def chat():
    input_data = request.json
    input_message = input_data.get('message', '')
    with open('Input_LLM.txt','a+') as file: #reading the file and adding the question
        file.write(f"Reply to the following client message: {input_message}\n")
        file.seek(0)
        content = file.read() #creating a variable with the text

    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
    try:
        chat_completion = client.chat.completions.create( 
        messages=[
            {
                "role": "user",
                "content": f"{content}",
            }
        ],
        model="llama3-groq-70b-8192",
        )
        output = chat_completion.choices[0].message.content
        if output.endswith("..."):
            print("Response incomplete. Notifying customer service.")

        return jsonify({'response': output})
            #write an email to the customer service with the question saying to enter the platform and reply as soon as possible
    except Exception as e:
        print(f"An error occured. Please try again. {e}")
        return jsonify({'error': 'An error occurred. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)