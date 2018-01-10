#!/usr/bin/env python
# -*- coding:utf-8 -*-
#发布
from RedisHelper import RedisHelper

obj = RedisHelper()
obj.publish('你好'.decode('utf-8'))#发布