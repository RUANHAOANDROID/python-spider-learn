import urllib.request  # 导入 urllib.request模块
import ssl  # 导入ssl模块

douban_url = "https://www.douban.com/"
# 把证书验证改成不用验证
ssl._create_default_https_context = ssl._create_unverified_context
# 保存网页
douban_html_file =urllib.request.urlretrieve(douban_url,"douban.html")

