#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
data=10
def run(num):
    semaphore.acquire()
    global data
    print "thread...",num
    data-=1
    time.sleep(1)
    semaphore.release()

if __name__=='__main__':
    semaphore = threading.BoundedSemaphore(3)
    for i in range(20):
        t=threading.Thread(target=run,args=(i,))
        t.start()

    while threading.active_count() !=1:
        pass
    else:
        print 'all threding done'
