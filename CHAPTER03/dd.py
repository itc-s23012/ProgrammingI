with open("numbers.txt", "r") as f:
    a = sum(int(data) for data in f)
    print(a)
# 55
