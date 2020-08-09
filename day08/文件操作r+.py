# f = open("老师点名",mode="r+",encoding='utf-8')
# f.write("周润发")
# s = f.read()
#
# f.flush()
# f.close()
# print(s)
#

f = open("精品",mode='r+',encoding='utf-8')
f.seek(6)
s = f.read(3)
print(s)
f.close()