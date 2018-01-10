#!/usr/bin/env python
# -*- coding:utf-8 -*-
#订阅
from RedisHelper import RedisHelper
import sys

sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('UTF-8')
sys.getdefaultencoding()

obj = RedisHelper()
redis_sub = obj.subscribe()#调用订阅方法


while True:
    msg= redis_sub.parse_response()
    print ("收到订阅消息 {}".format((msg)[2])).decode('utf-8')
    #print "收到订阅消息 {}".format((msg)[2])
