# -- coding: utf-8 --
# GUI编程
"""
Python支持多种图形界面的第三方库，包括：
    Tk
    wxWidgets
    Qt
    GTK
Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。

Tkinter:
我们编写的Python代码会调用内置的Tkinter（编程），Tkinter封装了访问Tk的接口；
Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；
Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。
所以，我们的代码只需要调用Tkinter提供的接口就可以了。
"""

# 导入Tkinter包中__init__.py文件（__all__）允许的内容
from tkinter import *
# 导入tkinter包中的messagebox类(tk通用消息框)
import tkinter.messagebox as messagebox
# 导入tkinter包中的filedialog类(文件选择对话框类)
import tkinter.filedialog as filedialog
# 导入selenium WEB包中的webdriver类
from selenium import webdriver

# 导入模块
import base64, requests, json, random

# 创建Application类，继承父类Frame
"""
Frame 框架小部件，可能包含其他小部件
在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。
"""


# 父容器
class Application(Frame):
    # 定义属性
    def __init__(self, master=None, ):
        # 继承父类属性
        # 参数：bg:背景颜色，bd：边框大小，relief：边框的3D样式，cursor：鼠标移动的样式
        Frame.__init__(self, master, bd=200, relief="groove", cursor="arrow")
        # pack()方法把Widget加入到父容器中，并实现布局,是最简单的布局，grid()可以实现更复杂的布局。
        # 把Widget（装置）加入到父容器中，并实现布局，这里是将自身加入父容器中
        self.pack()
        # 把Widget（装置）加入到父容器中，并实现布局，这里是将方法加入父容器中
        self.createWidgets()
        self.createPage()

    # 图像增强部件方法
    # 创建createWidgets(装置)方法（子容器）
    def createWidgets(self):
        # 按钮小部件。
        # 用父控件构建一个按钮小部件。
        self.alertButton = Button(self, text="图像增强按钮", height="10", width="15",
                                  command=self.FileSelectionBox)
        # 把Widget（装置）加入到父容器中，并实现布局
        self.alertButton.pack(side='left')

    # 创建页面部件方法
    # 创建createPage(装置)方法（子容器）
    def createPage(self):
        self.pageInput = Entry(self)
        self.pageInput.pack()
        # 按钮小部件。
        # 用父控件构建一个按钮小部件。
        self.pageButton = Button(self, text="页面搜索按钮", height="10", width="15",
                                 command=self.pagePop)
        # 把Widget（装置）加入到父容器中，并实现布局
        self.pageButton.pack(side='left')

    # 页面弹出方法
    def pagePop(self):
        # 获取用户输入数据
        User = self.pageInput.get()
        Web = webdriver.Chrome()
        Web.get(User)
        Web.close()

    # 文件选择框方法
    def FileSelectionBox(self):
        # 选择文件
        self.Filepath = filedialog.askopenfilenames()
        if self.Filepath != "":
            for i in self.Filepath:
                self.Filepath = i
                print(self.Filepath)
                # self.Filepath = ",".join(self.Filepath)
                self.imageEnhancement()
                self.createSubassemblies()
        elif self.Filepath == "":
            self.createSMessagepart()

    # 创建图形增强方法：
    def imageEnhancement(self):
        # 图像清晰度增强逻辑代码

        '''
        图像清晰度增强
        '''

        # 百度图像增强API
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"
        # 二进制方式打开图片文件
        f = open(self.Filepath, 'rb')
        # 二进制图片文件base64编码
        img = base64.b64encode(f.read())

        # 变量字典
        params = {"image": img}
        # 百度权威Token
        access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        # 完整请求url
        request_url = request_url + "?access_token=" + access_token
        # Body头部变量
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        # 向指定的资源提交要被处理的数据。
        response = requests.post(request_url, data=params, headers=headers)
        # 判读返回值是否为True
        if response:
            # print (response.json())
            # 返回响应的内容为json编码
            response_b64encode = response.json()
            # 格式化返回(将“obj”序列化为JSON格式的“str”``)
            json_dumps = json.dumps(response_b64encode, indent=4, sort_keys=True, ensure_ascii=False)
            # 将已编码的 JSON 字符串解码为 Python 对象
            json_loads = json.loads(json_dumps)
            # 获取下标位
            response_b64decode = json_loads['image']
            # print(response_b64decode)
            # 将获取的下标位变量进行base64解码
            new = base64.b64decode(response_b64decode)
            # 解码图片保存
            number = random.randrange(1, 100000000, 2)
            with open(str(number) + '.jpeg', 'wb') as w:
                w.write(new)

        print('图像处理成功...')

    # 创建子容器的Widgets(部件)方法：
    def createSubassemblies(self):
        # 按钮小部件。
        # 用子容器构建一个退出按钮小部件。
        messagebox.showinfo(title="文件", message="图像处理成功！")

    # 创建子容器的Widgets(部件)方法：
    def createSMessagepart(self):
        # 按钮小部件。
        # 用子容器构建一个退出按钮小部件。
        messagebox.showinfo(title="文件", message="请选择文件")


if __name__ == '__main__':
    # 实例化Application
    app = Application()
    #  设置窗口标题:
    app.master.title('图形增强软件程序')
    # 调用主消息循环:
    app.mainloop()
