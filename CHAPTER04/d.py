def outer(a, b):
    print("outer function (a, b) = ({}, {})".format(a, b))

    def inner(c, d):
        print("inner function (c, d) = ({}, {})".format(c, d))
        return c * d

    return inner(a, b)


a = outer(4, 7)
print(a)


def a():
    for i in range(1, 10):
        for j in range(1, 10):
            b = i * j
            print("{:2d} x {:2d} = {:2d}".format(i, j, b))
        print()


a()

for i in range(1, 10):
    for f in range(1, 10):
        a = i * f
        print(f"{a:>4}", end="")
    print()

for i in range(1, 10):
    for f in range(1, 10):
        print(f"{i} × {f} = {i * f}")
    print()
