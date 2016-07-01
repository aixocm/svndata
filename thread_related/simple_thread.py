#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import threading
import time

def run(num):
    #lock.acquire()
    global data
    print("thread...",num)
    data -=1
    #lock.release()
    #time.sleep(0.1)
lock = threading.Lock()
data = 100
print threading.activeCount()
for i in range(100):
    t = threading.Thread(target=run, args=(i,))
    #t.start()

#print "--->data:",data
