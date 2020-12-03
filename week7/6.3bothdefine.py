class Human:
    def __init__(self):
        self.age = 18

    # 同时存在的调用顺序
    def __getattr__(self, item):
        print('human2:__getattr__')
        return '404'

    def __getattribute__(self, item):
        print('human2:__getattribute__')
        return super().__getattribute__(item)



h = Human()
print(h.age)
print(h.noattr)

# 同时存在，先 __getattribute__，再 __getattr__，最后 __dic__，先遇到 return 的先返回。
# 其中 object 对象调用的方法也是是 """ Return getattr(self, name)."""
# 若是 __getattribute__ 方法没有引用父类方法，则直接返回比如： None 或 ‘666’
