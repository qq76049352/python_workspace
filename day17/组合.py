# class Game_role():
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad=ad
#         self.hp=hp
#     def attack(self,p):
#         p.hp-=self.ad
#         print('%s攻击了%s，%s掉了%s血，还剩%s血'%(self.name,p.name,p.name,self.ad,p.hp))
#
# l1 = Game_role('盖伦',20,500)
# l2 = Game_role('亚索',50,200)
# l1.attack(l2)

#组合：给一个类的对象封装一个属性，这个属性是另一个类的对象

#版本一：添加武器：斧子，刀，枪，棍，棒...
#代码不合理：人物利用武器攻击别人，你的动作发起者是人，不是武器
# class Game_role:
#     def __init__(self,name,ad,hp):
#         self.name = name
#         self.ad=ad
#         self.hp=hp
#     def attack(self,p):
#         p.hp-=self.ad
#         print('%s攻击了%s，%s掉了%s血，还剩%s血'%(self.name,p.name,p.name,self.ad,p.hp))
#
# class Weapon:
#     def __init__(self,name,ad):
#         self.name=name
#         self.ad=ad
#     def fight(self,p1,p2):
#         p2.hp = p2.hp - self.ad
#         print('%s用%s打了%s,%s掉了%s血，还剩%s' % (p1.name,self.name,p2.name,p2.name,self.ad,p2.hp))
#
# p1 = Game_role('大阳哥',20,500)
# p2 = Game_role('印度阿宁',50,200)
# axe = Weapon("三板斧",60)
# broadsword = Weapon("屠龙宝刀",100)
#
# axe.fight(p1,p2)
# broadsword.fight(p2,p1)

#版本二
class Game_role:
    def __init__(self,name,ad,hp):
        self.name = name
        self.ad=ad
        self.hp=hp
    def attack(self,p):
        p.hp-=self.ad
        print('%s攻击了%s，%s掉了%s血，还剩%s血'%(self.name,p.name,p.name,self.ad,p.hp))
    def armament_weapon(self,wea):
        self.wea = wea

class Weapon:
    def __init__(self,name,ad):
        self.name=name
        self.ad=ad
    def fight(self,p1,p2):
        p2.hp = p2.hp - self.ad
        print('%s用%s打了%s,%s掉了%s血，还剩%s' % (p1.name,self.name,p2.name,p2.name,self.ad,p2.hp))

p1 = Game_role('大阳哥',20,500)
p2 = Game_role('印度阿宁',50,200)
axe = Weapon("三板斧",60)
broadsword = Weapon("屠龙宝刀",100)

p1.armament_weapon(axe)
p1.wea.fight(p1,p2)