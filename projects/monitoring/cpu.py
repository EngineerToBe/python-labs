#!/usr/bin/python3 -tt

import psutil
import time
import os
import logging

#get cpu percentage
cpu = psutil.cpu_percent()

t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print("{} cpu:{}%".format(current_time,cpu))


#msg="CPU utilization at ",current_time "is" cpu
#print ("CPU utilization at ",current_time)

print (current_time, cpu)
if not os.path.exists('./cpu.log'):
    os.mknod('./cpu.log')
