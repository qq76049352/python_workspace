# dic = {"a":"b","c":"d"}
#
# new_dic = {dic[key]:key for key in dic }
# print(new_dic)

lst1 = ["alex","wusir","taibai","ritian"]
lst2 = ['sb',"很色","3","4"]
new_dic = {lst1[i]:lst2[i] for i in range(len(lst1))}
print(new_dic)
