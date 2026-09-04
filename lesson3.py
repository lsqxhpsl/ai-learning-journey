# 第3课练习：if 判断
score = int(input("请输入你的考试分数（0-100）："))

if score >= 90:
    print("优秀！")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("需要努力了")
age = int(input("请输入你的年龄："))
if age >= 18 and age < 60:
    print("你是成年人")
else:
    print("你是未成年人或老年人")
