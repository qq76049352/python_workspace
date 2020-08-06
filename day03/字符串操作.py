# s = "i am bilbo"
# s1 = s.capitalize()
# print(s)
# print(s1)

# s = "I am Bilbo"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())

# s = "alex麻花藤an wu sir sir se"
# print(s.title())

# s = "麻花藤"
# print(s.center(9,"*"))

# s =" olhello "
# print(s)
# print(s.strip())
# print(s.strip("lo "))

# s = "I am Bilbo"
# s1 = s.replace("Bilbo","张尔博")
# print(s1)
# s2 = s.replace(" ","")
# print(s2)
#
# s = "Bilbo is not Bilbo"
# s1 = s.replace("Bilbo","sb",1)
# print(s1)
# s2 = s.split(" ")
# print(s2)


# s = "我叫{},我今年{}岁，我喜欢{}".format("张尔博","30","编程")
# print(s)

# s = "我叫{1},我今年{0}岁，我喜欢{2}".format("张尔博","30","编程")
# print(s)
#
# s = "我叫{name},我今年{age}岁，我喜欢{hobby}".format(name="张尔博",age="30",hobby= "编程")
# print(s)

# s = "汪峰的老婆不爱汪峰"
# print(s.startswith("汪峰"))
# print(s.count("老婆"))
# print(s.find("汪峰",3))
#
# print(s.index("章子怡"))

# s = "abc123"
# print(s.isdecimal())
# print(s.isalpha())
# print(s.isalnum())

# s = "一二三456"
# print(s.isnumeric())
# print(len(s))
# print(s.__len__())

s = "小雪老师，你好漂亮"
for c in s:
    print(c)