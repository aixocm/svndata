#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from   app01  import views
urlpatterns = [
    url(r'index/',views.index),
    url(r'cache/',views.cache_page),
    url(r'login/',views.login),
    url(r'home/',views.home),
    url(r'logout/$',views.logout),
]