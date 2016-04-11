#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  contextlib
import threading
import  time
import  random
doing=[]
def num(l2):
    while True:
        print len(l2)
        time.sleep(1)
t=threading.Thread(target=num,args=(doing,))
t.start()

@contextlib.contextmanager
def  show(doing,item):
    #print 'before'
    doing.append(item)
    yield
    #print 'after'
    doing.remove(item)
def task(i):
    flag = threading.current_thread()
    with show(doing,flag):
        print  'with in'
        import time
        time.sleep(random.randint(1,4))

for i in range(20):
    temp = threading.Thread(target=task,args=(i,))
    temp.start()


