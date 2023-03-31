import sys
import os


# 获取文件/目录路径
def get_filepath():
    file_path = input('输入要操作的文件/目录(退出程序: -1): ')
    while True:
        if file_path == '-1':
            sys.exit()
        if not os.path.exists(file_path):
            file_path = input('文件/目录不存在，重新输入(退出程序: -1): ')
        else:
            break
    return file_path


# 获取操作类型
def get_operation():
    operate = input('输入操作(e:加密  d:解密)(退出程序: -1): ')
    while True:
        if operate == '-1':
            sys.exit()
        if operate == 'e' or operate == 'd':
            break
        else:
            operate = input('输入错误，重新输入: ')
    return operate


# 获取密码
def get_password():
    password = input('输入6-16位密码(退出程序: -1): ')
    while True:
        if password == '-1':
            sys.exit()
        if len(password) < 6 or len(password) > 16:
            password = input('请输入6-16位密码(退出程序: -1): ')
        else:
            break
    return password
