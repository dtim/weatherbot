from geopy.geocoders import Nominatim
from yr.libyr import Yr


class ForecastService(object):
    def __init__(self, user_agent):
        self.user_agent = user_agent
        self.geolocator = Nominatim(user_agent=user_agent)

    def weather(self, location_name: str):
        forecast = None
        try:
            location = self.geolocator.geocode(location_name)
            if location:
                coordinates = (location.latitude, location.longitude, int(location.altitude))
                meteo = Yr(coordinates=coordinates, language_name="en")
                forecast = meteo.now(as_json=True)
        finally:
            return forecast
