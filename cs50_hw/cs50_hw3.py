import string as str


def main():
    # fuel_gauge()        # 意外控制 类型错误 0除
    # felipes_taqueria()  # 意外控制 EOF 字典不匹配
    # grocery_list()      # 字典管理 排序
    # outdated()          # 字符串处理
    pass


def fuel_gauge():
    x = get_int("Input x: ")
    y = get_int("Input y: ")
    try:
        z = x / y
    except ZeroDivisionError:
        print("Division can not be 0")
    else:
        if z >= 0.99:
            print("F")
        elif z <= 0.01:
            print("E")
        else:
            print(f"{z * 100:.0f}%")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input is not an integer")


def felipes_taqueria():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    total = 0
    while True:
        try:
            item = input("Item: ")
            total += menu[item.title()]
            print(f"Total :${total:.2f}")
        except [EOFError, KeyError]:
            break


def grocery_list():
    dic = {}
    while True:
        try:
            item = input()
            if item.upper() in dic:
                dic[item.upper()] += 1
            else:
                dic[item.upper()] = 1
        except EOFError:
            break

    for key, value in sorted(dic.items()):
        print(value, " " + key.upper())


def outdated():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                mm, dd, yyyy = date.split("/")
            else:
                mmdd, yyyy = date.split(",")
                yyyy = yyyy.strip()
                mm, dd = mmdd.split(" ")
                if mm not in months:
                    continue
                else:
                    mm = months[mm]
            if int(dd) not in range(1, 32) or int(mm) not in range(1, 13):
                continue
            print(f"{int(yyyy):04d}-{int(mm):02d}-{int(dd):02d}")
        except EOFError:
            break


main()
