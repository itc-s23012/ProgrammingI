x = True
y = False
z = None

print(x and z is None)  # ①   xとaどちらの値もNoneかを調べる式
print(not x or not y)  # ②
print(x and not y and z is None)  # ③

# ①  True
# ②  True
# ③　True
