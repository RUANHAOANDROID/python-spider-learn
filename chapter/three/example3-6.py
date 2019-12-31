import urllib.request
import urllib.error

# 使用异常处理模块处理URL不存在异常
try:
    urllib.request.urlopen("http://www.xyxyxy.cn")  # 爬去不存在的链接
except urllib.error.URLError as e:  # 主动捕获
    print(e.reason)  # 输出异常
