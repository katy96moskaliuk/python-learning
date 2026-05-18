# `is_valid_ipv4_address`

Write a function

```python
def is_valid_ipv4_address(ip: str) -> bool:
    pass
```

The function must validate IPv4 addresses.

A valid IPv4 address has four decimal numbers separated by dots.

Each number must be from 0 to 255.

Spaces, letters, extra dots, missing parts, and other characters are not allowed.


## Tests

```python
assert is_valid_ipv4_address("0.0.0.0") is True
assert is_valid_ipv4_address("127.0.0.1") is True
assert is_valid_ipv4_address("192.168.1.1") is True
assert is_valid_ipv4_address("255.255.255.255") is True
assert is_valid_ipv4_address("8.8.8.8") is True

assert is_valid_ipv4_address("256.0.0.1") is False
assert is_valid_ipv4_address("192.168.1.256") is False
assert is_valid_ipv4_address("999.999.999.999") is False

assert is_valid_ipv4_address("192.168.1") is False
assert is_valid_ipv4_address("192.168.1.1.1") is False
assert is_valid_ipv4_address("192..168.1.1") is False
assert is_valid_ipv4_address(".192.168.1.1") is False
assert is_valid_ipv4_address("192.168.1.1.") is False

assert is_valid_ipv4_address("192.168.01.1") is False
assert is_valid_ipv4_address("001.168.1.1") is False

assert is_valid_ipv4_address("192.168.1.a") is False
assert is_valid_ipv4_address("abc") is False
assert is_valid_ipv4_address("") is False

assert is_valid_ipv4_address("192.168.1.1 ") is False
assert is_valid_ipv4_address(" 192.168.1.1") is False
assert is_valid_ipv4_address("192 168 1 1") is False
assert is_valid_ipv4_address("192-168-1-1") is False
```
