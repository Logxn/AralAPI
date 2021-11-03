import requests

class Station:
	def __init__(self, input):
		self.id = input['id']
		self.name = input['name']
		self.latitude = input['lat']
		self.longitude = input['lng']
		self.address = input['address']
		self.city = input['city']
		self.state = input['state']
		self.postcode = input['postcode']
		self.country_code = input['country_code']
		self.telephone = input['telephone']
		self.facilities = input['facilities']
		self.products = input['products']
		self.opening_hours = input['opening_hours']
		self.open_status = input['open_status']
		self.site_brand = input['site_brand']
		self.watchlist_id = input['watchlist_id']
		self.website = input['website']
		
		# Since some endpoints dont provide full data for a gas station we need to fill out the blanks
		self.static_map_url = None
		self.fuel_pricing = None

		if not 'fuel_pricing' in input:
			self._get_missing_data()
		else:
			self.static_map_url = input['static_map_url']
			self.fuel_pricing = input['fuel_pricing']


	def _get_missing_data(self):
		request_url = f'https://tankstellenfinder.aral.de/api/v1/locations/{self.id}'
		r = requests.get(request_url)

		result = r.json()

		self.static_map_url = result['static_map_url']
		self.fuel_pricing = result['fuel_pricing']

	def is_open(self):
		return self.open_status == 'open' or self.open_status == 'twenty_four_hour'
