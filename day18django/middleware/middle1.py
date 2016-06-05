#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import  HttpResponse
class mmm(object):
    def  process_request(self,request):
        print "mmm.process_request"
       # return HttpResponse('sb')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print "mmm.process_view"
    def process_response(self, request, response):
        print "mmm.process_response"
        return response
    def process_exception(self,request,exception):
        print "error mmm"
        return request

class xxx(object):
    def  process_request(self,request):
        return  "xxx.process_request"
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print "xxx.process_view"
    def process_response(self, request, response):
        print "xxx.process_response"
        return response
    def process_exception(self,request,exception):
        print "error xxx",exception
        return request
