import googlemaps


class GoogleGeoService:

    def __init__(self, api_key):
        self.city_search_key = "locality"
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)
        self.data = {}
    
    def query_geocode(self, query):
        if len(query) < 1:
            return []

        self.data = self.gmaps.geocode(query)
    
    def get_lat_lng(self):

        for result in self.data:     
            location = result["geometry"]["location"]
            #shortcut to check for city location
            if self.city_search_key in result["types"]:
                if "lat" in location and "lng" in location:
                    return location
            #all else fails, search for component. Perhaps have other city indicator checks
            elif any(component for component in result["address_components"] if "locality" in component["types"]):
                if "lat" in location and "lng" in location:
                    return location
                
            return None
        
    
    