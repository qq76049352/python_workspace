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
