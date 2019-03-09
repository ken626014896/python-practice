class aa:
    _a='a'
    __b="b"

    def _cc(self):
        print('cc')

    def __dd(self):
        print('dd')


a=aa()

print(a._a)
a._cc()

