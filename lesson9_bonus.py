# 第8课挑战：能保存到硬盘的单词本
def load_vocab():
    try:
        with open("vocab.txt", "r", encoding="utf-8") as f:
            vocab = {}
            for line in f:
                line = line.strip()
                if "=" in line:
                    word, meaning = line.split("=", 1)
                    vocab[word] = meaning
            return vocab
    except FileNotFoundError:
        return {}

def save_vocab(vocab):
    with open("vocab.txt", "w", encoding="utf-8") as f:
        for word, meaning in vocab.items():
            f.write(f"{word}={meaning}\n")

vocab = load_vocab()
print(f"已加载 {len(vocab)} 个单词")

while True:
    print("\n1.查词  2.加词  3.退出")
    choice = input("请选择：")

    if choice == "1":
        word = input("输入要查的单词：")
        if word in vocab:
            print(f"{word} = {vocab[word]}")
        else:
            print("还没收录这个词")
    elif choice == "2":
        word = input("输入新单词：")
        meaning = input("输入中文意思：")
        vocab[word] = meaning
        save_vocab(vocab)
        print("已添加并保存！")
    elif choice == "3":
        print("再见！")
        break
