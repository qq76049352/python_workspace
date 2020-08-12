# def func(lis):
#     new_lis = []
#     for i in range(len(lis)):
#         if i%2 == 0:
#             new_lis.append(lis[i])
#     return  new_lis
#
# a = [1,2,3,4,5,6,7]
#
# b = func(a)
# print(b)

# def IsNotFive(object):
#     if len(object)>5:
#         return True
#     else:
#         return  False

# def func(a,b):
#     c = a if a > b else b
#     return c
#
# print(func(3,5))

# def func(dic):
#     new_dic = {}
#     for k,v in dic.item:
#         if len(v >2):
#             new_dic[k]=v[0:2]
#         else:
#             new_dic[k]=v
#     return new_dic

import os
def func(filename,old,new):
    with open(filename,mode='r',encoding='utf-8')as f1,\
        open(filename+"_副本",mode='w',encoding='utf-8')as f2:
        for line in f1:
            s = line.replace(old,new)
            f2.write(s)
        os.remove(filename)
        os.rename(filename+'_副本',filename)


