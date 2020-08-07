# dic1 = {
#     'name':['alex',2,3,5],
#     'job': 'teacher',
#     'oldboy':
#         {'alex': ['python1', 'python2', 100]}
#  }
#
# dic1["name"].append('wusir')
# dic1["name"][0] = dic1["name"][0].title()
# dic1['oldboy'].setdefault('老男孩','linux')
# del dic1['oldboy']['alex'][1]
#
# print(dic1)
#

s1 = "k:1|k1:2|k2:3|k3:4"
l1 = s1.split("|")
l2 = dict();
for c in l1:
    k,v = c.split(":")
    l2[k] =int(v)
print(l2)
