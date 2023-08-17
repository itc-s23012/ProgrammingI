a = {x for x in 'abcabcabc' if x not in 'ab'}
b = {y for y in 'abcabcabc' if y not in 'bc'}
print(a | b)
# ①

A = set('ABCDEF')
B = set('DEFGHI')
print(A - B)
print(A | B)
print(A & B)
C = set('ABC')
print(A == B)
print(A == C)
