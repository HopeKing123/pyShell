# psutil：跨平台对系统监控,支持Linux/OSX/Windows等，大多数用在Linux上
import psutil
"""
获取CPU信息
>>> psutil.cpu_count()  # CPU逻辑数量
1
>>> psutil.cpu_count(logical=False)  # CPU物理核心
1

统计CPU的用户/系统/空闲时间:
>>> psutil.cpu_times()
scputimes(user=273609.87, nice=1096.07, system=278325.64, idle=14621619.68, iowait=6167.03, irq=0.0, softirq=1127.34, steal=0.0, guest=0.0, guest_nice=0.0)

# 实现类似于top命令的cpu使用率，每秒刷新一次，累计十次.
>>> for x in range(10):
...     print(psutil.cpu_percent(interval=1, percpu=True))


获取内存信息
使用psutil获取物理内存和交换内存信息，分别使用：
>>> psutil.virtual_memory()
svmem(total=2097086464, available=1003679744, percent=52.1, used=895107072, free=134893568, active=995336192, inactive=746115072, buffers=141500416, cached=925585408, shared=5808128, slab=166690816)
>>> psutil.swap_memory()
sswap(total=2047995904, used=311758848, free=1736237056, percent=15.2, sin=50343936, sout=419262464)

返回的是字节为单位的整数，可以看到，总内存大小是2097086464 = 2GB 已用895107072 = 826M,
交换分区大小是2047995904 = 20GB


获取磁盘信息
可以通过psutil获取磁盘分区，磁盘使用率和磁盘IO信息：
>>> psutil.disk_partitions()    # 磁盘分区信息
[sdiskpart(device='/dev/vda1', mountpoint='/', fstype='ext4', opts='rw,relatime,errors=remount-ro,data=ordered', maxfile=255, maxpath=4096)]
>>> psutil.disk_usage('/')      # 磁盘使用情况
sdiskusage(total=42140479488, used=13504188416, free=26686947328, percent=33.6)
>>> psutil.disk_io_counters()   # 磁盘IO
sdiskio(read_count=715655, write_count=22065466, read_bytes=27534892544, write_bytes=480235439104, read_time=1882768, write_time=27656920, read_merged_count=7498, write_merged_count=25945498, busy_time=9293272)


获取网络信息:
psutil可以获取网络接口和网络连接信息：
psutil.net_io_counters()    # 获取网络读写字节/包的个数
psutil.net_if_addrs()       # 获取网络接口信息
psutil.net_connections()    # 获取当前网络连接信息


获取进程信息:
通过psutil可以获取所有进程的详细信息:
psutil.pids()   # 所有进程ID
p = psutil.Process(指定进程)    # 获取指定进程，其实就是当前python交互环境
p.name() # 进程名称
p.ext()  # 进程exe路径
p.cwd()  # 进程工作目录
p.cmdline() # 进程启动的命令行
p.ppid() # 父进程ID
p.parent() # 父进程
p.children()    # 子进程列表
p.status()  # 进程状态
p.username() # 进程用户名
p.create_time() # 进程创建时间
p.terminal()    # 进程终端
p.cpu_times()   # 进程使用的CPU时间
p.memory_info() # 进程使用的内存   # 注意ps输出以千字节为单位,而psutil的rss以字节为单位
p.open_files()  # 进程打开的文件
p.connections() # 进程相关网络连接
p.num_threads() # 进程的线程数量
p.threads()     # 所有线程信息
p.environ()     # 进程环境变量
p.terminate()   # 结束进程，自己结束自己

# 模拟ps命令结果
psutil.test()

# 查看运行用户
psutil.users()

"""
