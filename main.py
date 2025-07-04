from datetime import date

from models.customer import Customer
from models.cart import Cart
from models.expirable_product import ExpirableProduct
from models.shippable_product import Shippable
from services.checkout import CheckoutService

# ✅ Final concrete class: Shippable + Expirable
class ShippableExpirableProduct(ExpirableProduct, Shippable):
    def __init__(self, name, price, quantity, weight, expiry_date):
        ExpirableProduct.__init__(self, name, price, quantity, expiry_date)
        Shippable.__init__(self, weight)

# ✅ Concrete non-shippable product (scratch card)
class NonShippableExpirableProduct(ExpirableProduct):
    def is_shippable(self):
        return False

# ----------- Setup test data -------------------

# Products
cheese = ShippableExpirableProduct("Cheese", 100, 5, 0.2, date(2025, 7, 1))
biscuits = ShippableExpirableProduct("Biscuits", 150, 3, 0.7, date(2025, 8, 1))
scratch_card = NonShippableExpirableProduct("Scratch Card", 50, 10, date(2030, 1, 1))

# Customer
customer = Customer("Ahmed", 1000)

# Cart setup
cart = Cart()
cart.add(cheese, 2)
cart.add(biscuits, 1)
cart.add(scratch_card, 1)

# Checkout process
checkout_service = CheckoutService()
checkout_service.checkout(customer, cart)
