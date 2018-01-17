import pprint

class LessengerParser:
    def __init__(self):
        pass

class LessengerController:
    
    def __init__(self, geoService, weatherService):
        self.geoService = geoService
        self.weatherService = weatherService

    def parse_location_query(self, query):
        return query

    def parse_location_data(self):
        pass
        
    def get_weather(self, query):
        pp = pprint.PrettyPrinter(indent=4)
        query = self.parse_location_query(query)
        geocode_result = []
        try:
            geocode_results = self.geoService.query_geocode(query)
            coors_points = self.geoService.get_lat_lng()
            weather_data = self.weatherService.get_weather_data(coors_points)
            pp.pprint(weather_data.summary) 
            
        except Exception as err:
            print('Handling unknown error ', err)
        return geocode_result

    
    