# 文件复制
import os
import time

src_path = r'I:\p1'
des_path = r'I:\p2'


# 封装函数
def copy(src, des):
        if os.path.isdir(src) and os.path.isdir(des):
            filelist = os.listdir(src)

            for file in filelist:
                path = os.path.join(src, file)
                # 判断是文件夹还是文件
                if os.path.isdir(path):
                    # 递归调用copy
                    path1 = os.path.join(des,file)
                    os.mkdir(path1)
                    # 重复读取父目录下子目录中的内容
                    copy(path,path1)
                else:
                    with open(path, 'rb') as rstream:
                        container = rstream.read()

                        path1 = os.path.join(des, file)
                        with open(path1, 'wb') as wstream:
                            wstream.write(container)
            else:
                print('复制完成！')


# 调用函数
if os.path.exists(des_path):
    print('已创建')
    copy(src_path, des_path)
else:
    print('没有创建，正在创建')
    os.mkdir(des_path)
    time.sleep(3)
    print('创建完成！')
    copy(src_path, des_path)