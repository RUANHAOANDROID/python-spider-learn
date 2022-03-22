from bs4 import BeautifulSoup

# BeautifulSoup 的4种节点对象的使用

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<b><!---Hey,buddy,Want to buy a used parser?--></b>
<p Class ="title">
<hr>
<center>剧中标题</center>
<hr>
<hr>
<ul>
    <li>扣丁学堂</li>
    <li>大晚上学python</li>
</ul>
<ol type="A">
    <li>扣丁学堂</li>
    <li>大晚上学python</li>
</ol>
<div>
    <h3>该传秋裤了</h3>
    <p>今天买了优衣库的秋裤</P>
</div>
<dl>
    <dt>帮助</dt>
    <dd>学习交流</dd>
</dl>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")
tag = soup.title  # 获取标签
string = tag.string  # 获取内容
comment = soup.b.string  # 获取b标签的注释文字内容
print(type(soup))
print(type(tag))
print(type(string))
print(type(comment))
