class Human:
    def __init__(self):
        self.age = 18

    # 对指定属性进行处理，其他属性返回 None。
    def __getattr__(self, item):
        self.item = item
        if self.item == 'fly':
            return 'superman'


h = Human()
print(h.age)
print(h.fly)
print(h.noattr)
print(h.item)

print(h.__dict__)