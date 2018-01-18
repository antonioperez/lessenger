import googlemaps

class LocationNotFound(Exception):
    pass

class GoogleGeoService:

    def __init__(self, api_key):
        self.city_search_key = "locality"
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)
        self.data = {}
        self.active_location = {}

    def get_region(self):
        if self.active_location["address_components"]:
            city = state = country = ""
            for compon in self.active_location["address_components"]:
                if "locality" in compon["types"]:
                    city = compon["short_name"]
                elif "administrative_area_level_1" in compon["types"]:
                    state = compon["short_name"]
                elif "country" in compon["types"]:
                    country = compon["short_name"]

            addr = "{0}, {1} {2}".format(city,state,country)
            return addr
        raise LocationNotFound("Region Not Found")

    def get_formatted_address(self):
        if "formatted_address" in self.active_location:
            return self.active_location["formatted_address"]

        raise LocationNotFound("Address Not Found")
    
    def search_location(self, location):
        if len(location) < 1:
            return []
        self.data = self.gmaps.geocode(location)
    
    def get_lat_lng(self):
        """
        Check for city key in result types.
        search for address components if first city indicator fails
        """

        if len(self.data) < 1: 
            raise LocationNotFound("No Active Data")

        for result in self.data:     
            location = result["geometry"]["location"]
            if self.city_search_key in result["types"]:
                if "lat" in location and "lng" in location:
                    self.active_location = result
                    return location
            elif any(component for component in result["address_components"] if "locality" in component["types"]):
                if "lat" in location and "lng" in location:
                    self.active_location = result
                    return location

        raise LocationNotFound("Location Not Found")
        
    
    