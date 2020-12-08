# python 没有接口这个概念
# 接口类，抽象类：定义 制定一个规范

# 第一版
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用支付宝支付了%s" % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用京东支付了%s" % self.money)
#
#
# a1 = Alipay(200)
# a1.pay()
#
# j1 = Jdpay(100)
# j1.pay()

# 第二版 改进，让你的支付方式一样
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用支付宝支付了%s" % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用京东支付了%s" % self.money)
#
# def pay(obj):
#     obj.pay()
#
# a1 = Alipay(200)
# j1 = Jdpay(100)
# pay(a1)#归一化设计
# pay(j1)

# 第三版，野生程序员来了。。。。要增加要给微信支付的功能
# class Alipay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用支付宝支付了%s" % self.money)
#
#
# class Jdpay:
#     def __init__(self, money):
#         self.money = money
#
#     def pay(self):
#         print ("使用京东支付了%s" % self.money)
#
# class Wechatpay:
#     def __init__(self, money):
#         self.money = money
#
#     def weixinpay(self):
#         print ("使用微信支付了%s" % self.money)
#
# def pay(obj):
#     obj.pay()
#
# a1 = Alipay(200)
# j1 = Jdpay(100)
# pay(a1)#归一化设计
# pay(j1)
#
# w1 = Wechatpay(50)
# w1.weixinpay()

# 第四版 发回去重新改，制定规则，抽象类，接口类

from abc import ABCMeta, abstractclassmethod


class Payment(metaclass=ABCMeta):  # 抽象类 强制定义一个规范。凡是继承都必须重写pay方法
    @abstractclassmethod
    def pay(self):
        pass  # 制定了一个规范


class Alipay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print("使用支付宝支付了%s" % self.money)


class Jdpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print("使用京东支付了%s" % self.money)


class Wechatpay(Payment):
    def __init__(self, money):
        self.money = money

    def pay(self):
        print("使用微信支付了%s" % self.money)


def pay(obj):
    obj.pay()


a1 = Alipay(200)
j1 = Jdpay(100)
pay(a1)
pay(j1)
w1 = Wechatpay(300)
pay(w1)
