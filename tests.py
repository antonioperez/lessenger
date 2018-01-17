
from lessenger.LessengerController import LessengerController
from lessenger.GoogleGeo import GoogleGeoService

import pprint


DARK_SKY = "8b4d5ca925446f9db4f7d7d0aac8b40c"
GMAPS_KEY = "AIzaSyD7W7v5psM8TDJwUV2WxsPkoYRtByh07Y0"


pp = pprint.PrettyPrinter(indent=4)


GeoService = GoogleGeoService(GMAPS_KEY)
LessController = LessengerController(GeoService)


tests = [
    "", "SF"
]

for test in tests:
    geocode_result = LessController.query_location(test)
    pp.pprint(geocode_result)

