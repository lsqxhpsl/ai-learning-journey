# 第3周第2课挑战：带记忆的多轮对话
from openai import OpenAI
from config import API_KEY

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

SYSTEM_PROMPT = """你是一位耐心、专业的 AI 学习教练，帮助零基础学员规划学习路径。
回答简洁实用，多用例子，不堆术语。"""

# ⭐ 关键：用列表保存全部对话历史
history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("=== AI 学习教练（输入 quit 退出）===")
while True:
    q = input("\n你：")
    if q == "quit":
        break

    # 1. 把你的话存进历史
    history.append({"role": "user", "content": q})

    # 2. 把完整历史发给 AI
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=history
    )
    answer = response.choices[0].message.content

    # 3. 把 AI 的回答也存进历史（这样下次它就记得了）
    history.append({"role": "assistant", "content": answer})

    print("\n教练：" + answer)
