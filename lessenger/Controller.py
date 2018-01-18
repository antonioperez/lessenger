from lessenger.GoogleGeo import LocationNotFound, NoDataError

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
    
    def get_help_message(self):
        msg = """ I hear you're interested in the weather <br>
            ask for the weather in any location <br>
            ex) weather in SF, what's the weather in Fresno, LA weather"""
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
        

    def get_weather(self, query, weather_type = "daily"):
        query = query.lower().strip()
        if not query: 
            raise QueryRequired("Query can't be empty") 
        
        location = ""
        locations = ()
        weather_data = None
        if "weather in" in query:
            locations = self.parserService.get_location(query, "weather in")
            if locations[1]:
                location = locations[1]
        elif "weather" in query:
            locations = self.parserService.get_location(query, "weather")
            if locations[0]:
                location = locations[0]
            elif locations[1]:
                location = locations[1]
        else:
            location = query
        
        if location:
            self.geoService.search_location(location)
            coors_points = self.geoService.get_lat_lng()
            self.weather_data = self.weatherService.get_weather_data(coors_points, weather_type)
            
        return self.weather_data    
    