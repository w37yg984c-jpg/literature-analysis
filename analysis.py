from openai import OpenAI
import jieba
from collections import Counter

# 1. 最高频词汇
with open("text.txt", encoding="utf-8") as f:
    text = f.read()

words = [w for w in jieba.cut(text) if len(w) > 1]
top = Counter(words).most_common(20)

# 2. 情感分析（简易词典法）
positive = ["高兴","喜欢","爱","快乐","温暖","美好","幸福"]
negative = ["虐待","坏脾气","暴躁","病","衰老","怕","恨","悲"]

pos_cnt = sum(text.count(w) for w in positive)
neg_cnt = sum(text.count(w) for w in negative)

# 3. 生成 HTML
html = """<html><head><meta charset="utf-8">
<title>文本分析结果</title></head><body>
<h1>文本分析结果</h1>
<h2>最高频词汇 Top 20</h2><ul>"""
for w, c in top:
    html += f"<li>{w}: {c}</li>"
html += "</ul>"
html += f"<h2>情感分布</h2><p>积极词：{pos_cnt} 次，消极词：{neg_cnt} 次</p>"
html += "</body></html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("完成，已生成 index.html")
print("高频词：", top)
print("积极：", pos_cnt, "消极：", neg_cnt)