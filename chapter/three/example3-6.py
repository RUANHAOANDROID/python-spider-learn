import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://www.xyxyxy.cn")  # 爬去不存在的链接
except urllib.error.URLError as e:  # 主动捕获
    print(e.reason)  # 输出异常
