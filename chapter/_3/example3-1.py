import ssl
import urllib.request

# 获取网页信息、状态吗、地址等
ssl._create_default_https_context = ssl._create_unverified_context
file = urllib.request.urlopen("http://www.1000phone.com")
print(file.info())  # 网页信息
print(file.getcode())  # 返回状态码
print(file.geturl())  # 返回url
