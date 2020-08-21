#生成列表 里面装1-14的数据
# lst = []
# for i in range(1,15):
#     lst.append("python%s"%i)
# print(lst)

# lst = [i for i in range(1,15)]
# # print(lst)


# lst = [i for i in range(1,101) if i % 2 ==0]
# print(lst)

# lst = [i**2 for i in range(1,101) if i % 3 == 0 ]
# print(lst)

names = [['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe']
         ,['Alice','Jill','Ana','Wendy','jennifer','Sherry','Eva']]
lst = [name for first in names for name in first if name.count('e')==2]
print(lst)