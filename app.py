from flask import Flask, jsonify, request
from lessenger.Controller import Controller

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def lessenger_chatbot():
    
    response = jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
