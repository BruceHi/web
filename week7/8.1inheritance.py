# 父类
class People:
    def __init__(self):
        self.gene = 'XY'

    def walk(self):
        print('I can walk')


# 子类
class Man(People):
    def __init__(self, name):
        self.name = name

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        self.name = name
    def shopping(self):
        print('buy buy')

p1 = Man('Adam')
p2 = Woman('eve')

p1.gene


