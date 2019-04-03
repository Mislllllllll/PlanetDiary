# -*- coding: utf-8 -*-
from django.db import models
from datetime import  datetime
# Create your models here.
class video(models.Model):
    video_name=models.CharField(max_length=100,verbose_name=u"视频名称")
    video_time=models.CharField(max_length=100,verbose_name=u"视频时长")
    video_people= models.CharField(max_length=50,verbose_name=u"视频播放人数")
    video_star=models.CharField(max_length=50,verbose_name=u"视频收藏人数")
    video_comment=models.CharField(max_length=100,verbose_name=u"视频评论")
    video_brief=models.CharField(max_length=200,verbose_name=u"视频简介")
    video_author=models.CharField(max_length=100,verbose_name=u"视频作者")
    video_club=models.CharField(max_length=100,verbose_name=u"视频所属部落")
    video_addtime=models.DateField(default=datetime.time,verbose_name=u"视频上传时间")
    