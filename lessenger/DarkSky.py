import forecastio


class DarkSkyService:

    def __init__(self, dark_sky_api_key):
        self.api_key = dark_sky_api_key
    
    def get_weather_data(self, gps_coor):
        if "lat" in gps_coor and "lng" in gps_coor:
            forecast = forecastio.load_forecast(self.api_key, gps_coor["lat"], gps_coor["lng"])
            curr_cast = forecast.currently()
            return curr_cast
        return None