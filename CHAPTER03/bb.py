import random

numbers = "0123456789"
b = "".join(random.sample(numbers, k=4))

while True:
    c = input()
    if c == b:
        break
    if len(c) != 4:
        print("input 4 numbers.")
        continue

    answer = "".join([b[i] if b[i] == c[i] else "X" for i in range(4)])

    print("->" + answer)
