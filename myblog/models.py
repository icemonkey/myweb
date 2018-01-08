# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from django.db import models

# Create your models here.
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    
    #显示数据
    #def __unicode__(self):
    #   return u'{} {} {} {}'.format(self.sku, self.name, self.price, self.size)

    class Meta:
        #修改类型
        verbose_name = 'Product'
        #修改表名称
        verbose_name_plural= 'Product表'

  