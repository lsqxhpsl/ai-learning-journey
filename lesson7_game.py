import random
def play():
    secret = random.randint(1, 100)
    x = 0
    while True:
        x += 1
        y = int(input("请输入数字："))
        if y > secret:
            print("太大了")
        elif y < secret:
            print("太小了")
        else:
            print("答对了！")
            print(f"你一共猜了{x}次")
            break
def main():
    print("=== 猜数字游戏 ===")
    while True:
        play()
        again = input("再来一局？(y/n)：")
        if again != "y":
            print("拜拜")
            break
main()