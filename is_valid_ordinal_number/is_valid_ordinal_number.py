import re

def is_valid_ordinal_number(value: str) -> bool:
    pattern = r"^(\d+)(st|nd|rd|th)$"

    match = re.fullmatch(pattern, value)

    if not match:
        return False

    number = int(match.group(1))
    suffix = match.group(2)

    if 11 <= number % 100 <= 13:
        return suffix == "th"

    last_digit = number % 10

    if last_digit == 1:
        return suffix == "st"

    if last_digit == 2:
        return suffix == "nd"

    if last_digit == 3:
        return suffix == "rd"

    return suffix == "th"


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
