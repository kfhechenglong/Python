from urllib import request
import re
import time
import gzip
import random
import csv
from ua_info import ua_list
# 抓取猫眼电影经典影片排行

# 确定要抓取的页面元素规律
# 在抓取数据之前，我们需要通过页面审查元素来找到页面数据的规律，看看自己需要的数据有什么规律可循，抓取哪些信息最合适
# 通过审查元素我们可以知道，每个影片的信息都在一个dd标签中
html = '<dd> <div class="movie-item film-channel"> <a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <div class="movie-poster"><img class="poster-default" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png"><img alt="热辣滚烫海报封面" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/160/h/220"></div></a><div class="movie-ver"><i class="imax2d"></i></div><div class="movie-item-hover"><a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <img class="movie-hover-img" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/218/h/300" alt="热辣滚烫"><div class="movie-hover-info">  <div class="movie-hover-title" title="热辣滚烫">    <span class="name ">热辣滚烫</span>      <span class="score channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></span>  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">类型:</span>    喜剧／剧情  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">主演:</span>    贾玲／雷佳音／张小斐  </div>  <div class="movie-hover-title movie-hover-brief" title="热辣滚烫">    <span class="hover-tag">上映时间:</span>    2024-02-10 09:00  </div></div></a></div></div><div class="channel-detail movie-item-title" title="热辣滚烫"><a href="/films/1478901" target="_blank" data-act="movies-click" data-val="{movieId:1478901}">热辣滚烫</a></div><div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div><dd> <div class="movie-item film-channel"> <a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <div class="movie-poster"><img class="poster-default" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png"><img alt="热辣滚烫海报封面" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/160/h/220"></div></a><div class="movie-ver"><i class="imax2d"></i></div><div class="movie-item-hover"><a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <img class="movie-hover-img" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/218/h/300" alt="热辣滚烫"><div class="movie-hover-info">  <div class="movie-hover-title" title="热辣滚烫">    <span class="name ">热辣滚烫</span>      <span class="score channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></span>  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">类型:</span>    喜剧／剧情  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">主演:</span>    贾玲／雷佳音／张小斐  </div>  <div class="movie-hover-title movie-hover-brief" title="热辣滚烫">    <span class="hover-tag">上映时间:</span>    2024-02-10 09:00  </div></div></a></div></div><div class="channel-detail movie-item-title" title="热辣滚烫"><a href="/films/1478901" target="_blank" data-act="movies-click" data-val="{movieId:1478901}">热辣滚烫</a></div><div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div><dd> <div class="movie-item film-channel"> <a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <div class="movie-poster"><img class="poster-default" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png"><img alt="热辣滚烫海报封面" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/160/h/220"></div></a><div class="movie-ver"><i class="imax2d"></i></div><div class="movie-item-hover"><a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}"> <img class="movie-hover-img" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/218/h/300" alt="热辣滚烫"><div class="movie-hover-info">  <div class="movie-hover-title" title="热辣滚烫">    <span class="name ">热辣滚烫</span>      <span class="score channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></span>  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">类型:</span>    喜剧／剧情  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">主演:</span>    贾玲／雷佳音／张小斐  </div>  <div class="movie-hover-title movie-hover-brief" title="热辣滚烫">    <span class="hover-tag">上映时间:</span>    2024-02-10 09:00  </div></div></a></div></div><div class="channel-detail movie-item-title" title="热辣滚烫"><a href="/films/1478901" target="_blank" data-act="movies-click" data-val="{movieId:1478901}">热辣滚烫</a></div><div class="channel-detail channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></div>'

#   </dd>
# 通过分析上面的页面元素，我们发现在鼠标hover时，信息最为完整，具体如下：
"""
<div class="movie-item-hover">
  <a href="/films/1478901" target="_blank" data-act="movie-click" data-val="{movieid:1478901}">
      <img class="movie-hover-img" src="https://p0.pipi.cn/mmdb/54ecdebe51bddd030c1789a49a18089e5bcaf.jpg?imageView2/1/w/218/h/300" alt="热辣滚烫">
    <div class="movie-hover-info">
      <div class="movie-hover-title" title="热辣滚烫">
        <span class="name ">热辣滚烫</span><span class="score channel-detail-orange"><i class="integer">9.</i><i class="fraction">4</i></span>
      </div>
      <div class="movie-hover-title" title="热辣滚烫">
        <span class="hover-tag">类型:</span>
        喜剧／剧情
      </div>
      <div class="movie-hover-title" title="热辣滚烫">
        <span class="hover-tag">主演:</span>
        贾玲／雷佳音／张小斐
      </div>
      <div class="movie-hover-title movie-hover-brief" title="热辣滚烫">
        <span class="hover-tag">上映时间:</span>
        2024-02-10 09:00
      </div>
    </div>
  </a>
</div>
"""
# 确定url的规律
# 另外我们发现页面url的规律，每次一页回显30条数据
# https://www.maoyan.com/films?showType=3&offset=60
# https://www.maoyan.com/films?showType=3&offset=60
# showType=1 正在热映，showType=2 即将上映，showType=3 经典影片
# offset为以30位倍数递增

# 编写爬虫程序

# 定义一个爬虫类
class MaoYanMoviesSpider(object):
  # 初始化
  # 定义初始化页面url
  def __init__(self):
    self.url = 'https://www.maoyan.com/films?showType=2&requestCode=3f1975a82e8c7434b2ca34fa5aa7b847udgon'
  # 定义请求函数
  def get_html(self,url):
    # headers = {
    #    'User-Agent':random.choice(ua_list),
    #    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Pragma':'no-cache',
    # 'Connection':'keep-alive',
    # 'Upgrade-Insecure-Requests':'1',
    # 'Cookie':'__mta=107256253.1708421428031.1708672050303.1708672057726.27; uuid_n_v=v1; uuid=A7F99EA0CFD211EE8FC9879C0B12C6E7AE8D16FA0C5D4F43A0F799EBD66F183C; _lxsdk_cuid=182443f653ec8-0933e86dc522b6-4343363-1fa400-182443f653ec8; _lxsdk=A7F99EA0CFD211EE8FC9879C0B12C6E7AE8D16FA0C5D4F43A0F799EBD66F183C; _csrf=4c8cf3f25c38d1a1c05950c5030b69a0e188a620cb75ba4bb17090544e45b544; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1708421417,1708671973; __mta=107256253.1708421428031.1708672057726.1708673218695.28; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1708673222; _lxsdk_s=18dd4c9355b-84-578-e82%7C%7C44',
    # }
    # req = request.Request(url)
    # res = request.urlopen(req)
    # html = self.unGzip(res.read()).decode()
    self.parse_html(html)
    # with open('./1.html','r',encoding='utf-8') as file:
    #   self.parse_html(file.read())
  # 解析函数
  def parse_html(self,html):
    # print(html)
    #  定义正则表达式
    re_partten = '<dd>.*?class="movie-hover-title" title="(.*?)".*?class="score channel-detail-orange">(.*?)</span>.*?(class="hover-tag">.*?</div></div>)'
    pattern = re.compile(re_partten, re.S)
    try:
      r_list = pattern.findall(html)
      self.save_html(r_list)
    except Exception as e:
      print("错误:",e)
  # 保存数据
  def save_html(self,r_list):
    print(r_list)
    #  整理数据
    # [('热辣滚烫', '<i class="integer">9.</i><i class="fraction">4</i>', 'class="hover-tag">类型:</span>    喜剧／剧情  </div>  <div class="movie-hover-title" title="热辣滚烫">    <span class="hover-tag">主演:</span>    贾玲／雷佳音／张小斐  </div>  <div class="movie-hover-title movie-hover-brief" title="热辣滚烫">    <span class="hover-tag">上映时间:</span>    2024-02-10 09:00  </div></div>')]
    with open('maoyan.csv','a',newline='',encoding="utf-8") as f:
      fieldnames = ['电影名称', '电影评分','类型','主演','上映时间']
      writer = csv.DictWriter(f,fieldnames=fieldnames)
      # 写入字段名，当做表头
      writer.writeheader()
      for r in r_list:
        name = r[0].strip()
        print('电影名称：{}'.format(name))
        # 解析评分
        score_partten = '<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>'
        score_l = re.compile(score_partten, re.S).findall(r[1])
        score = str(score_l[0][0]) + str(score_l[0][1])
        print('电影评分：{}'.format(score))
        # 其它信息
        other_partten = 'class="hover-tag">(.*?)</span>(.*?)</div>'
        other_info_l = re.compile(other_partten, re.S).findall(r[2])
        cols = {'电影名称': name,'电影评分':score,'类型':'','主演':'','上映时间':''}
        for info in other_info_l:
          key = info[0].strip()
          value = info[1].strip()
          if key == '类型:':
             cols['类型'] = value
          elif key == '主演:':
            cols['主演'] = value
          elif key == '上映时间:':
            cols['上映时间'] = value
        print(cols)
        writer.writerow(cols)

  def unGzip(self,page):
    # 解决压缩包格式
    try:
        data = gzip.decompress(page)
    except:
        pass
    return data
  def run(self):
    #  for offset in range(0,)
    url = self.url.format(30)
    self.get_html(url)

# 主程序入口
if __name__ == '__main__':
  try:
      spider = MaoYanMoviesSpider()
      spider.run()
  except Exception as e:
      print("错误:",e)