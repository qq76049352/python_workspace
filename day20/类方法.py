#类方法
# class A:
#     def func(self): #普通方法
#         print(self)
#
#
#     @classmethod
#     def func1(cls): #类方法
#         print(cls)
#
# # a1 = A()
# # a1.func()
# A.func1()
#
#
# a1 = A()
# a1.func1()#对象调用方法，cls得到是类本身
#类方法：通过类名调用的方法，类方法中第一个参数约定俗称cls，python自动将类空间传给cls

#类方法的应用场景：
#1，类中有些方法是不需要对象参与

# class A:
#     name = 'alex'
#     count = 1
#
#     @classmethod
#     def func1(cls): #此方法无需对象参与
#         return  cls.name + str(cls.count + 1)

# A.func1(1)#不可取

# a1 = A()
# print(a1.func1())

# print(A.func1())


#2，对类中的变量进行改变，要用到类方法

#3，继承中，父类得到子类的类空间

# class A:
#     age = 12
#
#     @classmethod
#     def func1(cls): #此方法无需对象参与
#         # print(cls)
#         #对B类的所有内容进行修改。
#         print(cls.age)
#         # return  cls.name + str(cls.count + 1)
#     def func2(self):
#         print(self)
#
# class B(A):
#     age = 22
#     pass
#
# # B.func1()
# b1 = B()
# b1.func2()

#静态方法
class A:
    @staticmethod
    def func():
        print(666)

A.func()

# def login(username,password):
#     if username == 'alex' and password == 123:
#         print("登录成功")
#     else:
#         print("登录失败")
#
# login('alex',1234)

# 1,代码块。清晰
# 2，复用性，
