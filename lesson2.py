# 第2课练习：让程序和你对话
name = input("请输入你的名字：")
birth_year = int(input("请输入你的出生年份："))

age = 2026 - birth_year

print(f"你好，{name}！")
print(f"你今年 {age} 岁，明年就 {age + 1} 岁了")
