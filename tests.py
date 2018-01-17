
from lessenger.LessengerController import LessengerController
from lessenger.GoogleGeo import GoogleGeoService
from lessenger.DarkSky import DarkSkyService

import forecastio
import pprint


DARK_SKY = ""
GMAPS_KEY = ""


pp = pprint.PrettyPrinter(indent=4)


GeoService = GoogleGeoService(GMAPS_KEY)
WeatherService = DarkSkyService(DARK_SKY)
LessController = LessengerController(GeoService, WeatherService)


test_inputs = [
    "SF", "Fresno, CA"
]

for inputs in test_inputs:
    geocode_result = LessController.get_weather(inputs)
    #pp.pprint(geocode_result)

lat = 31.9685988
lng = -99.9018131

forecast = forecastio.load_forecast(DARK_SKY, lat, lng)
byHour = forecast.hourly()

print(byHour.summary)
print(byHour.icon)