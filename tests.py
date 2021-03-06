
from lessenger.Controller import LessengerController
from lessenger.Parser import LessengerParser
from lessenger.GoogleGeo import GoogleGeoService
from lessenger.DarkSky import DarkSkyService

import forecastio
import pprint


DARK_SKY = "8b4d5ca925446f9db4f7d7d0aac8b40c"
GMAPS_KEY = "AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0"

pp = pprint.PrettyPrinter(indent=4)

geo_service = GoogleGeoService(GMAPS_KEY)
weather_service = DarkSkyService(DARK_SKY)
request_parser = LessengerParser()
lessenger_control = LessengerController(geo_service, weather_service, request_parser)

test_inputs = [
    "What's the weather tomorrow in Fresno", 
    "weather tomorrow in 93722",
    "Fresno"
]

for query in test_inputs:
    geocode_result = lessenger_control.get_response(query)
    if geocode_result:
        pp.pprint(geocode_result)
        print("\n")
