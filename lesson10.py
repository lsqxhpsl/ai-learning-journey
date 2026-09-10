# 第9课练习：异常处理

# 例1：除零会崩
print("=== 例1：除零 ===")
try:
    result = 10 / 0
    print("结果是", result)
except ZeroDivisionError:
    print("出错了：不能除以 0")

# 例2：用户输入不对，程序也不崩
print("\n=== 例2：输入数字 ===")
try:
    num = int(input("请输入一个数字："))
    print(f"你输入的是 {num}，它的 2 倍是 {num*2}")
except ValueError:
    print("这不是一个有效数字")

print("程序继续运行了！")

# 例3：列表越界
print("\n=== 例3：列表越界 ===")
fruits = ["苹果", "香蕉", "橙子"]
try:
    idx = int(input("输入 0-2 的索引："))
    print(f"你选的是 {fruits[idx]}")
except ValueError:
    print("请输入数字")
except IndexError:
    print("索引超出范围，列表只有 3 个元素")

# 例4：finally 无论对错都执行
print("\n=== 例4：finally ===")
try:
    f = open("not_exist.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("文件不存在")
finally:
    print("这段话无论成功失败都会打印")
