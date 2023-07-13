import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num4 = "".join(random.sample(numbers, k=4))

while input() != num4:
    print("NG")

print("OK")
