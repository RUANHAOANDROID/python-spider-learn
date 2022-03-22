import re

# 原子表的使用
exam = "\w\docdingke[xyz]\w"  # \w字母 、数字、下划线.\d 十进制数，含有xyz
exam1 = "\w\dcodingke[^xyz]"  # 【^zxy】除x,y,z意外
exam2 = "\w\dcodingke[xyz]\w"  # \w除字母、数字、下划线外
str1 = "1000phone6codingke_666"
ret = re.search(exam, str1)
ret1 = re.search(exam1, str1)
ret2 = re.search(exam2, str1)
print(ret)
print(ret1)
print(ret2)
