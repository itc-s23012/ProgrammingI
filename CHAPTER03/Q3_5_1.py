a = 1
while a < 10:
    if a % 2 == 0:
        print(a)
    a += 1

a = 1
while True:
    if a % 2 == 0:
        print(a)
    a += 1  # ここで止めた場合無限ループ
    if a >= 10:
        break
