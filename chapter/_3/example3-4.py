import ssl
import urllib.request

# 解决关键字是中文的编码问题

keywd ="开发" #使用中文查询
keycode =urllib.request.quote(keywd) # 对中文关键字编码
url = "http://www.codingke.com/search/course?keywords="+keycode

req =urllib.request.Request(url)
data =urllib.request.urlopen(req).read()
fhandle =open("dev.html","wb")
fhandle.write(data)
fhandle.close()
