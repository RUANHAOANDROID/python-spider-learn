import re  # 正则表达式

exam = "qianfeng"  # 字符作为原子
str1 = "qianfengdu"  # 需要匹配的字符
ret = re.search(exam, str1)  # 需要匹配的字符串
print(ret)
