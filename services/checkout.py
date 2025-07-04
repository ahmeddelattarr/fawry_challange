from models.shippable_product import shippable
from .shipping import ShippingService

class CheckoutService:
	def __init__(self):
		self.shipping_service = ShippingService()

	def checkout(self,customer,cart):
		if cart.is_empty():
			raise Exception("Cart is empty. Cannot proceed to checkout.")

		subtotal = cart.get_subtotal()
		shippable_items = cart.get_shippable_items()
		shipping= self.shipping_service.ship(shippable_items, cart) if shippable_items else 0
		total = subtotal + shipping

		if customer.balance < total:
			raise Exception("Insufficient balance to complete the purchase.")

		customer.balance -= total

		print("** Checkout receipt **")
		for product, quantity in cart.items.items():
			print(f"{quantity}x {product.name:12} {product.price * quantity}")
		print("----------------------")
		print(f"Subtotal         {subtotal}")
		print(f"Shipping         {shipping}")
		print(f"Amount           {total}")
		print(f"Remaining Balance: {customer.balance}")
