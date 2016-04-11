#!/usr/bin/env python
# -*- coding:utf-8 -*-
import  event_drive
class  MyClass(event_drive.BaseHandler):
    def execute(self):
        print "hehheehheh"

event_drive.event_list.append(MyClass)
event_drive.run()
