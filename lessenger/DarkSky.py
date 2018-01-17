

class DarkSkyService:

    def __init__(self, api_key):
        self.api_key = api_key
        self.gmaps = googlemaps.Client(key=api_key)


    