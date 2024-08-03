import re
from collections import defaultdict

def wordcount(text):
    # 将文本转换为小写
    text = text.lower()
    # 使用正则表达式提取单词（忽略标点符号）
    words = re.findall(r'\b\w+\b', text)
    # 创建一个字典用于计数单词出现次数
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    return dict(word_counts)

# 格式化输出函数
def format_output(output, example_number):
    print(f"示例{example_number}的输出：")
    for word, count in sorted(output.items()):
        print(f"{word}: {count}")
    print("\n")

# 示例1输入
input_text_1 = """Hello world!  
This is an example.  
Word count is fun.  
Is it fun to count words?  
Yes, it is fun!"""

output_1 = wordcount(input_text_1)
format_output(output_1, 1)

# 示例2输入
input_text_2 = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

output_2 = wordcount(input_text_2)
format_output(output_2, 2)
