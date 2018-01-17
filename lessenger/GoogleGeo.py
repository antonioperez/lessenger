import googlemaps

class LocationNotFound(Exception):
    pass

class GoogleGeoService:

    def __init__(self, api_key):
        self.city_search_key = "locality"
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)
        self.data = {}
    
    def search_location(self, location):
        if len(location) < 1:
            return []
        self.data = self.gmaps.geocode(location)
    
    def get_lat_lng(self):
        for result in self.data:     
            location = result["geometry"]["location"]
            """shortcut to check for city location
            search for address components if first city indicator fails"""
            if self.city_search_key in result["types"]:
                if "lat" in location and "lng" in location:
                    return location
            elif any(component for component in result["address_components"] if "locality" in component["types"]):
                if "lat" in location and "lng" in location:
                    return location

        raise LocationNotFound("Location Not Found")
        
    
    