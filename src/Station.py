
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

	def is_open(self):
		return self.open_status == 'open'
