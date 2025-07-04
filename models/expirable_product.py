from datetime import date
from .base_product import Product

class ExpirableProduct(Product):
	def __init__(self,name,price,quantity,expiry_date):
		super().__init__(name, price, quantity)
		self.expiry_date = expiry_date

	def is_expired(self) :

		return date.today() > self.expiry_date