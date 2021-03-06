from multiprocessing import Pipe, Process
from threading import Thread

import time

def proc1(pipe):
   for i in range(10):
     print("send {0}".format(i))
     pipe.send(i)
     time.sleep(0.5)
   print("end proc1")

def proc2(pipe):
   n =10
   while n:
     print("proc2 recv {0}".format(pipe.recv()))
     n -=1

if __name__ == '__main__':
  (p1,p2) = Pipe(duplex=False)
  pr = Process(target=proc1,args=(p2,))
  cu = Process(target=proc2,args=(p1,))
  pr.start()
  # pr.join()
  cu.start()
