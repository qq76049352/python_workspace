# def chi():
#     print("我要吃")
#
# print(chi())

# def func1():
#     print("哈哈")
#
# def func2():
#     func1()
#     print("呵呵")
#     func1()
# func2()

def func1():
    print("呵呵")
    def func2():
        print("哈哈")
    func2()
    print("哄哄")
func1()