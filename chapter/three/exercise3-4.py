import requests  # 导入 urllib.request模块

# 第三章练习题 使用requests爬取并打印千烽官网数据
url = 'http://www.1000phone.com'
qf = requests.get(url)
print(qf.text)
print(qf.encoding)
