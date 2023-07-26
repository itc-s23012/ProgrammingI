print(list(range(1, 8)))
print("{:04}".format(5))

a = map(lambda x: "{:04}".format(x), range(1, 8))
print(a)

print(list(a))

print(["{:0=4}".format(x) for x in range(1, 8)])
print(("{:0=4}".format(x) for x in range(1, 8)))
print(list("{:0=4}".format(x) for x in range(1, 8)))

print(list(range(1, 8)))

print("{:04}".format(5))

formatted_list = ["{:04}".format(x) for x in range(1, 8)]
print(formatted_list)

formatted_generator = ("{:04}".format(x) for x in range(1, 8))
print(list(formatted_generator))
