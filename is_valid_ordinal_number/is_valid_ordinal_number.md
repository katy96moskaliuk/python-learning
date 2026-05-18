# `is_valid_ordinal_number`

Write a function

```python
def is_valid_ordinal_number(value: str) -> bool:
    pass
```

The function must validate English ordinal numbers written with digits.

A valid ordinal number has one or more digits followed by the correct suffix: `st`, `nd`, `rd`, or `th`.

The suffix must match the number.

Spaces, letters before the number, missing suffixes, and other characters are not allowed.


## Tests

```python
assert is_valid_ordinal_number("1st") is True
assert is_valid_ordinal_number("2nd") is True
assert is_valid_ordinal_number("3rd") is True
assert is_valid_ordinal_number("4th") is True
assert is_valid_ordinal_number("5th") is True
assert is_valid_ordinal_number("9th") is True

assert is_valid_ordinal_number("10th") is True
assert is_valid_ordinal_number("11th") is True
assert is_valid_ordinal_number("12th") is True
assert is_valid_ordinal_number("13th") is True
assert is_valid_ordinal_number("14th") is True

assert is_valid_ordinal_number("21st") is True
assert is_valid_ordinal_number("22nd") is True
assert is_valid_ordinal_number("23rd") is True
assert is_valid_ordinal_number("24th") is True

assert is_valid_ordinal_number("101st") is True
assert is_valid_ordinal_number("102nd") is True
assert is_valid_ordinal_number("103rd") is True
assert is_valid_ordinal_number("104th") is True

assert is_valid_ordinal_number("111th") is True
assert is_valid_ordinal_number("112th") is True
assert is_valid_ordinal_number("113th") is True

assert is_valid_ordinal_number("1th") is False
assert is_valid_ordinal_number("2st") is False
assert is_valid_ordinal_number("3nd") is False
assert is_valid_ordinal_number("4rd") is False

assert is_valid_ordinal_number("11st") is False
assert is_valid_ordinal_number("12nd") is False
assert is_valid_ordinal_number("13rd") is False

assert is_valid_ordinal_number("21th") is False
assert is_valid_ordinal_number("22th") is False
assert is_valid_ordinal_number("23th") is False

assert is_valid_ordinal_number("1") is False
assert is_valid_ordinal_number("first") is False
assert is_valid_ordinal_number("1 st") is False
assert is_valid_ordinal_number(" 1st") is False
assert is_valid_ordinal_number("1st ") is False
assert is_valid_ordinal_number("1-st") is False
assert is_valid_ordinal_number("1ST") is False
assert is_valid_ordinal_number("") is False
```
