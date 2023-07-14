import random

numbers = "0123456789"
num4 = "".join(random.sample(numbers, k=4))

while input() != num4:
    print("NG")

print("OK")
