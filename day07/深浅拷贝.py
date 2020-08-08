# lst1 = ["金毛狮王","紫衫龙王","白眉鹰王","青翼蝠王"]
# lst2= lst1
#
# lst2.append("杨左使")
# print(lst1)

# 浅拷贝 copy

# lst1 = ["赵本山","刘能","赵四"]
# # lst2 = lst1.copy()
# lst2 = lst1[:]
# lst2.append("张三")
# print(lst1)
# print(lst2)

# lst1 = ["超人","七龙珠","葫芦娃","山中小猎人",["金城武","王力宏","渣渣辉"]]
# lst2 = lst1.copy()
# lst1[4].append("大秧歌")
# print(id(lst1[4]))
# print(id(lst2[4])) #浅拷贝

#深拷贝
# import copy
# lst1 = ["超人","七龙珠","葫芦娃","山中小猎人",["金城武","王力宏","渣渣辉"]]
# lst2 = copy.deepcopy(lst1)
# lst1[4].append("大秧歌")
# # print(id(lst1[4]))
# # print(id(lst2[4]))
# print(lst1,lst2)


