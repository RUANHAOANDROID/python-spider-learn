import urllib.request
import urllib.error

# HTTPError异常中答应状态吗出错
try:
    urllib.request.urlopen("http://www.1000phone.com/1")  # 爬不存在的URL
except urllib.error.HTTPError as e:  # 主动捕获异常
    print(e.code)  # 输出状态码
    print(e.reason)  # 输出异常原因
