# 第3周第1课：第一次调用 AI
from openai import OpenAI
from config import API_KEY

# 建立连接
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

print("正在问 AI，请稍等...")

# 发请求
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ]
)

# 取答案
answer = response.choices[0].message.content
print("AI 回答：", answer)
