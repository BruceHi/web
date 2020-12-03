class Human:
    def __getattribute__(self, item):
        """
        将不存在的属性设置为 100 并返回
        :param item:
        :return:
        """
        print('Human2:__getattribute__')
        try:
            # return super(Human, self).__getattribute__(item)  # 快捷键自动生成的是 python 2 的写法。
            # 不能换成 raise
            # raise 后面接的是指定异常类型，语法格式：raise [Exception [, args [, traceback]]]
            return super().__getattribute__(item)
        except Exception as e:
            self.__dict__[item] = 100
            return 100


h = Human()
print(h.noattr)

print(h.__dict__)
