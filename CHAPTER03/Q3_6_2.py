import random

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
b = "".join(random.sample(numbers, k=4))
while True:
    c = input()
    if c == b:
        break
    if len(c) != 4:
        print("input 4 numbers.")
        continue
    answer = ""
    for i in range(4):
        if b[1] == c[i]:
            answer += b[i]
        else:
            answer += "X"
    print("->" + answer)
