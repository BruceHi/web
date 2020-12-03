# 2. 使用构造函数 __new__
class Foo:
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name


bar = Foo('test')
print(bar.name)

# 相当于下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')
print(bar.name)


# __new__ 实现单例模式
class Singleton:
    __instance = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        # cls.__instance = super(Singleton, cls).__new__(cls)
        cls.__instance = super().__new__(cls)
        print(cls, cls.__instance)
        return cls.__instance


s1 = Singleton()
s2 = Singleton()
print(id(s1))
print(id(s1) == id(s2))
