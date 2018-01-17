import forecastio


class DarkSkyService:

    def __init__(self, dark_sky_api_key):
        self.api_key = dark_sky_api_key
    
    def get_curr_weather_data(self, lat, lng):
        forecast = forecastio.load_forecast(self.api_key, lat, lng)
        curr_cast = forecast.hourly()
        return curr_cast