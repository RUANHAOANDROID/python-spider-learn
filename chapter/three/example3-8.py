import urllib.request
import urllib.error

# URLError异常中答应状态吗出错
try:
    urllib.request.urlopen("http://www.xyxy.com")  # 爬不存在的URL
except urllib.error.URLError as e:  # 主动捕获异常
    print(e.code)  # 输出状态码
    print(e.reason)  # 输出异常原因
