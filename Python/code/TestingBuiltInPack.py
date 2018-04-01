import os
import requests

#加载包到项目里

print("当前工作的环境:")
print(os.getcwd())

#抓去并返回一个对象
r = requests.get("https://www.baidu.com")

print(r.url)
print(r.encoding)
print(r.text)