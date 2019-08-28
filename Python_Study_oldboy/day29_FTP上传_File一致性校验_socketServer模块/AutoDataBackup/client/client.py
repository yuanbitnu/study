import socket
import struct
import os
import hashlib
import pickle
import time
# import schedule

file_dirpath = 'D:\\新建文件夹\\密保卡'  # 待发送文件的dir


def md5_opration(file_name):
    md5_obj = hashlib.md5()
    with open(file_name, mode='rb') as file_stream:
        for line in file_stream:
            md5_obj.update(line)
        return md5_obj.hexdigest()


def send_file(addressInfo, file_path):
    conn_socket = socket.socket()
    conn_socket.connect(addressInfo)
    while True:
        file_total_size = os.path.getsize(file_path)
        md5_val = md5_opration(file_path)
        fileInfo_dic = {"file_name": file_path,
                        "file_size": file_total_size, "file_md5_val": md5_val}
        fileInfo_dic_pickle = pickle.dumps(fileInfo_dic)
        fileInfo_dic_pickle_len = len(fileInfo_dic_pickle)

        head_byte = struct.pack(
            'i%ds' % fileInfo_dic_pickle_len, fileInfo_dic_pickle_len, fileInfo_dic_pickle)
        conn_socket.send(head_byte)

        with open(file_path, mode='rb') as file_stream:
            for line in file_stream:
                conn_socket.send(line)

        recv = conn_socket.recv(1024).decode('gbk')
        if recv == '200':
            conn_socket.close()
            break
        elif recv == '201':
            print('重新发送：')


def send_file_with_file_suffix(addressInfo, file_path, file_suffix):
    if os.path.splitext(file_path)[1] == file_suffix:
        send_file(addressInfo, file_path)
    elif file_suffix == '*':
        send_file(addressInfo, file_path)
    else:
        print('%s:不符合用户要求后缀' % file_path)


def get_all_fileAbsPath(path):
    file_lis = []
    if os.path.exists(path):
        while True:
            dir_lis = os.listdir(path)
            for item in dir_lis:
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path):
                    file_lis.append(full_path)
                elif os.path.isdir(full_path):
                    file_lis.extend(get_all_fileAbsPath(full_path))
            break
    return file_lis


def run(cmd, ip_port, file_suffix):
    while True:
        if cmd == 'exit':
            break
        elif cmd == 'run':
            all_fileAbsPath_lis = get_all_fileAbsPath(file_dirpath)
            for item in all_fileAbsPath_lis:
                # print(item)
                send_file_with_file_suffix(ip_port, item, file_suffix)
            break
        else:
            cmd = input('请重新输入命令>>>')


# ret = get_all_fileAbsPath('D:\\HBuilder文档')
# print(ret)

cmd = input('请输入命令>>>')
file_suffix = input('请输入需要copy文件的后缀名:')
# ip = input('请输入ip地址>>>')
# port = input('请输入端口号>>>')
IP_PORT = ('127.0.0.1', 8888)
# schedule.every().day.at("21:23").do(run, cmd, IP_PORT, file_suffix)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
run(cmd, IP_PORT, file_suffix)
