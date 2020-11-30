# lst = [5,7,6,12,1,13,9,18,5]
# # lst.sort()     #sort是list里面的一个方法
# # print(lst)
#
# l1 = sorted(lst)  #内置函数，返回给你一个新列表
# print(l1)
# l2 = sorted(lst,reverse=True)
# print(l2)

# 给列表排序，根据字符串的长度进行排序
# lst = ["大秧歌a","尼古拉斯aaa","赵四aaaaaa","谢大脚","艾泽拉斯"]
#
# a = sorted(lst,key= lambda s : s.count("a"))
# print(a)

lst = [
        {'id':1,'name':'alex','age':'12'},
        {'id':2,'name':'taibai','age':'19'},
        {'id':3,'name':'wusir','age':'48'},
        {'id':4,'name':'ritian','age':'28'},
        {'id':5,'name':'nvshen','age':'18'},
       ]
# a = lambda s:s['age']
a = sorted(lst,key=lambda dic:dic['age'])
print(a)
