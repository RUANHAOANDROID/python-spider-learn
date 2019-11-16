import re

# 使用通用字符陪陪字符串
exam = "\w\dcodingke\w"  # w表示字母数字或下划线、\d表示任意的十进制数[0-9]
str1 = "adbcdasdase1231z4codingke_asd"
ret = re.search(exam, str1)
print(ret)
