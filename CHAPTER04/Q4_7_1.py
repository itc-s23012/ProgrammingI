def make_addfunc():
    def add(x, y):
        return x + y

    return add


adder = make_addfunc()
answer = adder(1, 10)
print(answer)


def make_addfunc():
    print("足し算する関数を作成")

    def add(x, y):
        print("{} + {} = {}".format(x, y, x + y))
        return x + y

    return add


def make_addfunc():
    return lambda x, y: x + y


adder = make_addfunc()
answer = adder(1, 10)
print(answer)

adder = make_addfunc()
answer = adder(1, 10)
print(answer)
