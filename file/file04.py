# �ļ�����
import os
import time

src_path = r'I:\p1'
des_path = r'I:\p2'


# ��װ����
def copy(src, des):
        if os.path.isdir(src) and os.path.isdir(des):
            filelist = os.listdir(src)

            for file in filelist:
                path = os.path.join(src, file)
                # �ж����ļ��л����ļ�
                if os.path.isdir(path):
                    # �ݹ����copy
                    path1 = os.path.join(des,file)
                    os.mkdir(path1)
                    # �ظ���ȡ��Ŀ¼����Ŀ¼�е�����
                    copy(path,path1)
                else:
                    with open(path, 'rb') as rstream:
                        container = rstream.read()

                        path1 = os.path.join(des, file)
                        with open(path1, 'wb') as wstream:
                            wstream.write(container)
            else:
                print('������ɣ�')


# ���ú���
if os.path.exists(des_path):
    print('�Ѵ���')
    copy(src_path, des_path)
else:
    print('û�д��������ڴ���')
    os.mkdir(des_path)
    time.sleep(3)
    print('������ɣ�')
    copy(src_path, des_path)