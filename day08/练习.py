# f = open("../day08/练习.txt",mode="rb")
# content = f.read()
# print(content)
# f.close()

# f=open("../day08/哇擦.txt",mode="r",encoding="utf-8")
# content = f.read(3)
# print(content)    #友谊地

# f=open("../day08/哇擦.txt",mode="rb")
# content = f.read(3)
# print(content)

# f=open("../day08/哇擦.txt",mode="r",encoding="utf-8")
# content = f.read(3)
# content2 = f.read(3)
# print(content)    #友谊地
# print(content2)    #久天⻓

# f = open("../day08/哇擦.txt",mode="r",encoding='utf-8')
# content = f.readline()
# content2 = f.readline()
# content3 = f.readline()
# content4 = f.readline()
# content5 = f.readline()
# content6 = f.readline()
#
# print(content,end="")
# print(content2)
# print(content3)
# print(content4)
# print(content5)
# print(content6)


# f = open("../day08/哇擦.txt",mode='r',encoding='utf-8')
# lst = f.readline()
# print(lst)
# for line in lst:
#     print(line.strip())
# f.close()

# f = open("../day08/哇擦.txt",mode='r',encoding='utf-8')
# for line in f:
#     print(line.strip())
# f.close()

# f = open("小娃娃.txt",mode='w',encoding='utf-8')
# f.write('金毛狮王谢逊')
# f.flush()
# f.close()

# f = open("../day08/小娃娃.txt",mode='wb')
# f.write("金毛狮王".encode('utf-8'))
# f.flush()
# f.close()

# f = open("../day08/小娃娃.txt",mode='a',encoding='utf-8')
# f.write("麻花藤的最爱")
# f.flush()
# f.close()

# f = open("../day08/小娃娃.txt",mode='ab')
# f.write("我也不知道写什么好".encode('utf-8'))
# f.flush()
# f.close()

# f = open("../day08/小娃娃.txt",mode="r+",encoding='utf-8')
# content = f.read()
# f.write("哈哈")
# print(content)
# f.flush()
# f.close()

# f = open("../day08/小娃娃.txt",mode="r+",encoding='utf-8')
# f.write("呵呵")
# content = f.read()
# print(content)
# f.flush()
# f.close()

# f = open("小娃娃.txt",mode="w+",encoding='utf-8')
# f.write("哈哈")
# content = f.read()
# print(content)
# f.flush()
# f.close()

#生成随机数
from random import randint
s = set()
while len(s)<7:
    s.add(randint(1,36))

lst = list(s)
lst.sort()
print(lst)