import ssl
import urllib.request

# 爬扣丁学堂 php课程的网页内容并保存在本地

keywd ="php"
url = "http://www.codingke.com/search/course?keywords="+keywd
req =urllib.request.Request(url)
data =urllib.request.urlopen(req).read()
fhandle =open("php.html","wb")
fhandle.write(data)
fhandle.close()
