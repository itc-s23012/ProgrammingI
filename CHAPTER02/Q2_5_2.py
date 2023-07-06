w = "○ "
b = "● "
a = w + b * 3 + "\n" + b + w + b * 2 + "\n" + b * 2 + w + b + "\n" + b * 3 + w
print(a)

w = "○ "
b = "● "

for i in range(4):
    if i == 0:
        print(w + b * 3)
    elif i == 1:
        print(b + w + b * 2)
    elif i == 2:
        print(b * 2 + w + b)
    elif i == 3:
        print(b * 3 + w)
