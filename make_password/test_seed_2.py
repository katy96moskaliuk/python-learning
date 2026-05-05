from make_password_1 import make_password
import random

# random.seed(0)
# print(make_password())

# random.seed(1)
# print(make_password())

print(make_password())


# Observations:
# Running this multiple times with seed(0) → same passwords every time.
# Changing the seed to 1 → different passwords, but repeatable with seed(1).
# Removing random.seed() → passwords change every run because 
# the seed is set automatically (usually based on system time).