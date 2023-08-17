list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x if x%2==0 else None for x in list1])
# ④

mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
I = 2
J = 4
mat = [[i * J + j + 1 for j in range(J)] for i in range(I)]
print(mat)

prime = [2, 3, 5, 7, 11, 13]
a = [x**2 for x in prime if x**2 > 100]
print(a)

a = [('yamada', 20), ('satou', 35), ('tanaka', 50), ('suzuki', 40)]
print([i for i in range(len(a)) if a[i][1] >= 30])
