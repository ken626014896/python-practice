def Singmoshi(func):
    _ddd={}

    def warpper(*args,**kwargs):
        if func not  in _ddd:
            _ddd[func]=func(*args,**kwargs)
            #把实例对象放进字典中
        return _ddd[func]

    return warpper

@Singmoshi
class aa:

    a=1
    def __init__(self,x,a):
        self.x=x
        self.a=a

a=aa(550,2)
b=aa(5500,3)

print(a.x)
print(b.x)
print(a.a)
print(b.a)