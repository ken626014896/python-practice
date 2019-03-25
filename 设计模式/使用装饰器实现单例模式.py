def Singmoshi(func):
    _ddd={}

    def warpper(*args,**kwargs):
        if func not  in _ddd:
            _ddd[func]=func(*args,**kwargs)
            #把实例对象放进字典中
        return _ddd[func]

    return warpper

@Singmoshi
class singlclass:

    a=1
    def __init__(self,x,a):
        self.x=x
        self.a=a

a=singlclass(550,2)
b=singlclass(5500,3)

print(a.x)
print(b.x)   ## b的初始化带来的属性不会覆盖掉a的属性哦！返回的都是第一次初始化的对象
print(a.a)
print(b.a)