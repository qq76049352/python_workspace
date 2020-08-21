def func():
    print("我是周杰伦")
    yield "凌昆"
    print("我是王力宏")
    yield "李云迪？？？"
    print("我是笛卡尔积")
    yield "笛卡尔积是谁"
    # print("你好")  #最后一个yield之后不要加代码，会执行，会报错

g = func() #通过函数func（）创建一个生成器
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())