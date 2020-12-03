class Human:
    def __init__(self):
        self.age = 18

    # 读取未定义的属性被调用
    def __getattr__(self, item):
        print(f'__getattr__ called item: {item}')
        return 'ok'


h = Human()
print(h.age)
print(h.noattr)
