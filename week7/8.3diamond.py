# 钻石继承，使用拓扑排序，相同的在前边（左边）的先继承
class BaseClass:
    def call_me(self):
        print('call method on Base Class')


class LeftClass(BaseClass):
    def call_me(self):
        print('call method on Left Class')


class RightClass:
    def call_me(self):
        print('call method on Right Class')


class SubClass(LeftClass, RightClass):
    pass


a = SubClass()
a.call_me()

print(SubClass.mro())

#  修改RightSubclass 的 父类为 Object
print(SubClass.mro())


#    object
# base rightclass
# Leftclass
#    subclass
