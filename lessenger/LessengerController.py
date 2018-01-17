from lessenger.GoogleGeo import GoogleGeoService


class LessengerController:

    def __init__(self, geoService):
        
        self.geoService = geoService
    
    def query_location(self, query):
        
        geocode_result = self.geoService.query_geocode(query)
        return geocode_result

    
    