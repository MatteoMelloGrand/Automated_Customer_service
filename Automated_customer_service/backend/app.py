Created on Fri Aug  2 15:57:07 2024

@author: lenovo
"""

from groq import Groq # type: ignore
from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS  # For handling CORS
import os

app = Flask(__name__)
#CORS(app)  # Allow Cross-Origin requests
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/chat', methods = ['GET', 'POST'])
def chat():
    input_data = request.json
    input_message = input_data.get('message', '')
    with open('Input_LLM1.txt', 'r') as file:
        original_content = file.read()
    content1 = original_content + input_message 
    #content1 = file.read() #creating a variable with the text
    with open('Input_LLM.txt', 'w') as file:
        file.write(original_content)
    client = Groq(
    api_key="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",
)

    try:

        chat_completion = client.chat.completions.create( 
        messages=[
            {
                "role": "user",
                "content": content1,
            }
        ],
        model="llama-3.1-70b-versatile",
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



    
