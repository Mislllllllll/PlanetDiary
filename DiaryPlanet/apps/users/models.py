# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import  datetime
# Create your models here.
class userProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称",default="")
    gender=models.CharField(choices=(("male",u"男"),("female",u"女")),default="female",max_length=20)
    blood_type=models.CharField(choices=(("AB",u"AB血型"),("A",u"A血型"),("B",u"B血型"),("O",u"O血型")),default="AB",max_length=20)
    star_type=models.CharField(max_length=50,default="")
    phone_num=models.CharField(max_length=11,default="",null=True,blank=True)
    image=models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta():
        verbose_name=u"用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username

class email_Verify(models.Model):
    verify_code=models.CharField(max_length=50,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱地址")
    send_type=models.CharField(max_length=50,choices=(("register",u"注册"),("forget"),u"忘记密码"))
    send_time=models.DateField(default=datetime.now)

    class Meta():
        verbose_name=u"登录邮箱验证码"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username

class banner(models.Model):
        title = models.CharField(max_length=50, verbose_name=u"标题")
        image = models.ImageField(upload_to="/banner/%Y/%m", verbose_name=u"轮播图片")
        url=models.CharField(max_length=100,verbose_name=u"访问地址")
        index=models.CharField(max_length=5,verbose_name=u"访问顺序")
        add_time=models.TimeField(default=datetime.now,verbose_name=u"添加时间")

        class Meta():
            verbose_name = u"轮播图"
            verbose_name_plural = verbose_name

        def __unicode__(self):
            return self.username