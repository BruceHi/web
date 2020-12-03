# 工厂模式
class Human:
    def __init__(self):
        self.name = None
        self.gender = None

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender


class Man(Human):
    def __init__(self, name):
        print(f'hi, man {name}')


class Woman(Human):
    def __init__(self, name):
        print(f'hi, woman {name}')


# 工厂类：静态工厂模式
class Factory:
    def get_person(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)


factory = Factory()
factory.get_person('Adam', 'M')


# 工厂模式：返回在函数内动态创建的类
def factory2(func):
    class Kclass:
        pass

    # setattr(x, 'y', v) is equivalent to ``x.y = v''
    print(func.__name__, func)
    # setattr(Kclass, func.__name__, func)

    # 类方法
    setattr(Kclass, func.__name__, classmethod(func))
    return Kclass


def say_foo(self):
    print('bar')


# Foo = factory2(say_foo)
# foo = Foo()
# foo.say_foo()

# 类方法调用
Foo = factory2(say_foo)
Foo.say_foo()
