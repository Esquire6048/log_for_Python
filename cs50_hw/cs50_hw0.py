import string as str


def main():
    # indoor_voice()   # 大写变小写
    # playback_speed() # 字符串替换
    # making_faces()   # 字符串替换为Emoji
    # einstein()       # 次方计算
    # tip_calculator() # 字符串转浮点数
    pass


def indoor_voice():
    print(input().lower())


def playback_speed():
    print(input().replace(" ", "..."))


def making_faces():
    print(input().replace(":)", "🙂").replace(":(", "🙁"))


def einstein():
    # 方法1
    print(int(input()) * (300000000**2))
    # 方法2
    print(int(input()) * pow(300000000, 2))


def tip_calculator():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100


main()
