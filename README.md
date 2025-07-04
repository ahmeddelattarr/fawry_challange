---

## Fawry Quantum Internship Challenge – E-commerce System

This repository is a solution to the fawry assesment .

---

## Features Implemented

* Define products with:

  * Name, price, quantity
  * Optional expiry
  * Optional shipping weight
* Add products to a cart with quantity checks.
* Reject expired or out-of-stock items.
* Calculate:

  * Order subtotal
  * Shipping fees based on weight
  * Final total
  * Updated customer balance
* Generate a shipment notice for shippable items.
* Raise appropriate exceptions when:

  * Cart is empty
  * Insufficient customer balance
  * Expired product or insufficient stock

---



## Folder Structure

```
fawry_challange/
│
├── main.py                      # Main entry point
├── models/
│   ├── base_product.py          # Abstract base Product class
│   ├── expirable_product.py     # Products with expiry dates
│   ├── shippable_product.py     # Shippable mixin class
│   ├── cart.py                  # Cart logic
│   ├── customer.py              # Customer with balance
│
├── services/
│   ├── checkout.py              # Handles checkout process
│   ├── shipping.py              # Handles shipping calculation
```

---

## How to Run

```bash
cd fawry_challange
python main.py
```

You will see the console output that includes:

* Shipment Notice (for shippable items)
* Checkout Receipt
* Warnings for invalid operations (like expired or out-of-stock items)

---

## Sample Output

```
[Warning] Expired Cheese is expired. Skipping.
[Warning] Not enough stock for Empty Box. Skipping.
[Warning] Not enough stock for Biscuits. Skipping.

** Shipment notice **
2x Cheese       400g
1x Biscuits     700g
3x TV           9000g
Total package weight 10.1kg

** Checkout receipt **
2x Cheese       200
1x Biscuits     150
3x TV           6000
1x Scratch Card 50
----------------------
Subtotal         6400
Shipping         303.0
Amount           6703.0
Remaining Balance: 3297.0
```

---

## Assumptions

* Products are rejected from the cart if:

  * Expired (`date.today() > expiry_date`)
  * Quantity requested exceeds available stock
* Shipping cost: **30 EGP per kg**
* Shippable items must implement:

  * `get_name()`
  * `get_weight()`
* The system auto-skips failed `add()` attempts but logs them.

---

