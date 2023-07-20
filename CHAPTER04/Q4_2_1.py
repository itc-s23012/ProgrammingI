def number_to_day(num=0):
    if num == 0:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より１日を超えて離れた日"
    return day


day = number_to_day
print(day(1))

print(number_to_day(0))
print(number_to_day(1))
print(number_to_day(-1))
print(number_to_day(5))


def number_to_day(num=0):
    return (
        ["今日", "明日", "昨日", "今日より１日を超えて離れた日"][num]
        if -1 <= num <= 1
        else "今日より１日を超えて離れた日"
    )


print(number_to_day(1))
print(number_to_day(0))
print(number_to_day(-1))
print(number_to_day(5))
