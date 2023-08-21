def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_days_in_month(month, year):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return days_per_month[month - 1]

def get_first_day_of_month(month, year):
    q = 1
    m = month
    Y = year if month > 2 else year - 1
    K = Y % 100
    J = Y // 100
    h = (q + 13*(m + 1) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    return h

def create_calendar(month, year):
    days_in_month = get_days_in_month(month, year)
    first_day = get_first_day_of_month(month, year)

    days_of_week = ['日', '月', '火', '水', '木', '金', '土']
    color_code = {
        "土": "\033[91m",
        "日": "\033[94m",
    }
    header = f'{year}年{month}月'
    calendar_str = header.center(20) + '\n'
    calendar_str += ' '.join(days_of_week) + '\n'

    calendar_str += '   ' * first_day

    current_day = 1
    day_of_week = first_day
    while current_day <= days_in_month:
        calendar_str += f'{current_day:2} '
        current_day += 1
        day_of_week += 1
        if day_of_week == 7:
            calendar_str += '\n'
            day_of_week = 0

    return calendar_str

print(create_calendar(8, 2023))

