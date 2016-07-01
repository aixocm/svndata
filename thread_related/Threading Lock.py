#_*_coding:utf-8_*_
__author__ = 'jieli'
import threading,time
def run(n):
    time.sleep(0.5)
    global  num
    lock.acquire() #申请锁并+锁
    num +=1
    lock.release() #释放锁
if __name__ == '__main__':
    num = 0
    lock = threading.Lock()
    for i in range(10):
        t = threading.Thread(target=run,args=(i,))
        t.start()


    while threading.active_count() != 1:
        print threading.active_count()
    else:
        print '----all threads done---'
        print num
print help(threading.RLock())