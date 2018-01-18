from flask import Flask, jsonify, request
from flask_cors import CORS

from lessenger.Controller import LessengerController
from lessenger.Parser import LessengerParser
from lessenger.GoogleGeo import GoogleGeoService
from lessenger.DarkSky import DarkSkyService

DARK_SKY = "8b4d5ca925446f9db4f7d7d0aac8b40c"
GMAPS_KEY = "AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0"

APP = Flask(__name__)
CORS(APP)

@APP.route("/chat/messages", methods=['POST'])
def lessenger_chatbot():
    geo_service = GoogleGeoService(GMAPS_KEY)
    weather_service = DarkSkyService(DARK_SKY)
    request_parser = LessengerParser()
    lessenger_control = LessengerController(geo_service, weather_service, request_parser)
    
    data = {
        "messages" : []
    }
    request_form = request.form
    action = request_form.get("action")

    if action == "message" and "text" in request_form:
        message = request_form.get("text")
        data["messages"].append(lessenger_control.get_response(message))
    
    elif action == 'join' and 'name' in request_form:
        name = request_form.get("name")
        greeting = lessenger_control.get_greeting(name)
        helper = lessenger_control.get_help_message()
        data["messages"].append(greeting)
        data["messages"].append(helper)

    else:
        error = lessenger_control.get_error_message()
        helper = lessenger_control.get_help_message()
        data["messages"].append(error)
        data["messages"].append(helper)

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == '__main__':
    APP.run(port=9000, debug=True)