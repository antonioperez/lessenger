import forecastio


class WeatherTypeError(Exception):
    pass

class WeatherDataError(Exception):
    pass

class DarkSkyService:

    def __init__(self, dark_sky_api_key):
        self.api_key = dark_sky_api_key
        self.forecast = None
        self.weather_types = [
            'currently', 'minutely', 'hourly', 'daily'
        ]
    
    def get_weather_data(self, gps_coor, time, weather_type = "currently"):
        weather_type = weather_type.lower()

        if len(weather_type) < 0 or weather_type not in self.weather_types:
            raise WeatherTypeError("Weather Type Not Valid: Must be 'currently' 'minutely' 'hourly' 'daily' ") 

        if "lat" in gps_coor and "lng" in gps_coor:
            loadedForecast = forecastio.load_forecast(self.api_key, gps_coor["lat"], gps_coor["lng"], time)
            if weather_type == "currently":
                self.forecast = loadedForecast.currently()

            elif weather_type == "minutely":
                self.forecast = loadedForecast.minutely()

            elif weather_type == "hourly":
                self.forecast = loadedForecast.hourly()

            elif weather_type == "daily":
                self.forecast = loadedForecast.daily()
        
        if self.forecast == None:
            raise WeatherDataError("Error Reading Weather Data")
            
        return self.forecast