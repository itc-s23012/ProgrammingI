a = 0
while a < 100:
    if a > 10:
        break
    a += 2
    print(a)
# 12

a = 0
while a < 100:
    a += 2
print(a)
# 100

a = 0
while True:
    if a > 10:
        break
    a += 2
print(a)
# 12

a = 0
while a < 100 and a <= 10:
    a += 2
    print(a)
