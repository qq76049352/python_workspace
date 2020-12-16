# 属性的初识
# class Person:
#     def __init__(self, name, hight, weight):
#         self.name = name
#         self.__hight = hight
#         self.__weight = weight
#         # self.bmi = self.__weight / self.__hight ** 2
#
#     @property
#     def bmi(self):
#         return '%s 的bmi 值%s'%(self.name,self.__weight/self.__hight ** 2)
#
#
# p1 = Person("张尔博", 1.68, 63.5)
# # print(p1.bmi())
# print(p1.bmi)

#属性：将一个方法 伪装 成一格属性，在代码的级别上没有本质的提升，但是让其看起来更合理


#属性的改
class Person:
    def __init__(self, name, age):
        self.name = name
        if type(age) is int:
            self.__age = age
        else:
            print("你输入的有误")


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a1):
        # print('666')
        if type(a1) is int:
            self.__age = a1
        else:
            print("你输入的有误")

    @age.deleter
    def age(self):
        # print(666)
        del  self.__age

p1 = Person("帅哥",18)
# print(p1.age)
p1.age = 23
print(p1.age)
del p1.age
# property : 类似bmi这种，area，周长。。。  ***
#.setter **
# .deleter *