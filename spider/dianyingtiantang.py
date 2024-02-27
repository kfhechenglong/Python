# -*- coding: utf-8 -*-
from urllib import request
import re
import csv
import random
from bs4 import BeautifulSoup
from hashlib import md5
from ua_info import ua_list
import sys
class MovieSkySpider(object):
    def __init__(self):
        self.url = 'https://www.dygod.net/html/gndy/china/index_2.html'
        self.count = 0
        # self.db = pymysql.connect(
        #     'localhost','root','123456','movieskydb',
        #     charset='utf8'
        # )
        # self.cursor = self.db.cursor()
    # 1.请求函数
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        print(url)
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        # 本网站使用gb2312的编码格式
        html = res.read().decode('gb2312', 'ignore')
        print(html)
        soup = BeautifulSoup(html, 'html.parser')
        ret = soup.find_all(class_='tbspan', style='margin-top:6px')
        return ret
    # 2.正则解析函数
    def re_func(self,re_bds,html):
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        return r_list
    
    def getmanget(self, linkurl):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=linkurl, headers=headers)
        res = request.urlopen(req)
        # 本网站使用gb2312的编码格式
        html = res.read().decode('gb2312', 'ignore')
        soup = BeautifulSoup(html, 'html.parser')
        ret = soup.find_all('a')
        for n in ret:
            if 'magnet' in str(n.string):
                return n.string
        return None
  
    # 3.提取数据函数
    def parse_html(self,one_url):
        # 调用请求函数，获取一级页面
        one_html = self.get_html(one_url)
        with open('电影.csv','a',newline='',encoding="utf-8") as f:
          fieldnames = ['电影名称','中文名称', '电影年代','电影产地','类别','下载链接']
          writer = csv.DictWriter(f,fieldnames=fieldnames)
          # 写入字段名，当做表头
          writer.writeheader()
          for x in one_html:
            info = {'电影名称': '','中文名称': '','电影年代':'','电影产地':'','类别':'','下载链接':''}
            a_tags = x.find_all("a")
            info['电影名称'] = a_tags[1].string
            pat = re.compile(r'◎译　　名(.*)\n')
            ret = re.findall(pat, str(x))
            for n in ret:
                n = n.replace(u'\u3000', u'')
                info['中文名称'] = str(n).split('/')[0]
    
            pat = re.compile(r'◎年　　代(.*)\n')
            ret = re.findall(pat, str(x))
            for n in ret:
                n = n.replace(u'\u3000', u'')
                info['电影年代'] = str(n)
    
            pat = re.compile(r'◎产　　地(.*)\n')
            ret = re.findall(pat, str(x))
            for n in ret:
                n = n.replace(u'\u3000', u'')
                info['电影产地'] = str(n).split('/')[0]
    
            pat = re.compile(r'◎类　　别(.*)\n')
            ret = re.findall(pat, str(x))
            for n in ret:
                n = n.replace(u'\u3000', u'')
                info['类别'] = str(n).split('/')[0]
    
            linkurl = 'https://www.dygod.net/' + a_tags[1].get("href")
            manget = self.getmanget(linkurl)
            if manget:
              info['下载链接'] = str(manget)
            writer.writerow(info)
    # 4.判断链接是否已经抓取过
    def is_hold_on(self,finger):
        # 查询数据库
        sql='select finger from request_finger where finger=%s'
        # execute()函数返回值为受影响的行数（即0或者非0）
        r = self.cursor.execute(sql,[finger])
        # 如果为0表示没有抓取过
        if not r:
            return True
    # 5.解析二级页面，获取数据（名称与下载链接）
    def save_html(self,two_url):
        two_html = self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1> \
        </div>.*?<a.*?href="(.*?)".*?>.*?style="BACKGROUND-COLOR:.*?</a>'
        # film_list: [('name','downloadlink'),(),(),()]
        film_list = self.re_func(re_bds,two_html)
        print(film_list)
        # 插入数据库
        # sql = 'insert into movieinfo values(%s,%s)'
        # #L = list(film_list[0])
        # self.cursor.executemany(sql,film_list)
        # self.db.commit()
    
    #主函数 
    def run(self):
        # 二级页面后四页的正则表达式略有不同，需要重新分析
        # for i in range(1,4):
      url = self.url
      self.parse_html(url)
if __name__ == '__main__':
    spider = MovieSkySpider()
    spider.run()