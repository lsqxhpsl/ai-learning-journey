# 第4课练习：循环
print("=== for 循环：打印 1 到 5 ===")
for i in range(1, 6):
    print("第", i, "次")

print("=== for 循环：累加 1 到 100 ===")
total = 0
for n in range(1, 101):
    total = total + n
print("1 加到 100 等于", total)

print("=== while 循环：倒数 ===")
count = 5
while count > 0:
    print(count)
    count = count - 1
print("发射！")
for i in range(1, 4):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="  ")
    print()
