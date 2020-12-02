# class file:
#     def __init__(self,name,sex,phone,job):
#         self.name = name
#         self.sex = sex
#         self.phone = phone
#         self.job = job

# 类：具有相同属性和技能的一类事物。
# 人类：
# 对象：具体的类的表现。具体的实实在在的一个实例

# class Person:
#     # 类体：两部分：变量部分，方法（函数）部分
#     mind = '有思想'   #变量，静态变量，静态字段
#     animal = '高级动物'
#     faith = '有信仰'
#     def __init__(self):
#         print(self)
#         print(666)
#
#     # def __init__(self,name,age,sex,hobby):
#     #     print(666)
#
#     def work(self):  #方法，函数，动态变量
#         print("人类都会工作...")
#
#     def shopping(self):
#         print("人类可以消费...")
#
#
# #类名的角度
#     #操作类中的静态变量
#         #1，Person.__dict__ 查询类中的所有的内容（不能进行增删改操作）
# # print(Person.__dict__)
# # print(Person.__dict__['faith'])
# #Person.__dict__['mind']='无脑'  #报错，不能修改
#         #2，万能的  .    对类中的单个的变量进行增删改查，用万能的 点
# # print(Person.mind)
# # print(Person.animal)#查
# # Person.money = '运用货币'#增
# # Person.mind = '无脑' #改
# # del Person.mind      #删
# # print(Person.__dict__)
#
#     #操作类中的方法  (工作当中基本不用类名去操作)
# # Person.work(111)
#
#
# #对象的角度
# ret = Person()  #类名+（）的过程：实例化的过程（创建一个对象的过程），
#         # Person（）实例化对象，实例，对象
# print(ret)
# #1,只要类名+（）产生一个对象，自动执行类中的__init__方法

class Person:
    # 类体：两部分：变量部分，方法（函数）部分
    mind = '有思想'   #变量，静态变量，静态字段
    animal = '高级动物'
    faith = '有信仰'


    def __init__(self,name,age,hobby):
        self.name = name
        self.age =age
        self.hobby=hobby

    def work(self):  #方法，函数，动态变量
        print("人类都会工作...")

    def shopping(self):
        print("人类可以消费...")


#类名的角度
    #操作类中的静态变量
        #1，Person.__dict__ 查询类中的所有的内容（不能进行增删改操作）
# print(Person.__dict__)
# print(Person.__dict__['faith'])
#Person.__dict__['mind']='无脑'  #报错，不能修改
        #2，万能的  .    对类中的单个的变量进行增删改查，用万能的 点
# print(Person.mind)
# print(Person.animal)#查
# Person.money = '运用货币'#增
# Person.mind = '无脑' #改
# del Person.mind      #删
# print(Person.__dict__)

    #操作类中的方法  (工作当中基本不用类名去操作)
# Person.work(111)



ret = Person('alex',1000,'oldwoen')  #类名+（）的过程：实例化的过程（创建一个对象的过程），
        # Person（）实例化对象，实例，对象
print(ret.__dict__)
#1,类名+（）产生一个实例（对象，对象空间）
#2，自动执行类中的__init__方法，将对象空间传给__init__的self参数。
#3 给对象封装相应的属性

#对象的角度
    #操作对象中的静态变量
        #1，__dict__查询对象中的所有的内容
        #2，万能的 点

# ret.high = 175
# del ret.name
# ret.age = 73
# print(ret.__dict__)

    #对象操作类的静态变量：只能查
# print(ret.mind)

    #对象调用类的方法
ret.shopping()


