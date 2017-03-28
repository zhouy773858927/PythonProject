import re    #正则表达式

# 类
#    声明
# class CLASS_NAME(object):
#     pass
#    变量,函数定义

# 2.x新式类  老式类
# 3.x全部为新式类

# 车 品牌 车的发动机型号2.4L 2.0T 价格
# 类变量:所有这个类的对象都共有的
# 每个对象所特有的变量:这个类的每一个对象私有的
class Car:
    name = "小汽车"
    def __init__(self, pinpai,dangci, fadongji, jiage):# Initialization构造函数:在这个对象被创建的时候会调用的方法
        self.pinpai = pinpai
        self.dangci= dangci
        self.fadongji = fadongji
        self.jiage = jiage

    def __getitem__(self, item):
        return self.dangci[item],self.jiage[item]

    def __setitem__(self, key, value):
        self.dangci[key]=value

    def test(self):
        pass

if __name__ == '__main__':
    # a = Car("BMW","4.0L",500000)
    # b = Car("奇瑞","1.5L",50000)
    # print(a.name)
    # Car.name="大卡车"
    # print(a.name)
    # print(b.name)
    # __main__
    dangci=["性能版","尊享版","奢华版"]
    jiage =[100000,200000,500000]
    c=Car("BMW",dangci,"4.0L",jiage)
    # None
    c[0]="低调版"
    c.setDangci(0,"低调版")
    print(c[0])
    # ('低调版', 100000)
    #     尊享版
    #     性能版
