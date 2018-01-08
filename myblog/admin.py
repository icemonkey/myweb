# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myblog.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    #显示数据的列
    list_display = ('sku','name','price','size')
    #显示搜索栏
    search_fields = ('name','price')
    #添加快速过滤
    list_filter = ('name','price')

admin.site.register(Product,ProductAdmin)