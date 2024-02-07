from urllib import request
from urllib import parse
from fake_useragent import UserAgent
# 拼接url
def get_url(word):
  url = 'http://www.baidu.com/s?wd={}'
  # 要搜索的内容=
  params = parse.quote(word)
  full_url = url.format(params)
  return full_url
# 发送请求，保存数据到本地文件
def request_url(url, filename):
  # 向url发送请求
  # 重构请求头
  headers = {
    'User-Agent': UserAgent().chrome
  }
  print(url)
  # 创建请求对象
  req = request.Request(url=url, headers=headers)
  # 获取响应对象
  res = request.urlopen(req)
  print(res)
  # 获取响应内容
  html = res.read().decode('utf-8')
  # 将获取的数据保存在本地
  filename = word+'.html'
  with open(filename, 'w', encoding='utf-8') as file_obj:
    file_obj.write(html)

# 主程序入口
if __name__ == '__main__':
  word = input('请输入你要搜索的内容： ')
  url = get_url(word)
  filename = word + '.html'
  request_url(url, filename)