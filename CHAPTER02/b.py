print(pow(2, 3))

print(pow(10, 10))

print(pow(*divmod(20, 3)))

quotient, remainder = divmod(20, 3)
result_pow = pow(quotient, remainder)
print(result_pow)
