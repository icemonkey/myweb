#coding:utf-8
import re
import sys
import os
import datetime
import datetime as dtime

def getYesterday():
   today=datetime.date.today()
   twoday=datetime.timedelta(days=1)
   yesterday=today-twoday
   return yesterday.strftime('%Y-%m-%d')
yes = getYesterday();

base_dir = "/zq/cutuid/"
#2017-12-16-0000-2330_m2.yiwang.com.cn.log.gz
logfile = base_dir+str(yes)+"-0000-2330_m2.yiwang.com.cn.log"
templog = base_dir+"temp.log"
reslog = base_dir+"res.log"

##scp 100.103 log to 100.203
logfile1 = str(yes)+"-0000-2330_m2.yiwang.com.cn.log"
cpfile = 'scp leaf@10.20.100.103:/data/cdnlogs/m2.yiwang.com/'+logfile1+'.gz ' +base_dir
unzipfile = 'gunzip ' + logfile+'.gz'
#print logfile
#print templog
#print reslog
#print cpfile
#print unzipfile
os.system(cpfile)
os.system(unzipfile)


def cutlog():
    pattern = "&.*?&uid=(\d+)"
    reuid = re.compile(pattern)
    with open(logfile) as f:
        for lines in f.readlines():
            a = reuid.findall(lines)
            with open(templog, 'a') as f:
                astr = str(a).strip("['']")
                if astr:
                    f.write(astr+'\n') 
cutlog()


cutlog1 = 'cat '+ templog+ ' | sort | uniq >> '+ reslog
#print cutlog1
os.system(cutlog1)

dellogfile = 'rm -rf '+ logfile
deltempfile = 'rm -rf '+ templog
#print(dellogfile)        
#print(deltempfile)        
os.system(dellogfile)
os.system(deltempfile)



