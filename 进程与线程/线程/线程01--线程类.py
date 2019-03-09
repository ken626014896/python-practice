import  threading
import time


class Mythread(threading.Thread):
    def __init__(self,arg):

        super(Mythread,self).__init__()  #注意：一定要显式的调用父类的初始化函数。
        self.arg = arg

    def run(self):  # 定义每个线程要运行的函数
            time.sleep(1)
            print('the arg is:%s\r' % self.arg)

if __name__=='__main__':
    for i in range(4):
        t = Mythread(i)
        t.start()
        t.join()

    print('main thread end!')