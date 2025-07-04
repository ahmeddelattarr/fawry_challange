class ShippingService:
	def ship(self, shippable_items_with_qty):
		total_weight = 0
		print("** Shipment notice **")
		for item, quantity in shippable_items_with_qty:
			weight = item.get_weight() * quantity
			total_weight += weight
			print(f"{quantity}x {item.get_name():12} {weight * 1000:.0f}g")
		print(f"Total package weight {total_weight:.1f}kg\n")
		return total_weight * 30