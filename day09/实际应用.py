
# def sum(n):
#     s = 0
#     for a in range(n+1):
#         s+=a
#     print(s)
#
# sum(100)


def fn(n):
    if n%2==0:
        return "偶数"
    else:
        return "奇数"

s = fn(23)
print(s)