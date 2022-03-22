import urllib.request  # 导入 urllib.request模块

# 将响应对象复制给变量phone_file
phone_file = urllib.request.urlopen("http://www.1000phone.com")
# 读取所有的内容，以UTF-8编码
phone_data = phone_file.read().decode("UTF-8")
# 只读取一行内容
phone_dataLine = phone_file.readline()
# 打印页面
print(phone_data)
# 打印行
print(phone_dataLine)
