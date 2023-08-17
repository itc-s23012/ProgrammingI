yamanote_line = {0: 'Tokyo', 1: 'Yuurakuchou', 2: 'Shinbashi'}
for v in yamanote_line.values():
    print(v)
# ①
a = {1: 'Hokkaido', 2: 'Aomori', 3: 'Iwate'}
print(a)

print(a[1])

print(a.get(0))

print(a.get(1))

print(a.get(0, 'Not Found'))
