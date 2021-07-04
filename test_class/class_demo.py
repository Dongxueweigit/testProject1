# Author：DongXuewei
# Time  ：2021/7/4 6:53

# 创建一个人类，通过关键字“class 类名：”的方式进行定义
class Person:
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    """def set_name(self,name):
        self.name = name #self.name是类中的属性，name是外部传进来的参数
    def set_age(self,age):
        self.age = age"""

    def __init__(self, name, age, gender, weigth):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weigth

    def eat(self):
        print("eating")

    def play(self):
        print("playing")

    def jump(self):
        print("junping")


# 实例化一个对象张三，通过 “实例队形名=类名()”的方式进行实例化
# 对张三调用类中定义的属性和方法，通过“实例对象名.类方法”的方式完成（有括号的是方法，没有括号的是属性）
"""zs = Person()
zs.set_name("zhangsan")
zs.set_age(18)"""

zs = Person("zhangsan", 20, "男", 100)
print(f"张三的姓名：{zs.name}\n张三的年龄：{zs.age}")
