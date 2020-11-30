def func(n):
    return  n * n

print(func(3))
a = func
print(a.__name__)
print(func.__name__)

# a = lambda x: x*x
# print(a)
# print(a(6))
#
# b = lambda x,y: x + y
# print(b(1,3))

##匿名函数只能一行代码 ，
##  语法：lanbda 参数 ：返回值