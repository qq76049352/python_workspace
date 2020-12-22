# __名字__
    #类中的特殊方法\内置方法
    #双下方法
    #魔术方法 magic_method

#   类中的每一个双下方法都有它自己的特殊意义


# __call__ flask django
# __new__
    # 写一个单例类
#__len__
#__str__/__repr

class A:
    def __call__(self, *args, **kwargs):
        print("执行call方法了")
    def call(self):
        print("执行call方法了")

class B:
    def __init__(self,cls):
        print("在实例化A之前做一些事情")
        self.a = cls()
        self.a()
        print("在实例化A之后做一些事情")

# a = A()
# a() #相当于调用__call__方法
# A()() 和上面一样

B(A)

