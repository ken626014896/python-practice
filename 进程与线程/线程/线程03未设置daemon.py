import  threading
import time

def action(arg):
    time.sleep(1)
    print('sub thread start!the thread name is:%s\r' % threading.currentThread().getName())
    print('the arg is:%s\r' % arg)
    time.sleep(1)

if __name__=='__main__':
    for i in range(4):
     t=threading.Thread(target=action,args=(i,))
     t.start()
    print('over')
    #默认是前台线程
    #可以看出，创建的4个“前台”线程，主线程执行过程中，前台线程也在进行，
    # 主线程执行完毕后，等待前台线程也执行完成后，程序停止