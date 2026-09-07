# 第6课练习：函数
def say_hello(name):
    print(f"你好，{name}！")

say_hello("lsqxhpsl")
say_hello("AI 学习者")

def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

print(f"100°C = {celsius_to_fahrenheit(100):.1f}°F")
print(f"36.6°C = {celsius_to_fahrenheit(36.6):.1f}°F（体温）")
