import urllib.request
import urllib.parse
import http.cookiejar

login_url = "http://bbs.chinaunix.net/member.php?mod=loging&action=login&loginsubmit=yes&loginhash=L768Q"
login_data = urllib.parse.urlencode({"username": "a877348180", "password": "a123456"}).encode("utf-8")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = urllib.request.Request(login_url, login_data, headers)
# req.add_header("User-Agent",
#                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87")

# req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0")
# cookie 处理第一步：创建Cookiejar对象
cookiejar = http.cookiejar.CookieJar()
# 第二步:以cookie为处理器创建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
# 第三步 : 创建全局opener对象
urllib.request.install_opener(opener)
wb_file = opener.open(req)
wb_data = wb_file.read()
fhandle = open("bbsl.html", "wb")
fhandle.write(wb_data)
fhandle.close()

urllib.request.install_opener(opener)
wb_main_url = "http://account.chinaunix.net/login/sso?url=http%3A%2F%2Fbbs.chinaunix.net%2Fforum-55-1.html"
wb_main_html = urllib.request.urlopen(wb_main_url)
fhandle = open("bbs2.html", "wb")
fhandle.write(wb_main_html.read())
fhandle.close()
