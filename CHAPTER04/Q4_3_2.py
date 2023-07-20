numbers = [1, 2, 3, 4]


def func_hint(*args):
    print("args:", args)
    print("len(args):", len(args))


print(func_hint(*numbers))

many_numbers = list(range(100))
print(many_numbers)


def func_square(*args):
    results = []
    for n in args:
        results.append(n * n)
    return results


numbers = [1, 2, 3, 4]
print(func_square(*numbers))

many_numbers = list(range(100))
print(func_square(*many_numbers))


def func_square(*args):
    return [n * n for n in args]


numbers = [1, 2, 3, 4]
print(func_square(*numbers))

many_numbers = list(range(100))
print(func_square(*many_numbers))
