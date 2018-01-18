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

    def parse_location_query(self, query):
        query = query.lower().strip()
        if not query: 
            raise QueryRequired("Query can't be empty")        
        return query




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

    def get_weather(self, location):
        query = self.parserService.parse_location_query(location)        
        weather_data = None
        try:
            geocode_results = self.geoService.search_location(location)
            coors_points = self.geoService.get_lat_lng()
            weather_data = self.weatherService.get_weather_data(coors_points)

        except LocationNotFound as err:
            print(err)

        except NoDataError as err:
            print(err)
            
        return weather_data    
    