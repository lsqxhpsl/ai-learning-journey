def get_scores():
    """录入成绩，返回列表"""
    scores = []
    while True:
        s = input("请输入成绩（输入 q 结束）：")
        if s == "q":
            break
        scores.append(int(s))
    return scores

def analyze(scores):
    """统计并打印结果"""
    if len(scores) == 0:
        print("没有数据")
        return
    print(f"数量: {len(scores)}")
    print(f"最高: {max(scores)}")
    print(f"最低: {min(scores)}")
    print(f"平均: {sum(scores)/len(scores):.1f}")

# 主程序
scores = get_scores()
analyze(scores)
