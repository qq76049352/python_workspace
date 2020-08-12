# def chi(good_food,bad_food):
#     print("我要吃",good_food,bad_food)
#
# chi('盖浇饭','辣条')

# def chi(*food):
#     print("我要吃",food)
#
# chi("盖浇饭",'辣条','面条')

# def func(a,b,c,*args,d=5):
#     print(a,b,c,d,args)
#
# func(1,2,3)
# func(1,2,3,4,5,d = '马大哈')

# def he(*num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum
# print(he(1,2,3,4,5))

def func(**food): #动态接收关键字参数
    print(food)

func(good_food="盖浇饭",bad_food="辣条")