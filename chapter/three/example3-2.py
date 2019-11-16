import ssl
import urllib.request

# 获取网页信息、状态吗、地址等

ssl._create_default_https_context = ssl._create_unverified_context
for i in range(1, 10):
    try:
        file = urllib.request.urlopen("http://www.codingke.com", timeout=3)  ##设置网页超时时间
        data = file.read()
        print(len(data))  # 打印爬去内容的长度
    except Exception as e:
        print("异常了```" + str(e))
