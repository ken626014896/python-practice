import  multiprocessing
import os


def worker(a):
    print('child process  %s :%s' % (os.getpid(),a))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=multiprocessing.Process(target=worker,args=('test',))
    p.daemon=True

    #daemon=True 即该子进程会跟随主进程一起结束
    p.start()

    print('over')