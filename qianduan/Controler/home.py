#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import  make_server
from  jinja2 import Template
import time
from  url import url_list
def index():
    # return "index"
    data = open('Views/index.html').read()
    current_time = str(time.time())

    template = Template(data)
    result = template.render(
            name='alex',
            age='83',
            current_time = current_time,
            user_list = ['ALEX','ERIC','HDFJ'],num = 2
    )
    return result.encode('utf-8')

def dali():
    # return "dali"
    data = open('Views/dali.html').read()
    return data

def alex():
    return "alex 123"
