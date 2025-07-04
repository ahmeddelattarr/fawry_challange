class ShippingService:
	def ship(self,shippable_items, cart):
		total_weight= sum(items.get_weight() * cart.items[items] for items in shippable_items)
		print("** shipment notice **")
		for item in shippable_items:
			quantity = cart.items[item]
			print(f"{quantity}x {item.get_name():12} {item.get_weight() * quantity * 1000:.0f}g")

		print (f"Total weight: {total_weight * 1000:.0f}g")
		return total_weight *30