# def func():
#     print("你吃了吗")
#
# print(func)
# a = func
# a()

# def f1():
#     print("我是麻花藤")
# def f2():
#     print("我是马云")
# def f3():
#     print("我是马赛克")
# def f4():
#     print("我是吗卫华")
#
# lst = [f1,f2,f3,f4]
# for i in lst:
#     i()
# print(lst)


def func(fn):
    fn()

def gn():
    print("我是火锅,刚才有人要吃我")

func(gn)