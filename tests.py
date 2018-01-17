
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


tests = [
    "SF", "Fresno, CA"
]

for test in tests:
    geocode_result = LessController.get_weather(test)
    #pp.pprint(geocode_result)

lat = 31.9685988
lng = -99.9018131

forecast = forecastio.load_forecast(DARK_SKY, lat, lng)
byHour = forecast.hourly()

print(byHour.summary)
print(byHour.icon)