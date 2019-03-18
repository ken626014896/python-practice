# -*- coding: utf-8 -*-
import time
from multiprocessing import Pool
def run(fn):
  #fn: 函数参数是数据列表的一个元素
  time.sleep(1)
  print(fn*fn)

if __name__ == "__main__":
  testFL = [1,2,3,4,5,6]
  print ('shunxu:') #顺序执行(也就是串行执行，单进程)
  s = time.time()
  for fn in testFL:
    run(fn)
  t1 = time.time()
  print ("顺序执行时间：", int(t1 - s))

  print ('concurrent:') #创建多个进程，并行执行
  pool = Pool(6)  #创建拥有10个进程数量的进程池
  #testFL:要处理的数据列表，run：处理testFL列表中数据的函数
  pool.map(run, testFL)
  print('因为是阻塞的，我插不入中间，只好等进程池里面的运行完 我在插入')
  pool.close()#关闭进程池，不再接受新的进程

  pool.join()#主进程阻塞等待子进程的退出
  t2 = time.time()
  print ("并行执行时间：", int(t2-t1))

  pool2 = Pool(6)  # 创建拥有10个进程数量的进程池
  # testFL:要处理的数据列表，run：处理testFL列表中数据的函数
  pool2.map_async(run, testFL)
  print('因为是非阻塞的，我直接插入，在进程池里的进程运行前运行，')
  pool2.close()  # 关闭进程池，不再接受新的进程

  pool2.join()  # 主进程阻塞等待子进程的退出
  t3 = time.time()
  print("并行执行时间：", int(t3 - t2))