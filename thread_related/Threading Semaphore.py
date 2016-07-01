#_*_coding:utf-8_*_
__author__ = 'jieli'
import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print "run the thread: %s\n" %n
    semaphore.release()

if __name__ == '__main__':

    num= 0
    semaphore  = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    print threading.active_count()
else:
    print '----all threads done---'
    print num
