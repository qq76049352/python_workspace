# def func():
#     print("大渣粥")
#     a = yield "11"
#     print(a)
#     print("狗不理")
#     b = yield "22"
#     print(b)
#     print("大麻花")
#     c = yield "33"
#     print(c)
#
# g = func()
# print(g.__next__())
# print(g.send("1"))
# print(g.send(3))

#__next__()可以让生成器向下执行一次
#send()也可以让生成器向下执行一次

# def eat():
#     print("我吃什么啊")
#     a = yield "馒头"
#     print("a=",a)
#     b = yield "⼤饼"
#     print("b=",b)
#     c = yield "⾲菜盒⼦"
#     print("c=",c)
#     yield "GAME OVER"
# gen = eat() # 获取⽣成器
# ret1 = gen.__next__()
# print(ret1)
# ret2 = gen.send("胡辣汤")
# print(ret2)
# ret3 = gen.send("狗粮")
# print(ret3)
# ret4 = gen.send("猫粮")
# print(ret4)

def func():
    yield 11
    yield 22
    yield 33
    yield 44
g = func()
lst = list(g)
print(lst)