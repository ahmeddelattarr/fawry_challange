
class Cart:
	def __init__(self):
		self.items = {}

	def add(self,product,quantity):
		try:
			# TODO: add negitave quantity validation
			if product.is_expired():
				print(f"[Warning] {product.name} is expired. Skipping.")
				return
			if quantity > product.quantity:
				print(f"[Warning] Not enough stock for {product.name}. Skipping.")
				return
			self.items[product] = quantity
		except Exception as e:
			print(f"[Error] Failed to add {product.name}: {e}")

	def is_empty(self):
		return len(self.items) == 0

	def get_subtotal(self):
		return sum(product.price* quantity for product, quantity in self.items.items())

	def get_shippable_items(self):
		return [(product, qty) for product, qty in self.items.items() if product.is_shippable()]

