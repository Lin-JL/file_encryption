import os
import sys


# 密码转化
def password_convert(password):
    total = 0
    for c in password:
        total += ord(c) ** 2

    convert_pwd = []
    for i in range(len(password)):
        convert_pwd.append((total + i * ord(password[i])) % 255)

    return convert_pwd


# 获取是否覆盖文件
def get_is_cover(path):
    choice = input(path + '已存在，是否覆盖(y/n)(退出程序: -1): ')
    while True:
        if choice == '-1':
            sys.exit()
        elif choice == 'y' or choice == 'Y':
            return True
        elif choice == 'n' or choice == 'N':
            return False
        else:
            choice = input('请正确输入(y/n)(退出程序: -1): ')


# 加密文件
def encrypt(filename, password, output_file_path, cover=None):
    try:
        fo = open(filename, 'rb')
        f_read = fo.read()
    except Exception as e:
        print('读取文件异常(加密): ' + str(e))

    if os.path.exists(output_file_path):
        if cover is None:
            cover = get_is_cover(output_file_path)
        if not cover:
            return

    try:
        f_write = open(output_file_path, 'wb+')
    except Exception as e:
        print('写入文件异常(加密): ' + str(e))

    convert_pwd = password_convert(password)
    position_pwd = convert_pwd[::-1]

    file_len = len(f_read)
    pwd_len = len(password)
    for i in range(file_len):
        new_byte = f_read[i] ^ convert_pwd[i % pwd_len]
        f_write.write(bytes([new_byte]))

    for i in range(pwd_len):
        f_write.seek(0)
        content = f_write.read()
        pos = position_pwd[i] % len(content)
        f_write.seek(pos)
        insert_byte = bytes([convert_pwd[i]])
        f_write.write(insert_byte + content[pos:])
    fo.close()
    f_write.close()


# 解密文件
def decrypt(filename, password, output_file_path, cover=None):
    try:
        fo = open(filename, 'rb')
        f_read = fo.read()
    except Exception as e:
        print('读取文件异常(解密): ' + str(e))

    if os.path.exists(output_file_path):
        if cover is None:
            cover = get_is_cover(output_file_path)
        if not cover:
            return

    try:
        f_write = open(output_file_path, 'wb')
    except Exception as e:
        print('写入文件异常(解密): ' + str(e))

    convert_pwd = password_convert(password)
    pwd_len = len(password)

    for i in range(pwd_len):
        pos = convert_pwd[i] % (len(f_read) - 1)
        f_read = f_read[:pos] + f_read[pos + 1:]

    for i in range(len(f_read)):
        new_byte = f_read[i] ^ convert_pwd[i % pwd_len]
        f_write.write(bytes([new_byte]))

    fo.close()
    f_write.close()


# 加密文件夹
def encrypt_dir(dirname, password, output_dir_path, cover=None):
    if not os.path.exists(dirname):
        print('文件/目录不存在:' + dirname)
        sys.exit()

    if os.path.isfile(dirname):
        encrypt(dirname, password, output_dir_path, cover)
    elif os.path.isdir(dirname):
        if os.path.exists(output_dir_path):
            if cover == None:
                cover = get_is_cover(output_dir_path)
            if not cover:
                return
        else:
            try:
                os.makedirs(output_dir_path)
            except Exception as e:
                print('创建文件夹异常: ' + str(e))
                sys.exit()

        child_path = os.listdir(dirname)
        for c in child_path:
            input_path = os.path.join(dirname, c)
            output_path = os.path.join(output_dir_path, '加密_' + c)
            encrypt_dir(input_path, password, output_path, cover)
    else:
        print('encrypt_dir出错了')
        sys.exit()


# 解密文件夹
def decrypt_dir(dirname, password, output_dir_path, cover=None):
    if not os.path.exists(dirname):
        print('文件/目录不存在:' + dirname)
        sys.exit()

    if os.path.isfile(dirname):
        decrypt(dirname, password, output_dir_path, cover)
    elif os.path.isdir(dirname):
        if os.path.exists(output_dir_path):
            if cover == None:
                cover = get_is_cover(output_dir_path)
            if not cover:
                return
        else:
            try:
                os.makedirs(output_dir_path)
            except Exception as e:
                print('创建文件夹异常: ' + str(e))
                sys.exit()

        child_path = os.listdir(dirname)
        for c in child_path:
            input_path = os.path.join(dirname, c)
            output_path = os.path.join(output_dir_path, '解密_' + c)
            decrypt_dir(input_path, password, output_path, cover)
    else:
        print('decrypt_dir出错了')
        sys.exit()
