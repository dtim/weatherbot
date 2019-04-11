from geopy.geocoders import Nominatim
from yr.libyr import Yr
import json


class ForecastService(object):
    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.geolocator = Nominatim(user_agent=user_agent)

    def weather(self, location_name: str):
        forecast = {}
        try:
            location = self.geolocator.geocode(location_name)
            if location:
                coordinates = (location.latitude, location.longitude, int(location.altitude))
                meteo = Yr(coordinates=coordinates, language_name="en")
                response = meteo.now(as_json=True)
                if response:
                    forecast = json.loads(response)
        finally:
            return forecast
