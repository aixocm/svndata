#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import random
def dayday_fun(username):
    for s in range(3):
        time.sleep(1)
        Time=time.strftime('%Y-%m-%d')
        n=random.randint(1,5)
        with open(username,'ab') as f:
            f.write('%s=%d\n'%(Time,n))