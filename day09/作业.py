f1 =open("a1.txt",mode='r+',encoding='utf-8')
lst = f1.readline().split()
result = []
for line in f1:
    s = line.split()
    dic = dict()
    for v in range(len(s)):
        dic[lst[v]]=s[v]
    result.append(dic)
print(result)
