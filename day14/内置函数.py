
# lst = ["白蛇传","逍遥叹","庄周闲游"]

# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())


#
# it = iter(lst)
# print(it.__next__())
# print(next(it))

# lst = (1,2,3,4)
# print(id(lst))
# print(hash(lst))
#
# dic = {"jay":"周杰伦","jj":"林俊杰"}


# print(help(str))  #所有方法名字
# print(dir(str))   #帮助文档

# a = 10
# print(callable(a)) #能否被调用

# a = 1.23e1
# print(type(a))
# print(a)

# print(bin(5)) #2进制
# print(oct(8)) #8进制
# print(hex(15)) #16进制

# print(abs(-8)) #绝对值 |绝对值| 取模
# print(divmod(10,3))   #计算商和余数
# print(round(3.4)) #四舍五入
# print(pow(2,4,3)) #次幂  第三个参数取余

# print(sum([1,2,3,4,5],3))
# print(min([1,6,43,25,34]))
# print(max([1,6,43,25,34]))

# lst = ["马化腾","马云","马大神","马帅"]
# l1 = reversed(lst)
# print(list(l1))

lst = ["马化腾","马云","马大神","马帅"]
s = slice(1,3,2) #切片
print(lst[s])
print(lst[1:3:2])