# lst = [22,33,44,55,66,77,88,99,101,238,456,567,678,789]
# n = 567
#
# left = 0
# right = len(lst)-1
# middle = (left+right)//2
# count = 0
#
# while left <=right:
#     count +=1
#     middle = (left + right) // 2
#     if n > lst[middle]:
#         left = middle + 1
#     elif n < lst[middle]:
#         right = middle -1
#     else:
#         print("存在")
#         print(middle)
#         print(count)
#         break
# else:
#     print("不存在")

lst = [22,33,44,55,66,77,88,99,101,238,456,567,678,789]

# def binary_search(left,right,n):
#     middle = (left + right)//2
#     if n > lst[middle]:
#         left = middle + 1
#     elif n < lst[middle]:
#         right = middle - 1
#     else:
#         return middle
#     return binary_search(left,right,n)
#
# print(binary_search(0,len(lst),101))

def binary_search(left,right,n):
    middle = (left + right)//2
    if left > right:
        return -1
    if n > lst[middle]:
        return binary_search(middle+1,right,n)
    elif n < lst[middle]:
        return binary_search(left,middle-1,n)
    else:
        return middle
print(binary_search(0,len(lst),789))

# def binary_search(lst,n):
#     left = 0
#     right = len(lst)-1
#     middle = (left + right)//2
#     if right < 0:
#         print("没找到")
#         return
#     if n > lst[middle]:
#         lst = lst[middle+1:]
#     elif n < lst[middle]:
#         lst = lst[:middle-1]
#     else:
#         print("找到了")
#         return
#     binary_search(lst,n)
#
# binary_search(lst,65)


