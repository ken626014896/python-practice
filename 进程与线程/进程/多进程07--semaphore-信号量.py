from  multiprocessing import  Process ,Semaphore
import os,random,time



def func(i,sem):
    sem.acquire()
    print('第%s个人进入小黑屋,拿了钥匙锁上门' % i)
    time.sleep(random.randint(3,5))
    print('第%s个人出去小黑屋,还了钥匙打开门' % i)
    sem.release()
if __name__ == '__main__' :
    sem =Semaphore(5)
    for i in range(1,20) :
        p = Process(target=func,args=(i,sem))
        p.start()