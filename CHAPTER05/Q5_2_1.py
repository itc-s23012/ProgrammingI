num = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]]
col = [row[2] for row in num]
print(col)
#➂

prime = [2, 3, 5, 7, 11, 13]
prime_square = [x**2 for x in prime]
print(prime_square)
#２乗

a = [2, 3, 5, 7, 11, 13]
b = [x**3 for x in a]
print(b)

a = [i * j for i in range(1, 3) for j in range(1, 10)]
print(a)

b = [i * j for i in range(1, 4) for j in range(1, 10)]
print(b)
