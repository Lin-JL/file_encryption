import os
import sys

from helper.func import get_filepath, get_password, get_operation
from helper.secret import encrypt_dir, decrypt_dir

extension_name = '.myenc'


while True:
    file_path = get_filepath()
    choice = get_operation()
    password = get_password()

    dirname = os.path.dirname(file_path)
    if choice == 'e':
        filename = os.path.basename(file_path) + extension_name
        output_file_path = os.path.join(dirname, filename)
        encrypt_dir(file_path, password, output_file_path)
        print('加密完成\n')
    else:
        filename = os.path.basename(file_path)
        if filename[-len(extension_name):] == extension_name:
            filename = filename[:-len(extension_name)]
        else:
            filename = '解密_' + filename
        output_file_path = os.path.join(dirname, filename)
        decrypt_dir(file_path, password, output_file_path)
        print('解密完成\n')

