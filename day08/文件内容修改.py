import os

with open("吃的",mode='r',encoding='utf-8') as f1,\
        open("吃的_副本",mode='w',encoding='utf-8')as f2:
    # s = f1.read()
    # ss = s.replace("肉","菜")
    # f2.write(ss)
    for line in f1:
        new_line = line.replace("菜","肉")
        f2.write(new_line)
os.remove("吃的")
os.rename("吃的_副本","吃的")
