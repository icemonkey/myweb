#coding=utf-8
import MySQLdb
import re
import sys
import os
import datetime
import datetime as dtime

base_dir = "/zq/cutuid/"

def lastmonth():
   today=datetime.date.today()
   twoday=datetime.timedelta(days=7)
   yesterday=today-twoday
   return yesterday.strftime('%Y%m')
lastmonth = lastmonth()

reslog = base_dir + 'res.log'
reslog1 = base_dir + 'res1.log'

cutlog1 = 'cat '+ reslog+ ' | sort | uniq >> '+ reslog1
#print cutlog1
os.system(cutlog1)

conn= MySQLdb.connect(
        host='10.20.100.203',
        port = 3306,
        user='yw_statistics',
        passwd='yw_statistics',
        db ='m2_log_uid',
        )
cur = conn.cursor()
#创建数据表
#cur.execute("create table m2_log_uid_2017(id int not null auto_increment primary key ,uid varchar(20),datetime varchar(20)) auto_increment=1")
#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

with open(reslog1) as f:
    for line in f.readlines():
        line = str(line)
        sql1 = "insert into m2_log_uid_2017 (uid,datetime) values ("
        sql2 = line + "," +str(lastmonth)+');'
        sql = sql1 + sql2
        #print sql
        cur.execute(sql)
        conn.commit()
#修改查询条件的数据
#cur.execute(sql)
#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.close()

#base_dir = "/zq/cutuid/"
mvfile = 'mv ' + reslog1 + ' ' + base_dir + 'm2_uid.log.' + str(lastmonth)
rmfile = 'rm -rf ' + base_dir + 'res.log'
#print(mvfile)
os.system(mvfile)
os.system(rmfile)

