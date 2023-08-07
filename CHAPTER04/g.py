
# -*- coding:utf-8 -*-

import jpbizday
import datetime
import calendar

class calWidget(tk.Frame):
    def __init__(self, master = None, cnf = {}, **kw):

        tk.Frame.__init__(self, master, cnf, **kw)

root = tk.Tk()
root.title("calendar")
root.geometry('600x400')

# 作成したウィジットを配置
widget = calWidget(root)
widget.pack()

root.mainloop()
       
# frame_calendar部分の作成
        self.calDate = tk.Frame(self)
        self.calDate.pack()

        # 日付部分を作成するメソッドの呼び出し
        self.createCal(self.year, self.month)

    # 日付を表示
    def createCal(self, year, month):

        # 初期化
        try:
            for key,item in self.day.items():
                item.destroy()
        except:
            pass

        cal = calendar.Calendar()
        cal.setfirstweekday(6)
        # 指定した年月のカレンダーをリストで返す
        days = cal.monthdayscalendar(year, month)
        days_count = sum(len(v) for v in days)

        self.day = {}
        # 日付
        for y in range(0, len(days)):
            for x in range(0, 7):
                # 平日：黒、土曜：青、祝日、日曜：赤
                if days[y][x] != 0:
                    date = days[y][x]
                    if jpbizday.is_bizday(datetime.date(nowYear, nowMonth, date)):
                        color = "black"

                    elif x == 6:
                        color = "blue"
                    else:
                        color = "red"

                    self.day[date] = tk.Button(self.frame_calendar, text = date, fg = color, height = 2, width = 4, relief = "flat")
                    self.day[date].bind("<Button-1>", callback)

                    self.day[date].grid(column = x, row = y, padx = 10, pady=5)



