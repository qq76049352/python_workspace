#广义的封装：实例化一个对象，给对象空间封装一些属性。
#狭义的封装：私有制。
#私有成员，私有方法，私有对象属性

# 私有静态字段
class A:
    name = 'alex'
    __age = 1000

    def func(self):
        print("func...")

a1 = A()
print(a1.name)
print(A.name)
print(a1.age)
print(A.age)

