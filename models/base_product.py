from abc import ABC, abstractmethod

class Product (ABC):
	"""
	Abstract base class for a product.
	Defines the interface that all concrete products must implement.
	"""

	def __init__(self, name: str, price: float, quantity: int):
		self.name = name
		self.price = price
		self.quantity = quantity


	@abstractmethod
	def is_expired(self) -> bool:

		return False

	@abstractmethod
	def is_shappable(self) -> bool:

		return False