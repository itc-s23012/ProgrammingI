a = [1, 1, 2, 3, 5, 8, 13, 21]
x = 0
for n in a:
    if n > 10:
        break
    x += n
print(x)
# 20

a = [1, 1, 2, 3, 5, 8, 13, 21]
x = sum(n for n in a if n <= 10)
print(x)
