# import sys
# sys.setrecursionlimit(10000)
# def func(i):
#     print("我是谁，我在那里"+str(i))
#     func(i+1)
#
# func(1)

# 遍历树形结构
# 伪代码
# def func(根节点)：
#     left = 根节点.leftNode
#     right = 根节点.rightNode
#     func(left)
#     func(right)

import os
filePath = r"C:\Users\张尔博\PycharmProjects\python_workspace"

def read(filePath,n):
    it = os.listdir(filePath)
    # print("__iter__" in dir(it))
    # print("__next__" in dir(it))
    for el in it:
        if os.path.isdir(os.path.join(filePath,el)): #判断是否是文件夹
            print('\t' * n, el)
            read(os.path.join(filePath,el),n+1)
        else:
            print('\t'*n,el)  #递归出口
read(filePath,0)