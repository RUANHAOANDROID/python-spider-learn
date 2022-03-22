import urllib.request
import urllib.error

# 使用URLError处理HTTPError异常
try:
    urllib.request.urlopen("http://www.1000phone.cc")  # 爬不存在的URL
except urllib.error.URLError as e:
    if hasattr(e, 'code'): # 使用hasattr判断e中是否有code属性
        print(e.code)
    print(e.reason)
