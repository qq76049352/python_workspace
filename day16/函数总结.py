def func(*args, **kwargs):
    print(args)
    print(kwargs)


# *args 表示任何多个无名参数，它本质是一个 tuple(元组)
# **kwargs 表示关键字参数，它本质上是一个 dict(字典)
# 如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前
# func(1, 2, 3, name='alex', age=1000)
l1 = [1,2,3]
l2 = [4,5,6]
func(*l1,*l2)

#形式参数的位置：位置参数 ，*args 默认参数，**kwargs
#实际参数的位置：位置参数，关键字参数

l1 = [i for i in range(1,100)]
l2 = [i for i in range(1,100) if i >50] 
