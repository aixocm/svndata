#!/usr/bin/env python
# -*- coding:utf-8 -*-
def f1():
    return 'this is home/f1'
def f2():
    return 'This is home/f2'
def f3():
    return 'This is home/f3'
class A:
    static_name='KKK'
    def __init__(self):
        self.name='JJ'
    def show(self):
        pass
    @staticmethod
    def static_show():
        print 'xixi'