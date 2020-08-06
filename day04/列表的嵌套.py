
# lst = []
# lst.append("李太白")
# lst.append("李太白")
# lst.append("李太白")
# lst.append("李太白")
# lst[1:4]="李太白"
# print(lst)

lst = [1,"太白","wusir",["麻花藤",["可口可乐"],"王剑林"]]
lst[1] = lst[1].replace("白","黑")
print(lst)