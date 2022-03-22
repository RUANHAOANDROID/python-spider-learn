import re

# 边界限制元字符的使用
exam1 = "^codingke"  # 以codingke开头
exam2 = "^codingkee"  # 以codingkee开头
exam3 = "ke$"  # 以ke结尾
exam4 = "_jy$"  # 以_js结尾
str1 = "codingke_jy"
ret1 = re.search(exam1, str1)
ret2 = re.search(exam2, str1)
ret3 = re.search(exam3, str1)
ret4 = re.search(exam4, str1)

print(ret1)
print(ret2)
print(ret3)
print(ret4)
