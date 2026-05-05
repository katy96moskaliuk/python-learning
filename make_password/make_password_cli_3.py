import argparse
from make_password_1 import make_password

def main():
	parser = argparse.ArgumentParser(description='Generate a random password')

	parser.add_argument("--min-digits", type=int)
	parser.add_argument("--max-digits", type=int)
	parser.add_argument("--min-uppercase", type=int)
	parser.add_argument("--max-uppercase", type=int)
	parser.add_argument("--min-lowercase", type=int)
	parser.add_argument("--max-lowercase", type=int)
	parser.add_argument("--min-punctuation", type=int)
	parser.add_argument("--max-punctuation", type=int)

	args = parser.parse_args()

	try:
		password = make_password(
    	min_digits=args.min_digits if args.min_digits is not None else 2,
    	max_digits=args.max_digits if args.max_digits is not None else 4,
    	min_uppercase=args.min_uppercase if args.min_uppercase is not None else 4,
    	max_uppercase=args.max_uppercase if args.max_uppercase is not None else 8,
    	min_lowercase=args.min_lowercase if args.min_lowercase is not None else 4,
    	max_lowercase=args.max_lowercase if args.max_lowercase is not None else 8,
    	min_punctuation=args.min_punctuation if args.min_punctuation is not None else 2,
    	max_punctuation=args.max_punctuation if args.max_punctuation is not None else 4
		)
		print(password)
	except ValueError as e:
		print(f'Error{e}')

if __name__ == "__main__":
	main()