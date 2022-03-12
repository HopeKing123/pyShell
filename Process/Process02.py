# 自定义进程：通过继承父类Process来开发所需求的功能
from multiprocessing import Process


class MyProcess(Process):

    # 定义属性
    def __init__(self, name):
        # 继承父类方法
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法
    def run(self) -> None:
        n = 1
        while True:
            print('序号：{}，自定义进程,{}'.format(n,self.name))
            n += 1


if __name__ == '__main__':
    p1 = MyProcess('小明')
    p1.start()
    p2 = MyProcess('小红')
    p2.start()
