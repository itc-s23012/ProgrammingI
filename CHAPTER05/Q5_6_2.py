A = {x for x in range(21)}
print(A)
B = {x for x in range(21) if x % 2 == 0}
print(B)
C = A - B
print(C)

A = set('ABCDEF')
B = set('ABCDEF')
C = set('ABC')
print(A == B)
print(A == C)

D = set('GHI')
print(A.isdisjoint(D))
print(C <= A)
print(C.issubset(A))
print(A >= C)
print(A.issuperset(C))
