
class Cart:
	def __init__(self):
		self.items = {}

	def add(self,product,quantity):
		if product.is_expired():
			raise Exception(f"{product.name} is expired and cannot be added to the cart.")
		if quantity > product.quantity:
			raise Exception(f"Cannot add {quantity} of {product.name}. Only {product.quantity} available.")

		self.items[product]=quantity

	def is_empty(self):
		return len(self.items) == 0

	def get_subtotal(self):
		return sum(product.price* quantity for product, quantity in self.items.items())

	def get_shippable_items(self):
		return [(product, qty) for product, qty in self.items.items() if product.is_shippable()]

