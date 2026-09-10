# 第9课挑战：安全计算器
def safe_divide():
    try:
        a = float(input("输入第一个数："))
        b = float(input("输入第二个数："))
        result = a / b
        print(f"{a} ÷ {b} = {result}")
    except ValueError:
        print("请输入有效的数字（不要写字）")
    except ZeroDivisionError:
        print("除数不能为 0")
    except Exception as e:
        print(f"出错了：{e}")

while True:
    print("\n1.除法计算  2.退出")
    choice = input("选择：")
    if choice == "1":
        safe_divide()
    elif choice == "2":
        break
