import csv
# csv文件的写入
# 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象
with open('eggs.csv','w',newline='') as csvfile:
  # delimiter 指定分隔符，默认为逗号，这里指定为空格
  # quotechar表示引用符
  # writerow 单行写入，列表格式传入数据
  spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
  spamwriter.writerow(['www.baidu.com'] * 5 + ['how are you'])
  spamwriter.writerow(['hello world', 'web site', 'www.baidu.com'])
  spamwriter.writerows([('hello', 'world'),('I', 'love', 'you')])
# 以字典的方式读写数据
with open('names.csv', 'w', newline='') as csvfile:
  fieldnames = ['first_name', 'last_name']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  # 写入字段名，当做表头
  writer.writeheader()
  # 写入多行
  writer.writerows([{'first_name':'He', 'last_name':'chenglong'},{'first_name':'Juedui', 'last_name':'lingdu'}])
  # 写入单行
  writer.writerow({'first_name':'22', 'last_name':'333'})
# csv文件的读取
with open('eggs.csv', 'r', newline='') as csvfile:
  spamwriter = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamwriter:
    print(', '.join(row))
with open('names.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row['first_name'], row['last_name'])
