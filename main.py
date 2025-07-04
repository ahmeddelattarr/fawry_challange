from datetime import date, timedelta
from models.customer import Customer
from models.cart import Cart
from models.expirable_product import ExpirableProduct
from models.shippable_product import Shippable
from services.checkout import CheckoutService

# Concrete Hybrid Product
class ShippableExpirableProduct(ExpirableProduct, Shippable):
    def __init__(self, name, price, quantity, weight, expiry_date):
        ExpirableProduct.__init__(self, name, price, quantity, expiry_date)
        Shippable.__init__(self, weight)

    def is_shippable(self):
        return True

# Non-shippable & non-expired
class NonShippableExpirableProduct(ExpirableProduct):
    def is_shippable(self):
        return False

# --- Define Products ---
expired_cheese = ShippableExpirableProduct("Expired Cheese", 100, 5, 0.2, date(2023, 1, 1))  # ❌ expired
cheese = ShippableExpirableProduct("Cheese", 100, 5, 0.2, date.today() + timedelta(days=10))  # ✅
biscuits = ShippableExpirableProduct("Biscuits", 150, 2, 0.7, date.today() + timedelta(days=30))  # ✅
tv = ShippableExpirableProduct("TV", 2000, 3, 3.0, date.today() + timedelta(days=90))  # ✅
scratch_card = NonShippableExpirableProduct("Scratch Card", 50, 10, date.today() + timedelta(days=500))  # ✅
out_of_stock = ShippableExpirableProduct("Empty Box", 10, 0, 0.1, date.today() + timedelta(days=10))  # ❌ no stock

# --- Define Customer ---
customer = Customer("Ahmed", 10000)

# --- Define Cart ---
cart = Cart()

# --- Try All Additions ---
products_to_test = [
    (expired_cheese, 1),
    (cheese, 2),
    (biscuits, 1),
    (tv, 3),
    (scratch_card, 1),
    (out_of_stock, 1),
    (biscuits, 10),
]

for product, qty in products_to_test:
    try:
        cart.add(product, qty)
    except Exception as e:
        print(f"[Warning] {product.name} not added: {e}")

# --- Checkout ---
checkout_service = CheckoutService()
try:
    checkout_service.checkout(customer, cart)
except Exception as e:
    print(f"[Error] Checkout failed: {e}")
