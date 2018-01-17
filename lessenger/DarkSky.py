import forecastio


class WeatherTypeError(Exception):
    pass

class WeatherDataError(Exception):
    pass

class DarkSkyService:

    def __init__(self, dark_sky_api_key):
        self.api_key = dark_sky_api_key
        self.weather_types = [
            'currently', 'minutely', 'hourly', 'daily'
        ]
    
    def get_weather_data(self, gps_coor, weather_type = "currently"):
        weather_type = weather_type.lower()
        ret_forecast = None
        if len(weather_type) < 0 or weather_type not in self.weather_types:
            raise WeatherTypeError("Weather Type Not Valid: Must be 'currently' 'minutely' 'hourly' 'daily' ") 

        if "lat" in gps_coor and "lng" in gps_coor:
            forecast = forecastio.load_forecast(self.api_key, gps_coor["lat"], gps_coor["lng"])
            if weather_type == "currently":
                ret_forecast = forecast.currently()

            elif weather_type == "minutely":
                ret_forecast = forecast.minutely()

            elif weather_type == "hourly":
                ret_forecast = forecast.hourly()

            elif weather_type == "daily":
                ret_forecast = forecast.daily()
        
        if ret_forecast == None:
            raise WeatherDataError("Error Reading Weather Data")
            
        return ret_forecast