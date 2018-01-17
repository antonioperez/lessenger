from lessenger.GoogleGeo import LocationNotFound, NoDataError
import pprint

class QueryRequired(Exception):
    pass

class LessengerParser:
    """Class to read and parse the users request
    """
    def __init__(self):
        pass

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
    
    def get_response():
        pass

    def get_weather(self, query):
        query = self.parserService.parse_location_query(query)        
        weather_data = None
        try:
            geocode_results = self.geoService.search_location(query)
            coors_points = self.geoService.get_lat_lng()
            weather_data = self.weatherService.get_weather_data(coors_points)

        except LocationNotFound as err:
            print(err)

        except NoDataError as err:
            print(err)
            
        return weather_data    
    