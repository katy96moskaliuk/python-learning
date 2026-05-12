# Assignment: data type variants for orders in an online store

The goal of this assignment is to implement several variants of a single data type: `Order`.

The assignment is not about building a complete online store system.

You do not need to implement:

- users
- shopping carts
- payment systems
- databases
- warehouse logic
- delivery services
- UI

The goal is to demonstrate how inheritance and `super()` can be used to extend the behavior of a base order type:

- a regular order
- an order with delivery
- an order with a discount
- an order that has both delivery and a discount

## Data

Items are stored as a list of tuples:

```python
items = [
    ("Book", 100),
    ("Pen", 20),
    ("Notebook", 80),
]
```

Each tuple contains:

- item name
- item price

## Requirements

### Base class `Order`

Stores:

- `order_id`
- `items`

Methods:

- `items_total()` — returns the total price of all items
- `total()` — returns the final order price
- `describe()` — returns a string description of the order

### Class `DeliveryOrder`

Inherits from `Order`.

Adds:

- `delivery_price`

Overrides:

- `total()`

The method must call `super().total()` and add the delivery cost.

### Class `DiscountOrder`

Inherits from `Order`.

Adds:

- `discount`

Overrides:

- `total()`

The method must call `super().total()` and apply the discount.

The discount is represented as a number between `0` and `1`.

For example:

```python
discount = 0.10
```

means a 10% discount.

### Class `FinalOrder`

Inherits from both `DiscountOrder` and `DeliveryOrder`.

This class must combine both behaviors:

- adding delivery cost
- applying a discount

Inheritance order:

```python
class FinalOrder(DiscountOrder, DeliveryOrder):
    ...
```

With this inheritance order, the discount is applied after the delivery cost is added.

## Important restriction

Child classes must not recalculate the item sum using `sum(...)`.

Incorrect:

```python
def total(self) -> float:
    return sum(price for name, price in self.items) + self.delivery_price
```

The goal is not only to produce the correct number, but to build a method call chain using `super()`.

## Code skeleton

```python
Item = tuple[str, float]


class Order:
    def __init__(self, order_id: int, items: list[Item], **kwargs) -> None:
        ...

    def items_total(self) -> float:
        ...

    def total(self) -> float:
        ...

    def describe(self) -> str:
        ...


class DeliveryOrder(Order):
    def __init__(self, delivery_price: float, **kwargs) -> None:
        ...

    def total(self) -> float:
        ...


class DiscountOrder(Order):
    def __init__(self, discount: float, **kwargs) -> None:
        ...

    def total(self) -> float:
        ...


class FinalOrder(DiscountOrder, DeliveryOrder):
    pass
```

## Example checks

```python
items = [
    ("Book", 100),
    ("Pen", 20),
    ("Notebook", 80),
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
```

## Calculation explanation for `FinalOrder`

```text
items total: 200
+ delivery: 50
= 250
- discount 10%
= 225
```

Method call chain:

```text
FinalOrder.total()
→ DiscountOrder.total()
→ DeliveryOrder.total()
→ Order.total()
```

`FinalOrder` does not implement `total()` itself.

It gets its behavior through inheritance order and correct usage of `super()` in parent classes.
