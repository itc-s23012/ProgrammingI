a = "1.0,2.2,3.5"
print(a.split(","))

a = "1.0"
b = float(a)
print(type(a), a)
print(type(b), b)
print([a, b])

a = list(range(1, 8))


def double(x):
    return x * 2


for e in map(double, a):
    print(e, end=" ")

print(map(double, a))

print(list(map(double, a)))

s_coordi_list = ["1.0.2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def str_to_float_coordi(s_coordi):
    p = s_coordi.split(",")
    return list(map(float, p))


def str_to_float_coordi_iter(s_coordi_list):
    return map(str_to_float_coordi, s_coordi_list)


f_coordi_list = list(str_to_float_coordi_iter(s_coordi_list))

print(f_coordi_list)

a = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def b(s_coordi):
    p = s_coordi.split(",")
    f_coordi = []
    for n in p:
        f_coordi.append(float(n))
    return f_coordi


f_coordi_list = []
for s_coordi in a:
    f_coordi_list.append(b(s_coordi))
print(f_coordi_list)

a = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def b(s_coordi):
    p = s_coordi.split(",")
    f_coordi = [float(n) for n in p]
    return f_coordi


f_coordi_list = [b(s_coordi) for s_coordi in a]
print(f_coordi_list)
