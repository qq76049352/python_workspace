# dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
# print(dic.keys())
# for key in dic.keys():
#     print(key)

# print(dic.values())
# for value in dic.values():
#     print(value)

dic = {"及时雨":"宋江","易大师":"剑圣","维恩":"暗影猎手"}
print(dic.items())
for item in dic.items():
    k,v = item
    print(k,v)
    # print(item[0])
    # print(item[1])

#解构,捷报
# a , b = 1 , 2
# print(a)
# print(b)

# a , b , c = ("麻花藤","马云","不知道")