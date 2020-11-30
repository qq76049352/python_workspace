# # def func(i):
# #     return i % 2 == 1
# lst = [1,2,3,4,5,6,7,8,9]
#
# l1 = filter(lambda i:i%2==1,lst)
# print(l1)
# print(list(l1))

lst = [
        {'id':1,'name':'alex','age':12},
        {'id':2,'name':'taibai','age':19},
        {'id':3,'name':'wusir','age':48},
        {'id':4,'name':'ritian','age':28},
        {'id':5,'name':'nvshen','age':18},
       ]
l1 = filter(lambda dir:dir['age']>25,lst)
print(list(l1))