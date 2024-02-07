import re
html = """
<div><p>www.baid.com</p></div>
<div><p>Python案例</p></div>
"""
# 非贪婪模式匹配， re.S可以匹配换行符
pattern = re.compile('<div><p>.*?</p></div>',re.S)
re_list = pattern.findall(html)
print(re_list)
# 贪婪模式
pattern = re.compile('<div><p>.*</p></div>',re.S)
b_list = pattern.findall(html)
print(b_list)


# 正则表达式分组

website = "绝对零度 https://holazero.cn/"
# 提取所有信息，涉及到.的，需要使用\.转移

pattern_a = re.compile('\w+\s+\w+://\w+\.\w+')
print(pattern_a.findall(website))
pattern_b = re.compile('(\w+)\s+\w+://\w+\.\w+')
print(pattern_b.findall(website))
pattern_c = re.compile('(\w+)\s+(\w+://\w+\.\w+)')
print(pattern_c.findall(website))
# 

# 提取网页信息
html="""
<div class="movie-item-info">
<p class="name">
<a title="你好，李焕英">你好，李焕英</a>
</p>
<p class="star">
主演：贾玲,张小斐,沈腾
</p>    
</div>
<div class="movie-item-info">
<p class="name">
<a title="刺杀，小说家">刺杀，小说家</a>
</p>
<p class="star">
主演：雷佳音,杨幂,董子健,于和伟
</p>    
</div> 
"""
# 寻找html规律，使用正则表达式获取信息
pattern_html = re.compile('<div.*?<a title="(.*?)".*?star">(.*?)</p>.*?</div>', re.S)
r_list = pattern_html.findall(html)
print(r_list)
if r_list:
  for info in r_list:
    print("电影名称：" + info[0])
    print("电影主演：" + info[1].strip())
    print(30*"--")