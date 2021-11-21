#!/usr/bin/python2.7
# coding:utf-8
import os
import sys
Project = ['eurekaserver',
           'payserver',
           'travelmanage',
           'userserver',
           'configserver',
           'ferriswheelclient',
           'pushserver',
           'tdserver']
Start = 'start'
Stop = 'stop'
Status = 'status'
Sieve = []
Path = "/mnt/ferriswheel/"

Parameter = sys.argv[1]
Variety = sys.argv[2]

# 声明函数必须有空格


def start_function():
    os.chdir(Path+"{}".format(Parameter))
    os.system("nohup java -jar *.jar &")
    print("{}程序启动成功！！！".format(Parameter))


def stop_function():
    process = os.system("jps -l | grep {} | gawk -F ' ' '{{print $1}}' | xargs kill -9".format(Parameter))
    print("已关闭{}进程".format(Parameter))


def status_function():
# os.system("jps -l | grep {} | gawk 'NR == 1' | gawk -F ' ' '{{print $1}}'".format(Parameter))
    if os.system("jps -l | grep {} | gawk 'NR == 1' | wc -l >/dev/null 2>&1".format(Parameter)) != 0:
        os.system("echo {}正在运行".format(Parameter))
    else:
        os.system("echo {}未运行".format(Parameter))

for i in Project:
    Sieve.append(i)
    if Sieve[-1] == Parameter and Variety == Start:
        start_function()
        break
    elif Sieve[-1] == Parameter and Variety == Stop:
        stop_function()
        break
    elif Sieve[-1] == Parameter and Variety == Status:
        status_function()
        break
    else:
        print("请输入正确的start|stop|status")
        break


