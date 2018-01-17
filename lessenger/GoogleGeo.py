import googlemaps


class GoogleGeoService:

    def __init__(self, api_key):
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)
    
    def query_geocode(self, query):
        if len(query) < 1:
            return []
        
        geocode_result = self.gmaps.geocode(query)
        return geocode_result
        
    
    