import itchat
import time

print("请扫描弹出的二维码")
itchat.auto_login(hotReload=True)
boom_name = input("请输入想发送的人： ")
message = input("请输入发送的内容: ")
number = int(input("请输入发送的次数: "))
boom_obj = itchat.search_friends(remarkName=boom_name)[0]['UserName']


for i in range(1,number+1):
    time.sleep(0.01)
    print("正在发送第%d遍" %i)
    itchat.send_msg(msg=message,toUserName=boom_obj)