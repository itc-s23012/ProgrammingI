a = "1.0,2.2,3.5"
print(a.split(","))

a = "1.0"
b = float(a)
print(type(a), a)
print(type(b), b)
print([a, b])

a = list(range(1, 8))


def double(x):
    return x * 2


for e in map(double, a):
    print(e, end=" ")
