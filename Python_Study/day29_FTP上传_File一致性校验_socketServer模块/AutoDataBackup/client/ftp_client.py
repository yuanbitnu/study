import socket
import struct
import os
import hashlib
import pickle


def md5_opration(file_name):
    md5_obj = hashlib.md5()
    with open(file_name, mode='rb') as file_stream:
        for line in file_stream:
            md5_obj.update(line)
        return md5_obj.hexdigest()


while True:
    cmd = input('请输入命令>>>')
    ip = input('请输入ip地址>>>')
    port = input('请输入端口号>>>')
    if cmd == 'exit':
        break
    else cmd == 'run':
        IP_PORT = (ip, int(port))
        conn_socket = socket.socket()
        conn_socket.connect(IP_PORT)
        while True:
            action, file_name = cmd.strip().split(' ')
            file_total_size = os.path.getsize(file_name)
            md5_val = md5_opration(file_name)
            file_info_dic = {"action": action, "file_name": file_name,
                             "file_size": file_total_size, "file_md5_val": md5_val}

            file_info_dic_pickle = pickle.dumps(file_info_dic)
            file_info_dic_pickle_len = len(file_info_dic_pickle)

            head_byte = struct.pack('i%ds' % file_info_dic_pickle_len,
                                    file_info_dic_pickle_len, file_info_dic_pickle)
            conn_socket.send(head_byte)

            with open(file_name, mode='rb') as file_stream:
                for line in file_stream:
                    conn_socket.send(line)

            recv = conn_socket.recv(1024).decode('gbk')
            if recv == '200':
                conn_socket.close()
                break
            elif recv == '201':
                cmd = input('MD5校验失败，请重新输入命令>>>')
