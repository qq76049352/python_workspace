f = open("亵渎",mode='w+',encoding='utf-8')  #不用的
f.write("今天天气")
f.seek(0) #移动光标
s = f.read()
print(s)
f.flush()
f.close()