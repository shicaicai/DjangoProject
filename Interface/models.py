# -*- coding: utf-8 -*-
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField("event time")
    create_time = models.DateTimeField('auto_now=True')

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField()

    # 模型类的一个内部类，定于一些行为特性，unique_together用于设置两个字段为联合主键
    class Meta:
        unique_together = ('event', 'phone')

    # __str__方法告诉python对象以str的方式显示
    def __str__(self):
        return self.real_name
