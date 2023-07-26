def a(n):
    return "偶数" if (n % 2 == 0) else "奇数"


print(a(8))

a = list(map(int, "123"))
print(a)

l = [-1, -2, 3]
print(map(abs, l))
print(type(map(abs, l)))

a = range(1, 11)
b = list(map(lambda i: 2 * i, a))
print("文字列リスト:", b)

a = range(1, 11)
b = list(map(lambda i: str(i) + "番", a))
print("文字列リスト:", b)


even_numbers = list(filter(lambda i: i % 2 == 0, range(1, 11)))

for e in even_numbers:
    print(e, end=" ")

pairs = [(2, "down"), (1, "up"), (3, "left")]

pairs.sort(key=lambda x: x[1])
print(pairs)
