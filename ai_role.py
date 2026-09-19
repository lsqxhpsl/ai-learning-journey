# 第3周第2课：用 system prompt 给 AI 定人设
from openai import OpenAI
from config import API_KEY

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

# ⭐ 这就是"提示词"——给 AI 的岗位说明书
SYSTEM_PROMPT = """你是一位资深职业规划顾问，专门帮助求职者分析岗位、优化简历、准备面试。

回答要求：
1. 直接给结论，不说客套话
2. 建议必须具体可执行，不要说空话套话
3. 如果我的信息不够，主动追问
4. 每次回答控制在 300 字以内"""

def ask(question):
    """问一句，拿一句回答"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# 主循环
print("=== AI 职业顾问（输入 quit 退出）===")
while True:
    q = input("\n你问：")
    if q == "quit":
        break
    print("\n顾问：" + ask(q))
