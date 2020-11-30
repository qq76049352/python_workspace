lst = [1,2,3,4,5,6,7]
def func(i):
    return i * i

l1 = map(func,lst)
print(list(l1))

print(list(map(lambda i:i*i,lst)))