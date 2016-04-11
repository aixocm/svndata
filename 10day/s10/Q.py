#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process,Array,Pool



def foo(i):
    return i+100
def Bar(arg):
    print arg
pool = Pool(5)
print pool.apply()

