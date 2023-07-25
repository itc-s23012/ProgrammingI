many_numbers = list(range(100))
s = ""
for i in many_numbers:
    s += "{:2d},".format(i)
    if i % 10 == 9:
        s += "\n"
print(s)

a = list(range(1, 100))
s = ""
for i in a:
    s += "{:2d},".format(i)
    if i % 9 == 0:
        s += "\n"
print(s)
