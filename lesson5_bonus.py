# 第5课挑战：成绩收集器
scores = []

while True:
    s = input("请输入成绩（输入 q 结束）：")
    if s == "q":
        break
    scores.append(int(s))

if len(scores) > 0:
    print(f"你录入了 {len(scores)} 个成绩")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
    print(f"平均分：{sum(scores)/len(scores):.1f}")
else:
    print("你没有录入任何成绩")
