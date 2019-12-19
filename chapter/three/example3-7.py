# 使用异常处理模块处理URL不存在异常
import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://1000phone.com/1")  # 爬取错误的URL
except urllib.error.URLError as e:  # 主动捕捉异常
    print(e.code)  # 输出异常状态码
    print(e.reason)  # 输出异常原因
