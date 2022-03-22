import re

# 模式选择的使用
exam1 = "python|java"  # 用于匹配python或java
str1 = "adcdefgpython666java"  # 定义字符串
ret1 = re.search(exam1, str1).group() # group()调出第一个匹配结果 ,pthon出现在前面则匹配出python
print(ret1)
