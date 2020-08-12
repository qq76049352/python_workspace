
# def func():
#     # a = 20
#     global a
#     a = 30
#     print(a)
# func()
# a = 10
# print(a)

# def func1():
#     a = 10
#     def func2():
#         nonlocal a
#         a = 20
#         print(a)
#     func2()
#     print(a)
# func1()

a=1
def fun_1():
    a=2
    def fun_2():
        nonlocal a
        a=3
        def fun_3():
            a=4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)

print(a)
fun_1()
print(a)

