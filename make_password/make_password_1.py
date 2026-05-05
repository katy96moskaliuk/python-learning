import random
import string

def make_password(min_digits: int = 2,
                  max_digits: int = 4,
                  min_uppercase: int = 4,
                  max_uppercase: int = 8,
                  min_lowercase: int = 4,
                  max_lowercase: int = 8,
                  min_punctuation: int = 2,
                  max_punctuation: int = 4) -> str:
	
	params = [
		(min_digits, max_digits),
		(min_uppercase, max_uppercase),
		(min_lowercase, max_lowercase), 
		(min_punctuation, max_punctuation)
	]
	for min_val, max_val in params:
		if not isinstance(min_val, int) or not isinstance(max_val, int):
			raise ValueError('All values must be integers!')
		if min_val < 0 or max_val < 0:
			raise ValueError('Minimum values must be non-negative!')
		if min_val > max_val:
			raise ValueError('The minimum value cannot be greater than the maximum!')
		

	n_digit = random.randint(min_digits, max_digits)
	n_upper = random.randint(min_uppercase, max_uppercase)
	n_lower = random.randint(min_lowercase, max_lowercase)
	n_punct = random.randint(min_punctuation, max_punctuation)
	
	password = []

	password += random.choices(string.digits, k=n_digit)
	password += random.choices(string.ascii_uppercase, k=n_upper)
	password += random.choices(string.ascii_lowercase, k=n_lower)
	password += random.choices(string.punctuation, k=n_punct)

	random.shuffle(password)

	return ''.join(password)

if __name__ == "__main__":
	print(make_password())



