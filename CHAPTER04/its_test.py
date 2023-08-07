def a(s):
    n = len(s)
    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] < s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]

def main():
    N = int(input())
    b = []
    for _ in range(N):
        num = int(input())
        b.append(num)
    
    a(b)

    c = ' '.join(map(str, b))
    print(c)

if __name__ == "__main__":
    main()
