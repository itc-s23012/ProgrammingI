members = ['Yamada', 'Tanaka', 'Satou', 'Suzuki']
name = members.pop(3)
print(name)
# ④

square = []
square.append(1)
square.append(4)
square.append(9)
square.append(16)
square.append(25)
print(square)

square2 = [36, 49]
square.extend(square2)
print(square)
