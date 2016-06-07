#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wsgiref.simple_server import  make_server
from  jinja2 import Template
import time
from  url import url_list


if __name__ == '__main__':
    httpd = make_server('',8000,RunServer)
    print "Server HTTP on port 8000...."
    httpd.serve_forever()
