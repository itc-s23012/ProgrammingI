import random

numbers = list(range(10))
b = "".join(random.sample([str(num) for num in numbers], k=4))

while True:
    c = "".join(random.sample([str(num) for num in numbers], k=4))
    print(c)
    if c == b:
        break

    answer = "".join([b[i] if b[i] == c[i] else "X" for i in range(4)])
    print("->" + answer)
