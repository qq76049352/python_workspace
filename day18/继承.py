# 面向对象的三大特性：继承 多态 封装

# 继承

# class Animal:
#     breath = '呼吸'
#
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self):
#         print('动物都要进食')
#
# class Cat(Animal): #括号里面的 父类，基类，超类  #括号外子类，派生类
#     pass
#
# #初识继承：子类以及子类实例化的对象 可以访问父类的任何方法和变量
#     #类名可以访问父类的所有内容
# Cat.eat(111)
# print(Cat.breath)
# p1 = Cat('alex','men',18)
#     #子类实例化的对象也可以访问父类的所有内容
# print(p1.breath)

# 查询顺序

# 写三个类：狗，猫，鸡 每个类中都有吃喝，自己的方法
class Animal:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self):
        print("%s吃东西" % self.name)

    def drink(self):
        print("%喝东西" % self.name)


class Cat(Animal):
    # def eat(self):  #只执行自己类中的方法
    #     print(666)
    def miaow(self):
        print('喵喵叫')

class Dog(Animal):
    def bark(self):
        print('嗷嗷叫')

class Chook(Animal):
    def crow(self):
        print("大爷laiwanya")

# cat1= Cat('tom','公',3)
# cat1.eat()
#只执行父类的方法：子类中不要定义与父类同名的方法