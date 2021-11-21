#!/usr/bin/python2.7
#coding: utf-8
import os,sys
K = ''
#判断当前用户是不是root
if os.getuid() != 0:
    print("当前用户不是root，请切换为root用户或使用sudo临时获取root权限")
    sys.exit(1)
#获取用户安装的Redis版本
version = raw_input('Please input wanted redis version:');K = version
if version == K:
    url = 'http://download.redis.io/releases/redis-{}.tar.gz'.format(K)
else:
    print("更多版本下载地址：http://download.redis.io/releases/ ")
    sys.exit(1)

#拼接源码包下载地址并执行命令
cmd = 'wget ' + url
res = os.system(cmd)
if res != 0:
    print("无法下载资源包请检查您的网络或检查您是否安装wget命令")
    sys.exit(1)

if version == K:
    package_version = 'redis-{}'.format(K)
#解压下载的源码包
cmd = 'tar -zxf' + package_version + '.tar.gz'
res = os.system(cmd)
#如果解压失败则删除下载的源码包并且提示用户重新执行脚本
if res != 0 :
    os.system('rm -f' + package_version + '.tar.gz')
    print("请重新执行脚本以安装redis")
    sys.exit(1)
#解压成功则进入解压后的源码目录中依次执行配置、编译、安装过程
cmd = 'cd ' + package_version + '&& make MALLOC=libc && make PREFIX=/usr/local/redis install && make install'
res = os.system(cmd)
#安装失败则提示用户安装失败了，让用户检查环境依赖
if res != 0:
    print("无法安装redis，请检查redis安装的依赖项！")
    sys.exit(1)
