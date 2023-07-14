import random

num4 = "".join(random.sample([str(i) for i in range(10)], k=4))

while True:
    guess = input("Enter a 4-digit number: ")
    if guess == num4:
        print("OK")
        break
    else:
        print("NG")
