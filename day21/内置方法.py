# __名字__
    #类中的特殊方法\内置方法
    #双下方法
    #魔术方法 magic_method

#   类中的每一个双下方法都有它自己的特殊意义


# __call__  相当于对象（）
# __new__   特别重要 开辟内存空间的类的构造方法
    # 写一个单例类
#__len__    len（obj）
#__str__  str（obj），'%s'%obj ，print（obj）

#  所有的双下方法 没有 需要你在外部直接调用的
#  而是总有一些其他的 内置函数 特殊的语法 来自动触发这些 内置方法

# class A:
#     def __call__(self, *args, **kwargs):
#         print("执行call方法了")
#     def call(self):
#         print("执行call方法了")
#
# class B:
#     def __init__(self,cls):
#         print("在实例化A之前做一些事情")
#         self.a = cls()
#         self.a()
#         print("在实例化A之后做一些事情")
#
# # a = A()
# # a() #相当于调用__call__方法
# # A()() 和上面一样
#
# B(A)


# def iter(obj):
#     return  obj.__iter__()

# l = [1,2,3]
# iter(l) # l.__iter__()

#__len__
#内置函数和内置方法是有奸情的

# class mylist():
#     def __init__(self):
#         self.lst = [1,2,3,4,5,6]
#         self.name = 'alex'
#         self.age = 83
#     def __len__(self):
#         print("执行__len__了")
#         return len(self.__dict__)
#
# l = mylist()
# print(len(l))

#len（obj）相当于调用了obj的__len__方法
#__len__方法return的值就是len函数的返回值
#如果一个obj对象没有__len__方法，那么len函数会报错
# print(l.lst)

#练习
# class A:
#     def __init__(self,name):
#         self.name=name
#     def __len__(self):
#         return len(self.name)
#
# print(len(A('alex')))

#__new__    # ==>构造方法
#__init__  # ==>初始化方法

# class Single:
#     def __new__(cls, *args, **kwargs):
#
#         obj = object.__new__(cls)
#         print('在new方法里',obj)
#         # return super().__new__(cls)
#         return obj
#     def __init__(self):
#         print('在init方法里',self)

#1.开辟一个空间，属于对象的
#2.把对象的空间传个self，执行init
#3.将这个对象的空间返回给调用者
# obj = Single()
#single的new，single没有，只能调用object的new方法
#new方法在什么时候执行？？
    #在实例化之后，__init__之前先执行new来创建一片空间

#单例类
#如果一个类，从头到尾只有一个实例，说明从头到尾只开辟一个空间
# class Single:
#     __ISINCTANCE = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__ISINCTANCE:
#             cls.__ISINCTANCE = object.__new__(cls)
#         return cls.__ISINCTANCE
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# s1 =Single('alex',83)
# s2 =Single('taibai',40)
# print(s1.name)
# print(s2.name)

#__str__
# l=[1,2,3] #实例化一个list的对象
#l是个对象

# class A:pass
# a = A()
# print(a)

class Student:
    def __str__(self):
        print("在__str__里面打印")
        return  self.name
    def __init__(self,name):
        self.name = name

s1 = Student('alex')
# print(s1)

#print一个对象相当于调用了一个对象的__str__方法
# str(s1) #str相当于执行了__str__
print('%s'%s1) #相当于执行了s1的__str__
