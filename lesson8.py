# 第7课练习：字典
student = {
    "name": "lsqxhpsl",
    "age": 23,
    "city": "长治",
    "目标": "AI应用工程师"
}

print("我的信息：", student)
print("姓名：", student["name"])
print("城市：", student["city"])

student["学习时长"] = "每天2小时"   # 存（新增一项）
print("添加后：", student)

student["age"] = 24                 # 改（覆盖旧值）
print("改年龄后：", student)

print("--- 逐项查看 ---")
for key, value in student.items():
    print(f"{key} : {value}")
