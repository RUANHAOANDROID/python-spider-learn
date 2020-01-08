import urllib.request
import urllib.error

# 使用HTTPError类处理非HTTPError异常
try:
    urllib.request.urlopen("http://www.1000phone.cc")  # 爬不存在的URL
except urllib.error.HTTPError as e:  # 先用子类异常处理
    print(e.code)
    print(e.reason)  # reason属性是个元组(错误号，错误信息)
except urllib.error.URLError as e:  # 再用父类异常处理
    print(e.reason)
