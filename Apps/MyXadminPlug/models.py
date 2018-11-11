from django.db import models
from django.contrib.auth.models import AbstractUser  # 继承原有user同时增加自己的自定义user

from datetime import datetime


class UserProfile(AbstractUser):
    """
        自定义用户表单
    """
    phone = models.CharField(max_length=11, verbose_name='手机')
    hobby = models.CharField(max_length=20, null=True, blank=True, verbose_name='爱好')
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), verbose_name='性别')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserMessage(models.Model):
    """
    用户收到的消息
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    message = models.TextField(max_length=300, verbose_name='消息')
    has_read = models.CharField(choices=(('yes', '已读'), ('no', '没读')), max_length=10, default='no',
                                verbose_name='消息是否读过')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class DefinedFund(models.Model):
    """
    用户自定义
    """
    StuID = models.IntegerField(verbose_name='用户ID')
    StuNum = models.CharField(max_length=20, verbose_name='学号')
    Grade = models.CharField(max_length=10, verbose_name='成绩等级')

    class Meta:
        verbose_name = '自定义页数据'
        verbose_name_plural = verbose_name
