class Student(object):
  def __init__(self, name, score, sex):
    self.__name = name
    self.__score = score
    self.__sex = sex
  @property
  def name(self):
    print("我被访问了")
    return self.__name
  
  @name.setter
  def name(self, name):
    print("我被调用了")
    if len(name) > 1:
      self.__name = name
    else:
      print("name的长度必须大于一个字符")
  
  @property
  def score(self):
    return self.__score

yuan = Student("he", 100, 'man')

yuan.name = "chenglong"
print(yuan.name)