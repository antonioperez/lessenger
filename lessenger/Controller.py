from lessenger.GoogleGeo import LocationNotFound
from lessenger.DarkSky import WeatherDataError, WeatherTypeError
import datetime

class QueryRequired(Exception):
    pass

class LessengerController:
    """Control available services to parse data. 
       TO-DO: Add abstract class to keep service API consistent
       eg (switch out parsers)
    """
    def __init__(self, geoService, weatherService, parserService):
        self.geoService = geoService
        self.weatherService = weatherService
        self.parserService = parserService
        self.weather_data = None
        self.weather_time = datetime.datetime.now()
    
    def get_help_message(self):
        msg = """I hear you're interested in the weather! <br>
            Ask for the weather in any city <br>
            ex) weather in SF, what's the weather in Fresno, or LA weather"""
        return {
            "type": "rich",
            "html": msg
        }

    def get_greeting(self, name):
        greeting = "Hi {0}".format(name)
        return {
            "type": "text",
            "text": greeting
        }

    def get_error_message(self):
        msg = "I am sorry, I didn't understand your request."
        return {
            "type": "text",
            "html": msg
        }

    def get_response(self, query):
        response = {"type": "text", "text" : ""}
        try:
            self.get_weather(query)
            address = self.geoService.get_formatted_address()
            summary = self.weather_data.summary
            temperature = self.weather_data.temperature
            resp = "On {3} it'll be {0}F in {2}. {1}".format(temperature, summary, address, self.weather_time.strftime('%A %d'))
            response["text"] = resp

        except LocationNotFound as err:
            response["text"] = "Sorry! Location Not Found :("

        except QueryRequired as err:
            response = self.get_help_message()

        except WeatherDataError as err:
            response["text"] = "uh ohhh.. weather data not found. Try again!"

        except WeatherTypeError as err:
            response["text"] = "This type of weather data is not supported"


        return response

    def get_weather(self, query, weather_type = "currently"):
        query = query.lower().strip()
        if not query: 
            raise QueryRequired("Query can't be empty") 
        
        location = ""
        locations = ()
        
        if "weather in" in query:
            locations = self.parserService.parse(query, "weather in")
            if locations[1]:
                location = locations[1]
        elif "tomorrow in" in query:
            locations = self.parserService.parse(query, "tomorrow in")
            if locations[1]:
                location = locations[1]
                self.weather_time += datetime.timedelta(days=1)

        elif "weather tomorrow" in query:
            locations = self.parserService.parse(query, "weather tomorrow")
            if locations[0]:
                location = locations[0]
                self.weather_time += datetime.timedelta(days=1)
        elif "weather" in query:
            locations = self.parserService.parse(query, "weather")
            if locations[0]:
                location = locations[0]
            elif locations[1]:
                location = locations[1]
        else:
            location = query
        
        if location:
            self.geoService.search_location(location)
            coors_points = self.geoService.get_lat_lng()
            self.weather_data = self.weatherService.get_weather_data(coors_points, self.weather_time, weather_type)
            
        return self.weather_data    
    