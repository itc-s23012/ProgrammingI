A = {x for x in range(21) if x % 2 == 1}
print(A)

a = set('ABCDEF')
print(a)

a.add('G')
print(a)

a.remove('G')
print(a)

a.clear()
print(a)

prime = {2, 3, 5, 7, 11, 13}
prime_square = {x**2 for x in prime}
print(prime_square)

print({frozenset([1, 3, 5, 7, 9,]):'odd'})
