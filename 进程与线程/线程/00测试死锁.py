import threading
# lock = threading.Lock() #Lock对象
# lock.acquire()
# lock.acquire()  #产生了死锁。
# lock.release()
# lock.release()
# print(lock.acquire())


rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire() #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()
print(rLock)