# name = ''
#
# def func():
#     name = 'alex'   #常驻内存
#     def inner():
#         print(name)
#     return inner
#
# ret =func()
# ret()

#闭包的好处
from urllib.request import urlopen
def but():
    content = urlopen("http://www.xiaohua100.cn").read()
    def get_content():
        return content
    print(get_content.__closure__)
    return get_content
fn = but()  # 这个时候就开始加载校花100的内容
# 后⾯面需要⽤用到这⾥里里⾯面的内容就不不需要在执⾏行行⾮非常耗时的⽹网络连接操作了
content = fn() # 获取内容
print(content)
content2 = fn()  # 重新获取内容
print(content2)