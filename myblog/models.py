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
    
    sku = models.CharField(max_length=5, verbose_name='sku号码')
    name = models.CharField(max_length=20, verbose_name='名称')
    price = models.PositiveIntegerField(verbose_name='价格')
    size = models.CharField(max_length=1, choices=SIZES, verbose_name='尺寸')
    
    #显示数据
    #def __unicode__(self):
    #   return u'{} {} {} {}'.format(self.sku, self.name, self.price, self.size)

    class Meta:
        #修改类型
        verbose_name = 'Product'
        #修改表名称
        verbose_name_plural= 'Product表'

  