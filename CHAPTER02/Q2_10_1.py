print(pow(*divmod(20, 3)))

a, b = divmod(20, 3)
c = pow(a, b)
print(c)

result = divmod(20, 3)
print(pow(result[0], result[1]))
