# Задание: разновидности типа данных для заказов в интернет-магазине.

Цель задания — реализовать несколько разновидностей одного типа данных: `Order`.
Нужно показать, как с помощью наследования и `super()` можно расширять поведение базового заказа:

- обычный заказ
- заказ с доставкой
- заказ со скидкой
- заказ, у которого есть и доставка, и скидка

## Данные

Товары хранятся в виде списка кортежей:

```python
items = [
    ("Book", 100),
    ("Pen", 20),
    ("Notebook", 80),
]
```

Каждый кортеж содержит:

- название товара
- стоимость товара

## Требования

### Базовый класс `Order`

Хранит:

- `order_id`
- `items`

Методы:

- `items_total()` — возвращает сумму товаров
- `total()` — возвращает итоговую стоимость заказа
- `describe()` — возвращает строку с описанием заказа

### Класс `DeliveryOrder`

Наследуется от `Order`.

Добавляет:

- `delivery_price`

Переопределяет:

- `total()`

Метод должен вызвать `super().total()` и добавить стоимость доставки.

### Класс `DiscountOrder`

Наследуется от `Order`.

Добавляет:

- `discount`

Переопределяет:

- `total()`

Метод должен вызвать `super().total()` и применить скидку.

Скидка задаётся числом от `0` до `1`.

Например:

```python
discount = 0.10
```

означает скидку 10%.

### Класс `FinalOrder`

Наследуется от `DiscountOrder` и `DeliveryOrder`.

Этот класс должен объединять оба поведения:

- добавление доставки
- применение скидки

Порядок наследования:

```python
class FinalOrder(DiscountOrder, DeliveryOrder):
    ...
```

При таком порядке скидка применяется к сумме товаров вместе с доставкой.

## Важное ограничение

В дочерних классах нельзя заново считать сумму товаров через `sum(...)`.

Неправильно:

```python
def total(self) -> float:
    return sum(price for name, price in self.items) + self.delivery_price
```

Правильно — не просто получить правильное число, а построить цепочку вызовов через `super()`.


## Каркас кода

```python
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

## Пример проверки

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

## Пояснение расчёта для `FinalOrder`

```text
items total: 200
+ delivery: 50
= 250
- discount 10%
= 225
```

Цепочка вызовов:

```text
FinalOrder.total()
→ DiscountOrder.total()
→ DeliveryOrder.total()
→ Order.total()
```

`FinalOrder` сам не реализует `total()`.

Он получает поведение за счёт порядка наследования и корректного использования `super()` в родительских классах.
