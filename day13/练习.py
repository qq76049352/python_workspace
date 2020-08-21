# def func():
#     print("111")
#     yield 222
#
# gener = func()
# ret = gener.__next__()
# print(ret)

# def func():
#     print("111")
#     yield 222
#     print("333")
#     yield 444
#
# gener = func()
# ret = gener.__next__()
# print(ret)
# ret2 = gener.__next__()
# print(ret2)
# # ret3 = gener.__next__()
# # print(ret3)

# def cloth():
#     for i in range(0,10000):
#         yield "衣服"+str(i)
#
# cl = cloth()
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())
# print(cl.__next__())

# def eat():
#     print("我要吃什么啊")
#     a = yield "馒头"
#     print("a=",a)
#     b = yield "大饼"
#     print('b=',b)
#     c = yield "韭菜盒子"
#     print('c=',c)
#     yield "GameOver"
#
# gen = eat()
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.send("胡椒汤")
# print(ret2)
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send("猫粮")
# print(ret4)

# def func():
#     print(111)
#     yield 222
#     print(333)
#     yield 444
#     print(555)
#     yield 666
#
# for i in func():
#     print(i)

def func():
    for item in range(10):
        pass
    print(item)

func()