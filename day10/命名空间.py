a = '123'
b = 67
def func():
    c = "麻花藤"
    def haha():
        pass


a = 10
def func():
    a = 20
    print(a)
    print(locals())
    print(globals())
func()
print(a)


