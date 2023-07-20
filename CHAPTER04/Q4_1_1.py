def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


print(fib(1000))

a = 0
b = 1
b, a = a, b
print(a, b)
print(fib(1000))


def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


a = fib(1000)
print(a)


def fib(n):
    a, b = 0, 1
    while a < n:
        c = a + b
        print(c)
        a = b
        b = c
        print(fib(1000))
