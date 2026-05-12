class Order:
	def __init__(self, order_id, items, **kwargs):
		super().__init__(**kwargs)
		self.order_id = order_id
		self.items = items

	def items_total(self):
		return sum(price for _, price in self.items)
	
	def total(self):
		return self.items_total()
	
	def describe(self):
		return f"Order #{self.order_id}: total = {self.total()}"

class DeliveryOrder(Order):
	def __init__(self, delivery_price, **kwargs):
		super().__init__(**kwargs)
		self.delivery_price = delivery_price

	def total(self):
		return super().total() + self.delivery_price
	
class DiscountOrder(Order):
		def __init__(self, discount, **kwargs):
			super().__init__(**kwargs)
			self.discount = discount

		def total(self):
			return super().total() - super().total()*self.discount


class FinalOrder(DiscountOrder, DeliveryOrder):
	pass


items = [
	('Book', 100),
	('Pen', 20),
	('Notebook', 80),
]

order = Order(order_id=1, items=items)
assert order.items_total() == 200
assert order.total() == 200
assert order.describe() == "Order #1: total = 200"

delivery_order = DeliveryOrder(
    order_id=2,
    items=items,
    delivery_price=50,
)
assert delivery_order.total() == 250

discount_order = DiscountOrder(
    order_id=3,
    items=items,
    discount=0.10,
)
assert discount_order.total() == 180

final_order = FinalOrder(
    order_id=4,
    items=items,
    delivery_price=50,
    discount=0.10,
)
assert final_order.total() == 225

assert FinalOrder.mro() == [
    FinalOrder,
    DiscountOrder,
    DeliveryOrder,
    Order,
    object,
]

print(FinalOrder.__mro__)