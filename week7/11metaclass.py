# 使用 type 创建类
def hi():
    print('hi metaclass')


# type(object_or_name, bases, dict) -> a new type
# 类名，父类（元组表示），类的成员
Foo = type('Foo', (), {'say_hi': hi})
foo = Foo
print(foo.say_hi)
Foo.say_hi()


# 在初始化时就增加额外的功能
def pop_value(self, dict_value):
    for key, val in self.items():
        if val == dict_value:
            self.pop(key)
            break


# 元类要求，必须继承自 type
class DelValue(type):
    # 元类要求，必须实现 __new__ 方法
    def __new__(cls, name, bases, attrs):
        attrs['pop_value'] = pop_value
        return super().__new__(cls, name, bases, attrs)


class DelDictValue(dict, metaclass=DelValue):
    pass


d = DelDictValue()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

d.pop_value('C')
print(d)
