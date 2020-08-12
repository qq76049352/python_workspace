# x = 1
# x += 1
# print(x)
#
# s1 = "老男孩"
# s2 = s1.encode(encoding='utf-8')
# print(s2)
#
# a = '1,2,3'.split(',')
# print(a)

# dic = {"最终计算结果":None}
# s = input("请输入内容").strip()
# lst = s.split('+')
# sum = 0
# for i in lst:
#     sum+= int(i.strip())
# dic["最终计算结果"]=sum
# print(dic)

# def func(filename,*args):
#     f = open(filename,mode='w',encoding='utf-8')
#     s = '_'.join(args)
#     f.write(s)
#     f.flush()
#     f.close()

def func(user_list):
    new_list=[]
    name_list=[]
    for i in user_list:
        if i["name"] in name_list:
            for y in new_list:
                if i["name"] == y['name']:
                    y['hobby_list'].append(i['hobby'])
        else:
            name_list.append(i["name"])
            dic = {"name":i["name"],"hobby_list":[i["hobby"],]}
            new_list.append(dic)
    print(new_list)

user_list = [
    {"name":"alex","hobby":"抽烟"},
    {"name":"alex","hobby":"喝酒"},
    {"name":"alex","hobby":"探头"},
    {"name":"wusir","hobby":"喊麦"},
    {"name":"wusir","hobby":"街舞"},
]

func(user_list)