import re

# 任意匹配元字符
exam = "codingke..."
str1 = "aaa66codingke666666"
ret = re.search(exam, str1)
print(ret)
