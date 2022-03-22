import urllib.request
import urllib.error

# 使用HTTPError类处理非HTTPError异常
try:
    urllib.request.urlopen("http://www.xyxyxy.cn")  # 爬不存在的URL
except urllib.error.HTTPError as e:  # 主动捕获异常
    print(e.reason)  # reason属性是个元组(错误号，错误信息)
