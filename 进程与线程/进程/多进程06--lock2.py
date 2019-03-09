from multiprocessing import Process ,Lock
import random
import time
def func(addr,lock):
    lock.acquire()
    print('我是%s'%addr)
    time.sleep(random.random())
    print('谢谢！')
    lock.release()
if __name__ == '__main__':
    lock = Lock()
    l = ['四川的','湖南的','河南的','江苏的']
    for addr in l:
        p = Process(target=func,args=(addr,lock))
        p.start()
    time.sleep(4)
    print('\n\n我选%s'%random.choice(l))