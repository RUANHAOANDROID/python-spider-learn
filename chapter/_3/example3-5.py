import urllib
import urllib.request


# 使用代理IP爬取网页

# 创建代理函数
def use_proxy(proxy_addr, url):
    # 代理服务器信息
    proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    # 创建opener对象
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data


proxy_addr = '180.167.113.57:86'
data = use_proxy(proxy_addr, "http://www.100phone.com")

print('网页数据长度是：', len(data))
