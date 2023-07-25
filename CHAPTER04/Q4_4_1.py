import random
import time

vote_num = 0


def vote():
    print("投票します")
    global vote_num
    vote_num += 1


def reset_box():
    global vote_num
    print("箱を空にします")
    vote_num = 0


def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))


print(vote())
print(check_box())
print(vote())
print(check_box())
for i in range(3):
    print(vote())
print(check_box())
print(reset_box())
print(check_box())

民主党 = 0
共和党 = 0


def vote(team):
    global 民主党, 共和党
    if team == "A":
        民主党 += 1
    elif team == "B":
        共和党 += 1
        print("投票します")


def reset_box():
    global 民主党, 共和党
    民主党 = 0
    共和党 = 0
    print("箱を空にします")


def check_box():
    global 民主党, 共和党
    print("チームAの得票数は{}です".format(民主党))
    print("チームBの得票数は{}です".format(共和党))
    if 民主党 > 共和党:
        print("チームAの勝利です！")
    elif 民主党 < 共和党:
        print("チームBの勝利です！")
    else:
        print("引き分けです。")


def a(num_votes):
    teams = ["A", "B"]
    for _ in range(num_votes):
        b = random.choice(teams)
        vote(b)
        print("自動投票：チーム{}に投票しました".format(b))
        time.sleep(1)


print(a(10))
print(check_box())

print(vote("A"))
print(vote("B"))
print(check_box())
