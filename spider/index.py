# import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com/')
# print(response)
# # 上述代码会返回百度首页的响应对象， 其中 urlopen() 表示打开一个网页地址。注意：请求的 url 必须带有 http 或者 https 传输协议。
# # 输出结果
# # <http.client.HTTPResponse object at 0x00000222F56ABF10>

# # 获取百度首页代码
# from urllib import request
# response = request.urlopen('https://holazero.cn/')
# print(response)
# html = response.read().decode('utf-8')
# print(html)

# 重构爬虫user-agent信息
from urllib import request
url = 'http://httpbin.org/get'
# 重构请求头
headers = {
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'
}
# 创建请求对象，包装ua信息
req = request.Request(url = url, headers=headers)
# 发送请求，获取响应对象
res = request.urlopen(req)
# 获取响应内容
html = res.read().decode('utf-8')
print(html)