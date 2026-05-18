# `is_valid_moldova_phone`

Write a function

```python
def is_valid_moldova_phone(phone: str) -> bool:
    pass
```

The function must validate Moldovan phone numbers in:

- local format: 012345678
- international format: +37312345678

Spaces and dashes inside the number are allowed. Other characters are not allowed.


## Tests

```python
assert is_valid_moldova_phone("012345678") is True
assert is_valid_moldova_phone("012 345 678") is True
assert is_valid_moldova_phone("012-345-678") is True
assert is_valid_moldova_phone("012 345-678") is True

assert is_valid_moldova_phone("+37312345678") is True
assert is_valid_moldova_phone("+373 123 456 78") is True
assert is_valid_moldova_phone("+373-123-456-78") is True
assert is_valid_moldova_phone("+373 123-456 78") is True

assert is_valid_moldova_phone("12345678") is False
assert is_valid_moldova_phone("0012345678") is False
assert is_valid_moldova_phone("+3731234567") is False
assert is_valid_moldova_phone("+373123456789") is False

assert is_valid_moldova_phone("abc") is False
assert is_valid_moldova_phone("+373 abc def gh") is False
assert is_valid_moldova_phone("") is False

assert is_valid_moldova_phone("+373_123_456_78") is False
assert is_valid_moldova_phone("012/345/678") is False
assert is_valid_moldova_phone("+1 123 456 789") is False

assert is_valid_moldova_phone("+373--12345678") is False
```
