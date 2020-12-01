# g = (i for i in range(10))
# print(list(g))
# print(g.__next__())

# gen = ("麻花藤我第%s次爱你" %i  for i in range(10))
# # print(list(gen))
# # print(gen.__next__())
# for i in gen:
#     print(i)
#

def func():
    print(111)
    yield 222
g = func()
g1 = (i for i in g)
g2 = (i for i in g1)
print(list(g))
print(list(g1))
print(list(g2))

#迭代器定义：内部含有__iter__并且含有__next__方法的
#迭代器的好处：节省内存，惰性机制，一条刘走到底
#生成器：自己用python代码写的迭代器
