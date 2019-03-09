
def Fibonacci(i):
    """
    输出指定位置的斐波拉契数
    """

    if i == 1 or i ==2:
        return 1
    elif i == 0:
        return 0
    else:
        # sum = Fibonacci(i-2) + Fibonacci(i-1)
        # print(sum)           # 必须通过return返回结果，否则数据无法传输，导致结果报错，
        return Fibonacci(i-2) + Fibonacci(i-1)



if __name__ == "__main__":

    print(Fibonacci(1))  # 打印第五个斐波拉契数，不是零开始

    # 打印指定数量的斐波拉契数列
    l = []
    for i in range(0,5):
        l.append(Fibonacci(i))
    print(l)
