"""
导入一个模块，Python解释器对模块位置的搜索顺序是：
1.当前目录
2.如果不再当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录.
3.如果都找不到，Python会查看默认路径，UNIX下，默认路径一般为/usr/local/lib/python/.
模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录,PYTHONPATH由安装过程决定慕容目录.

"""
# sys:python自身的运行环境

import sys
# 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.path)
# 查看版本
print(sys.version)
# argv:用list存储了命令行的所以参数,argv至少有一个元素，第一个参数永远是该.py文件的名称,写脚本时会用到
print(sys.argv)
# platform:获取当前执行环境的平台
print(sys.platform)
# exit:可以中途退出程序,参数非0时，会引发一个SystemExit异常，从而可以在主程序中捕获该异常
print(sys.exit())