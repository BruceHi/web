# 1装饰器实现单例模式
def singleton(cls):
    instance = {}

    def get_instance():
        if cls not in instance:
            instance[cls] = cls()
        print(cls, cls())  # 类，实例化
        return instance[cls]

    return get_instance


@singleton
class MyClass:
    pass


m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))
