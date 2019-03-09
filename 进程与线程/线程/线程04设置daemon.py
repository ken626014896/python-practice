import  threading
import time

def action(arg):
    time.sleep(1)
    print('sub thread start!the thread name is:%s\r' % threading.currentThread().getName())
    print('the arg is:%s\r' % arg)
    time.sleep(1)

if __name__=='__main__':
    for i in range(4):
         t = threading.Thread(target=action, args=(i,))
         t. setDaemon(True)
         t. start()
    print('over')

