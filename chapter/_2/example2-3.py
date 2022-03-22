import re

# 匹配换行符
exam = "\n"

str1 = '''http://www.1000phone.com
        http://www.codingke.com'''  # str1字符串包含换行符
ret = re.search(exam, str1)  # search 函数陪陪正则表达式

print(ret)
