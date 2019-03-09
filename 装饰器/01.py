def debug(func):
    def wrapper(*args,**kwargs):
        print(args)
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args,**kwargs)

    return  wrapper


@debug
def say_hello(a):
    print('a')

say_hello('你好')
print(dir(say_hello))
print(say_hello.__name__)