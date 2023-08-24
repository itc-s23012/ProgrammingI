with open("my_math.py", "w") as f:
    f.write("""def my_pow(x, y):
    return x ** y\n""")
import my_math
print(my_math.my_pow(2, 5))

print(my_math.my_pow(2, 0.5))
ans = my_math.my_pow(-4, 0.5)
print(ans)

print("実数成分:  {}, 虚数成分: {}".format(ans.real, ans.imag))


with open("my_math.py", "w") as f:
    f.write("def my_pow(x, y):\n    return x ** y\n")

import my_math

print(my_math.my_pow(2, 5))
print(my_math.my_pow(2, 0.5))
ans = my_math.my_pow(-4, 0.5)
print("実数成分: {}, 虚数成分: {}".format(ans.real, ans.imag))

import my_module
print(my_module.func(5))

def func(v):
    i = v + 3
    return i

class MyClass:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def show_attributes(self):
        print("a = {}, sum: {}".format(self.a, self.b, self.sum())
                def sum(self):
                return self.a + self.b
import my_module1
my_class = my_module1.MyClass(3, 5)
my_class.show_attributes()
my_module1.func(10)
