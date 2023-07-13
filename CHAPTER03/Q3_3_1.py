a = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
b = []
for s in a:
    if len(s) >= 6:
        b.append(s)
print(b)

a = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
b = [s for s in a if len(s) >= 6]
print(b)
