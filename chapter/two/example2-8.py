import re

# 限定符使用
exam1 = "py.*n"  # py到n的任意字符且出现任意次数
exam2 = "cd{2}"  # cd出现2次
exam3 = "cd{3}"  # cd出现3次
exam4 = "cd{2,}"  # cd 重的d出现2次以上
str1 = "abcdddfphp345python_py" #原字符串
ret1 = re.search(exam1, str1)
ret2 = re.search(exam2, str1)
ret3 = re.search(exam3, str1)
ret4 = re.search(exam4, str1)

print(ret1)
print(ret2)
print(ret3)
print(ret4)
