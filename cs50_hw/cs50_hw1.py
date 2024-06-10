import string as str


def main():
    # deep_thought()              # 字符串匹配
    # home_federal_savings_bank() # 嵌套分支
    # file_extensions()           # 字符串分割 最右子串
    # math_interpreter()          # 字符串转算式 字符串分割
    # meal_time()                 # 字符串转浮点数 用范围进行match case
    pass


def deep_thought():
    s = input().lower()
    if s == "42" or s == "forty two" or s == "forty-two":
        print("Yes")
    else:
        print("No")


def home_federal_savings_bank():
    s = input().lower()
    if s.startswith("h"):
        if s.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


def file_extensions():
    # 获取最右边的子串
    _, s = input().strip().lower().rsplit(".", 1)
    match s:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def math_interpreter():
    # 分割字符串
    x, y, z = input().strip().split(" ", 2)
    match y:
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))
        case _:
            pass


def meal_time():
    hour, min = input().strip().split(":")
    time = float(hour) + float(min) / 60
    match time:
        case temp if temp >= 7 and temp <= 8:
            print("breakfast time")
        case temp if temp >= 12 and temp <= 13:
            print("lunch time")
        case temp if temp >= 18 and temp <= 19:
            print("dinner time")
        case _:
            pass


main()
