#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,sex,job,address):
        self.name=name
        self.sex=sex
        self.job=job
        self.address=address

    def speak(self):
        print 'hello,my name is',self.name,'nice to meet you!'

    def message(self):


