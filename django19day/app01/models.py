#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class  UserInfo(models.Model):
    USER_TYPE_LIST = (
        (1,'f'),
        (2,'fdg'),
    )
    user_type = models.IntegerField(choices=USER_TYPE_LIST,default=1)
    name = models.CharField(max_length=32,verbose_name="姓名",db_column='KJH',unique=True)
    email = models.EmailField(max_length=32,null=True)
    email2 = models.EmailField(max_length=32,default="1755897532@qq.com")
    ip = models.GenericIPAddressField(protocol="ipv4",null=True,blank=True)
    img = models.ImageField(null=True,blank=True,upload_to="upload")
    ctime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(auto_now_add=True)

    def  __unicode__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=16)


class Somthing(models.Model):
    c1=models.CharField(max_length=16)
    c2=models.CharField(max_length=16)
    c3=models.CharField(max_length=16)
    c4=models.CharField(max_length=16)
    color = models.ForeignKey(Color)


class Business(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    name1 = models.CharField(max_length=16,null=True)

class Host(models.Model):
    hostname = models.CharField(max_length=32)
    business = models.ForeignKey('Business',to_field='nid')


class UserGroup(models.Model):
    group_name = models.CharField(max_length=16)

class  User(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)
    user_user_group = models.ManyToManyField('UserGroup')

class User2(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)


class  AAdmin(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    user_info  = models.OneToOneField('User2')

class  SimpleModel(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

class  UserGroup_New(models.Model):
    caption=models.CharField(max_length=64)
    def __unicode__(self):
        return self.caption

class  User_New(models.Model):
    username = models.CharField(max_length=64)
    user_group = models.ForeignKey('UserGroup_New')
    def  __unicode__(self):
        return self.hostname

