# lst = [1,2,3]
# print(dir(lst))
# print('__iter__' in dir(lst))


# lst = ["皇阿玛","皇额娘","容嬷嬷","紫薇"]
# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__()) # 迭代到最后一个元素之后,在进行迭代就错误了

# lst = ["皇阿玛","皇额娘","容嬷嬷","紫薇"]
# it = lst.__iter__()
# while True:
#     try:
#         name = it.__next__()
#         print(name)
#     except StopIteration:
#         break


# lst = [1,2,3]
# it = lst.__iter__()
# from collections import Iterable
# from collections import Iterator

# print(isinstance(lst,Iterable))
# print(isinstance(lst,Iterator ))
# print('__iter__'in dir(it))
# print('__next__'in dir(it))
