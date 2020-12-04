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
# class Animal:
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def eat(self,food):
#         print("%s吃%s" % (self.name,food))
#
#     def drink(self):
#         print("%喝东西" % self.name)
#
#
# class Cat(Animal):
#     # def eat(self):  #只执行自己类中的方法
#     #     print(666)
#     def miaow(self):
#         print('喵喵叫')
#
#
# class Brid(Animal):
#     def __init__(self, name, sex, age, wing):
#         super().__init__(name, sex, age)
#         # super(Brid, self).__init__(name,sex,age)
#         # Animal.__init__(self, name, sex, age)
#         self.wing = wing
#
#     def bark(self):
#         print('嗷嗷叫')
#
#     def eat(self,food):
#         # Animal.eat(self)
#         # super(Brid, self).eat()
#         super().eat(food)
#         print("鸟也会吃啊")
#
#
# class Chook(Animal):
#     def crow(self):
#         print("大爷laiwanya")
#
#
# # cat1= Cat('tom','公',3)
# # cat1.eat()
# # 只执行父类的方法：子类中不要定义与父类同名的方法
# # 只执行子类的方法：在子类中定义与父类同名的方法
# # 既要执行父类的方法，也要执行子类的方法？
# # 两种解决方法：
# # L
# b1 = Brid('鹦鹉', '公', 20, '绿翅膀')
# print(b1.__dict__)
# b1.eat('虫子')

# 继承的进阶
# 继承：单继承，多继承

# 类：经典类，新式类
# 新式类:凡是继承object类都是新式类
    # python3x 所有类都是新式类,因为Python3x中的类都默认继承object
# class A:
#     pass
# 经典类：不继承object类都是经典类
    # python2x所（既有新式类，又有经典类）有的类都不继承object类，所有的类默认都是经典类，你可以让其继承object

# 单继承：新式类，经典类查询顺序一样。

# class A:
#     def func(self):
#         print('IN A')
#
# class B(A):
#     def func(self):
#         print('IN B')
#
# class C(B):
#     # def func(self):
#     #     print('IN c')
#     pass
#
# c1 = C()
# c1.func()

# 多继承：
    # 新式类：遵循广度优先。广度优先：每个节点有且直走一次
    # 经典类：遵循深度优先。深度优先：一条路走到底

#多继承的新式类：广度优先：一条路走到倒数第二级，判断，如果其他路能走到终点，则返回走另一条，如果不能，则走到终点
# class A:
#     def func(self):
#         print('IN A')
#
# class B(A):
#     # def func(self):
#     #     print('IN B')
#     pass
#
# class C(A):
#     def func(self):
#         print('IN c')
#
# class D(B):
#     # def func(self):
#     #     print('IN D')
#     pass
#
# class E(C):
#     def func(self):
#         print('IN E')
#
# class F(D,E):
#     # def func(self):
#     #     print('IN F')
#     pass
#
# f1 = F()
# f1.func()
# print(F.mro())  #查询类的继承顺序

#多继承的新式类：广度优先