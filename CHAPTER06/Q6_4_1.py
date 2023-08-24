import random

random.seed(1)
msgs = ["Hi", "Hello", "Good morning", "Good night", "See you later", "How are you", "Have a good day"]

with open("some.txt", "w") as f:
    for i in range(1000000):
        f.write("{}, {}\n".format(i, random.choice(msgs)))

with open('some.txt') as f:
    body = f.read()
    lines = body.split('\n')
    print('\n'.join(lines[:3]))  # 最初の3行を表示

with open('some.txt') as f:
    print(next(f), end="")  # 1行目を表示
    print(next(f), end="")  # 2行目を表示

with open('some.txt') as f:
    c = 0
    for l in f:
        print(l, end='')
        if c == 2:
            break
        c += 1

with open('some.txt') as f:
    c = 0
    for l in f:
        print(l, end='')
        if c == 2:
            break
        c += 1

