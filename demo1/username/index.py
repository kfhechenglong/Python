# 获取文件内容

f = open('./user.text','r+', encoding='utf-8')
user_info = {}
line = f.readlines()
for i in line:
  print(i.strip())
  info = i.strip().split(',')
  user_info[info[0]] = i.strip()
print(user_info)
while True:
  name  = input('请输入用户名：')
  if name not in user_info:
    print('用户不存在')
    continue
  count = 0
    # 密码错误三次则锁定账户信息
  while count < 3:
    password = input('请输入密码：')
    user_pwd = user_info[name].split(',')[1]
    if password == user_pwd:
      print('登录成功')
      f.close()
      exit()
    else:
      print('密码错误')
      count += 1
      if count == 3:
        print('账户锁定')
        # 重写文件内容
        info = user_info[name].split(',')
        info[2] = '1'
        user_info[name] = ','.join(info)
        print(user_info)
        f2 = open('./user.text','w+', encoding='utf-8')
        for user,val in user_info.items():
          f2.write(val+'\n')
        f.close()
        exit()