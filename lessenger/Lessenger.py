from lessenger.GoogleGeo import LocationNotFound, NoDataError
import re
import pprint

class QueryRequired(Exception):
    pass

class LessengerParser:
    """Class to read and parse the users request
    """

    def get_location(self, query, indicator):
        query = query.lower().strip()
        words = query.split()

        if len(words) == 1:
            return tuple(words)
  
        reg_word = r"\W*([\w]*)"
        regex = r"{}\W*{}{}".format(reg_word,indicator,reg_word)
        pattern = re.compile(regex)
        matches = re.search(pattern, query)
        if matches:
            return matches.groups()
        return ()

class LessengerController:
    """Control available services to parse data. 
       TO-DO: Add abstract class to keep service API consistent
       eg (switch out parsers)
    """
    def __init__(self, geoService, weatherService, parserService):
        self.geoService = geoService
        self.weatherService = weatherService
        self.parserService = parserService
    
    def get_response(self, query):
        pass

    def get_weather(self, query):
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
            geocode_results = self.geoService.search_location(location)
            coors_points = self.geoService.get_lat_lng()
            weather_data = self.weatherService.get_weather_data(coors_points)
            
        return weather_data    
    