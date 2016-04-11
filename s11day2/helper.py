#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Queue
import threading
class ThreadPool(object):

    def __init__(self,max_num=20):
        self.queue = Queue.Queue(max_num)
        for  i in xrange(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        return self.queue.put(threading.Thread)



pool = ThreadPool(20)

def func(arg,p):
    print arg
    import time
    time.sleep(2)
    p.add_thread()

for i in xrange(300):
    thread = pool.get_thread()
    t= thread(target=func,args=(i,pool))
    t.start()





