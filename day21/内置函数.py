# isinstance() 判断对象所属类型，包括继承关系
# issubclass() 判断类与类之间的继承关系

# class A:pass
# class B(A):pass
# b= B()
#
# # print(isinstance(b,B))
# # #判断这个对象是不是这个类型
# # print(isinstance(b,A))
#
# print(type("alex") is str)
# print(isinstance('alex',str))

# class A: pass
# class B(A): pass
# b = B()
#
# print(type(b))
# print(type(b) is A)  # type继承的不算
# print(isinstance(b, A))  # isinstance继承的也算同类

# == 值运算
# is 内存地址相等
#is要求更苛刻

#issubclass
class A: pass
class B(A): pass
print(issubclass(B,A))
print(issubclass(A,B))