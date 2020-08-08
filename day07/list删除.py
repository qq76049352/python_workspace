# lst = ["我不是药神","西游记","西虹市首富","天龙八部"]

# lst.clear()

# for el in range(0,len(lst)):
#     lst.pop()
#
# print(lst)

# lst = ["周杰伦","周润发","周星星","马化腾","周树人"]
# del_lst = []
# for el in lst:
#     if el.startswith("周"):
#         del_lst.append(el)
# for el in del_lst:
#     lst.remove(el)
# print(lst)

# dic = {'k1': 'alex', 'k2': 'wusir', 's1': '⾦金金⽼老老板'}
# # 删除key中带有'k'的元素
# del_dic = []
# for k in dic:
#     if 'k' in k:
#         del_dic.append(k)
#
# for v in del_dic:
#     del dic[v]
# print(dic)

dic = {"a":"123"}
s = dic.fromkeys("王健林","思聪")
print(dic)
print(s)