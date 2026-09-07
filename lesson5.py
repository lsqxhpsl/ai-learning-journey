# 第5课练习：列表
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("我的水果篮：", fruits)

print("第一个：", fruits[0])
print("最后一个：", fruits[-1])

fruits.append("西瓜")
print("加了西瓜后：", fruits)

fruits.remove("香蕉")
print("吃掉香蕉后：", fruits)

print("一共有", len(fruits), "种水果")

print("--- 我吃过的水果 ---")
for f in fruits:
    print("我吃过", f)
