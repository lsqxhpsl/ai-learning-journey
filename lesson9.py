# 第8课练习：文件读写

# 1. 写入（覆盖模式）
with open("my_note.txt", "w", encoding="utf-8") as f:
    f.write("Hello, 这是我的第一份文件。\n")
    f.write("第2行：今天学文件读写。\n")
    f.write("第3行：写完啦！\n")

print("文件写入完成")

# 2. 读取
with open("my_note.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("--- 文件内容 ---")
print(content)

# 3. 追加（在末尾接着写，不会清空）
with open("my_note.txt", "a", encoding="utf-8") as f:
    f.write("第4行：这是后来追加的。\n")

# 4. 再读看效果
with open("my_note.txt", "r", encoding="utf-8") as f:
    print("--- 追加后 ---")
    print(f.read())
