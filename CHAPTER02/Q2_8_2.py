a = ["I", "have", "an", "apple"]
a[2:4] = ["a", "pineapple"]
print(a)

a = ["I", "have", "an", "apple"]
result = "I, have, an, apple".replace("an", "a").replace("apple", "pineapple")
print(result)

a = ["I", "have", "an", "apple"]
result = ", ".join(a).replace("an", "a").replace("apple", "pineapple")
print(result)

a = ["I", "have", "an", "apple"]
result = [word.replace("an", "a").replace("apple", "pineapple") for word in a]
print(result)
