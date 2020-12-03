class Person:
    mind = '思想' #静态变量，静态字段
    animai = '高级动物'

    def __init__(self,name,age):  #构造方法
        self.name = name
        self.age = age

    def work(self):  #方法，动态变量
        print('都会工作...')

# 类名角度

    # 操作静态字段

        #1，查询类中的全部内容
# print(Person.__dict__)
        #2,万能的点 。
# print(Person.mind) #查询类中的全部内容
# Person.money = '货币' #增
# Person.animai = '低等动物' #改
# del Person.mind   #删

    #操作类中的方法（除了类方法，静态方法 需要类名调用之外，剩下方法都要对象调用）
# print(Person.__dict__)

#对象的角度
obj = Person('alex',1000)  #实例化过程，产生了一个实例（对象）

# 1，创建了一个对象空间，实例空间
# 2，自动执行 __init__方法，并将我的对象空间传给self
# 3，执行具体的__init__,给对象空间封装属性


    # 操作静态字段
        # 1，查询对象空间全部的内容
print(obj.__dict__)
        #2,万能的 点。 增删改查
print(obj.name)
print(obj.mind)
        #操作类中的方法 对象.方法名（）
