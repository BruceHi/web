class Human2:
    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print(f' __getattribute__ called item:{item}')
        return super().__getattribute__(item)


h = Human2()
print(h.age)

print(h.noattr)

# 思考：为什么使用super()不使用self
# 使用 self 就形成了死循环了，用于出不来。
