from multiprocessing import Event, Process
import time
def tra(e):
    while 1:
        if e.is_set():
            time.sleep(5)
            print('\033[31m 红灯亮!\033[0m')
            e.clear()
        else:
            time.sleep(5)
            print('\033[32m 绿灯亮!\033[0m')
            e.set()
def Car(i, e):
    e.wait()
    print('第%s辆车过去了' % i)
if __name__ == '__main__':
    e = Event()
    print('一开始is_set()为%s  e.wait()为阻塞状态'% e.is_set())
    triff_light = Process(target=tra, args=(e,))
    triff_light.start()
    for i in range(500):
        car = Process(target=Car, args=(i + 1, e,))
        car.start()
        time.sleep(2)