from functools import  reduce
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

s='123.456'
def str2float(s):
    def char2num(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
        return DIGITS[s]
    def fn(x, y):
        return x*10 + y
    def fm(x, y):
        return x*0.1 + y
    r1 = []
    r2 = []
    #要计算出整数位和小数位的个数

    int_num=s.index('.')


    float_num=0-(len(s)-1-int_num)
    n = 0
    m = -1


    r = list(map(char2num, s))

    while n < int_num:
        r1.append(r[n])
        n = n + 1
    while m >= float_num:
        r2.append(r[m])
        m = m - 1
    return reduce(fn, r1) + reduce(fm, r2)/10

print(str2float(s))