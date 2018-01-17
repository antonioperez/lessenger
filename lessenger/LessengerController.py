import pprint

class LessengerParser:
    def __init__(self):
        pass

class LessengerController:
    
    def __init__(self, geoService, weatherService):
        self.geoService = geoService
        self.weatherService = weatherService
        self.city_search_key = "locality"

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

            lat = None
            lng = None
            for result in geocode_results:     
                location = result["geometry"]["location"]
                #shortcut to check for city location
                if self.city_search_key in result["types"]:
                    if "lat" in location and "lng" in location:
                        lat = location["lat"]
                        lng = location["lng"]
                        break
                #all else fails, search for component. Perhaps have other city indicator checks
                elif any(component for component in result["address_components"] if "locality" in component["types"]):
                    if "lat" in location and "lng" in location:
                        lat = location["lat"]
                        lng = location["lng"]
                        break
            if lat != None and lng != None:
                weather_data = self.weatherService.get_curr_weather_data(lat, lng)
                pp.pprint(weather_data.summary) 
                
        except Exception as err:
            print('Handling unknown error ', err)
        return geocode_result

    
    