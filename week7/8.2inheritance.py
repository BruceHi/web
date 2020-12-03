# 父类
class People:
    def __init__(self, name):
        self.gene = 'XY'
        self.name = name

    def walk(self):
        print('I can walk')


# 子类
class Man(People):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        print('work hard')


class Woman(People):
    def __init__(self, name):
        super().__init__(name)

    def shopping(self):
        print('buy buy')


p1 = Man('Adam')
p2 = Woman('eve')

print(p1.gene)

# type 就是用来创建类对象的类，str是用来创建字符串对象的类，而int是用来创建整数对象的类。
# type 元类创建了 type 类，同时也创建了 object 类
# type 类继承了 object 类
# 是谁创建的，使用 __class__(都是 type 创建的)，继承关系，使用 __bases__
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)

print('Man', Man.__class__, Man.__bases__)

print(type(object))


class Son(Man, Woman):
    pass


print('Son', Son.__class__, Son.__bases__)
print(type(Son.__bases__))

a = (1, 2)
a += 3,
# TypeError: can only concatenate tuple (not "int") to tuple
print(a)
b = a + (1, 2)
print(b)
