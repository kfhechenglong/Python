class Person:
  def __init__(self, name):
    self.__name = name
  
  def __get_name(self):
    print("getter")
    return self.__name
  
  def __set_name(self, name):
    print("setter")
    self.__name = name
  
  def __del_name(self):
    print("del")
    del self.__name
  
  name = property(__get_name, __set_name, __del_name)

yuan = Person("hechenglong")

print(yuan.name)
yuan.name = "jueduilingdu"

del yuan.name

print(yuan.__dict__)