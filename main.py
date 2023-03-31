import os
import sys

from helper.func import get_filepath, get_password, get_operation
from helper.secret import encrypt_dir, decrypt_dir


while True:
    file_path = get_filepath()
    choice = get_operation()
    password = get_password()

    dirname = os.path.dirname(file_path)
    if choice == 'e':
        filename = '加密_' + os.path.basename(file_path)
        output_file_path = os.path.join(dirname, filename)
        encrypt_dir(file_path, password, output_file_path)
        print('加密完成\n')
    else:
        filename = '解密_' + os.path.basename(file_path)
        output_file_path = os.path.join(dirname, filename)
        decrypt_dir(file_path, password, output_file_path)
        print('解密完成\n')

