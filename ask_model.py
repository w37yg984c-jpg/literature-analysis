from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",   
)

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

prompt = f"""以下是一篇文学文本，请提出 3 种可行的文本分析方法建议，
例如：最高频词汇、能代表每个人物特征的词语、基于词典的情感分析（积极/消极分布）。
每种方法说明：需要什么套件、大致步骤、输出什么。先不要写代码。

文本内容：
{text}
"""

resp = client.chat.completions.create(
    model="z-ai/glm-5.3-flash",
    messages=[{"role": "user", "content": prompt}],
)

result = resp.choices[0].message.content
print(result)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result)    