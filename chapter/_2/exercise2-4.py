import urllib.request  # 导入 urllib.request模块

# 第二章 练习题 获取文档中所有文字
html = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML显示JSON数据</title>
</head>
<body>
<h2>HTML显示JSON数据</h2>
<p>
    First Name:<span id="fname"></span><br/>
    Last Name:<span id="lname"></span><br/>
</p>
<a href ="http://www.baidu.com" class ="sister" id="link1>百度</a>
<a href ="http://www.github.com" class ="sister" id="link1>github</a>
<p class ="story">...</p>
<script type="text/javascript">
    var txt = '{"firstName":"张","lastName":"三"}'
    var obj = eval ("("+txt+")");
    document.getElementById("fname").innerHTML=obj.firstName
    document.getElementById("lname").innerHTML=obj.lastName
</script>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
context = soup.get_text()
print(context)
