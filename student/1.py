class Person(object):

    def __init__(self, name, age):
        print("__init__方法执行")
        self.name = name
        self.age = age

    def __str__(self):
        print("__str__方法执行")
        return self.name


yuan = Person("yuan", 23)
print(yuan)