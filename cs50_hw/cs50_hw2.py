import string as str


def main():
    # camel_case()               # 字符串作为数组逐个处理
    # coke_machine()             # while循环
    # just_setting_up_my_twttr() # 与参考数组的元素匹配
    # vanity_plates()            # 字符串操作 是否是数字 是否包含数字 第一个数字位 是否包含标点符号
    # nutrition_facts()          # 构建和查找字典
    pass


def camel_case():
    sentence = input().strip()
    for word in sentence:
        if word.capitalize() == word:
            print("_" + word.lower(), end="")
        else:
            print(word.lower(), end="")


def coke_machine():
    amount = 0
    while amount < 50:
        print("Amount Due:", 50 - amount)
        amount += int(input("Insert Coin: "))
    print("Chamge Owed:", amount - 50)


def just_setting_up_my_twttr():
    vowels = ["a", "e", "i", "o", "u"]
    words = input()
    for word in words:
        if word.lower() in vowels:
            pass
        else:
            print(word, end="")


def vanity_plates():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 长度不大于6且不小于2
    if len(s) > 6 or len(s) < 2:
        return False
    # 前两位不能是数字
    if s[0].isdigit() or s[1].isdigit():
        return False
    # 包含数字
    if any(char.isdigit() for char in s):
        # 最后一位不能是数字
        if s[len(s) - 1].isdigit() == False:
            return False
        # 第一个数字不能是数字
        if s[[char.isdigit() for char in s].index(True)] == "0":
            return False
    # 不能包含标点符号
    if any(char in str.punctuation for char in s):
        return False
    else:
        return True


def nutrition_facts():
    # 构建字典
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    # 意外处理
    fruit = fruits.get(input())
    if fruit:
        print(f"Calories is {fruit}.")
    else:
        print(f"Cannot find calories.")


main()
