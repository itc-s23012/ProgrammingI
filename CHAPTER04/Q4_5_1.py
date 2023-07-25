a = [sum, min, max]
numbers = range(1, 11)
print(list(numbers))

a = [sum, min, max]
b = range(1, 11)
for i in a:
    print("Function: {}, Result: {}".format(i.__name__, i(b)))

b = range(1, 33)
a = list(b)
print(sum(a))
print(min(a))
print(max(a))
