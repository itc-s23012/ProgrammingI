def a(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("入力してください"))
print(f"{num}は{'素数' if a(num) else '素数ではありません'}")
