# 第7课挑战：简易英文单词本
vocab = {}

while True:
    print("\n1.查词  2.加词  3.退出")
    choice = input("请选择：")

    if choice == "1":
        word = input("输入要查的单词：")
        if word in vocab:
            print(f"{word} = {vocab[word]}")
        else:
            print("还没收录这个词，选 2 加进去吧")
    elif choice == "2":
        word = input("输入新单词：")
        meaning = input("输入中文意思：")
        vocab[word] = meaning
        print("已添加！")
    elif choice == "3":
        print("再见！")
        break
    else:
        print("请输入 1、2 或 3")
