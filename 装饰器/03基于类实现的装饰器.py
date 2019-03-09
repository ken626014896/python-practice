class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print ("[DEBUG]: enter function {func}()".format(
            func=self.func.__name__))
        return self.func(*args, **kwargs)
@logging
def say(something):
    print ("say {}!".format(something))

say('hi')

