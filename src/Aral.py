import requests
from src.Exceptions import *
from src.Station import *

class Aral:
	def __init__(self):
		self.base_url = 'https://tankstellenfinder.aral.de/api/v1/locations/'
		self.nearest_url = self.base_url + 'nearest_to?'

	def _get_lat_lon(self, postal_code, country):
		geocode_url = 'https://nominatim.openstreetmap.org/search/?postalcode='
		request_url = geocode_url + f'{postal_code}&country={country}&format=jsonv2'

		r = requests.get(request_url)

		if r.status_code != 200:
			print("Unknown Error")

		if not r.json():
			return []

		result = r.json()[0]
		keys = ['lat', 'lon']

		return [result[k] for k in keys]

	'''
	Finds gas stations with provided postal code

	'''
	def find_nearest_gasstation(self, postal_code, country="de"):
		resp = self._get_lat_lon(postal_code, country)
		
		if not resp:
			raise SystemExit(UnknownPostalCodeException)

		lat = resp[0]
		lon = resp[1]

		request_url = self.nearest_url + f'lat={lat}&lng={lon}&limit=1&autoload=true&travel_mode=driving&avoid_tolls=false&avoid_highways=false&show_stations_on_route=true&corridor_radius=5&format=json'

		r = requests.get(request_url)

		# Error handling might be useful here?

		gas_station = Station(r.json()[0])
		return gas_station

