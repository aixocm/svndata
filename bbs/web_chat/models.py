from django.db import models
from  web.models import UserProfiles
# Create your models here.



class QQGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    description = models.CharField(max_length=255,default="nothing")
    memebers = models.ManyToManyField(UserProfiles,blank=True)
    admins = models.ManyToManyField(UserProfiles,related_name='group_admins')
    max_member_nums = models.IntegerField(default=200)
    def __unicode__(self):
        return self.name

