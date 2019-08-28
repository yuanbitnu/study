import socket
import struct
import os
import pickle
import hashlib


def md5_opration(file_name):
    md5_obj = hashlib.md5()
    with open(file_name, mode='rb') as file_stream:
        for line in file_stream:
            md5_obj.update(line)
        return md5_obj.hexdigest()


ipaddr = ip_addr = socket.gethostbyname(socket.gethostname())

IP_PORT = (ipaddr, 8888)

ser_socket = socket.socket()
ser_socket.bind(IP_PORT)
ser_socket.listen(5)

while True:
    try:
        conn_socket, ipaddr = ser_socket.accept()
        while True:
            rec_fileInfo_len = conn_socket.recv(
                struct.calcsize('i'))  # return byet
            fileInfo_len = struct.unpack('i', rec_fileInfo_len)

            rec_fileInfo_dic = conn_socket.recv(fileInfo_len[0])
            fileInfo_dic = pickle.loads(rec_fileInfo_dic)

            action = fileInfo_dic['action']
            file_name = fileInfo_dic['file_name']
            file_size = fileInfo_dic['file_size']
            file_md5_val = fileInfo_dic['file_md5_val']

            has_recv_data_len = 0
            with open(file_name, mode='wb') as file_stream:
                while has_recv_data_len < file_size:
                    recv_data = conn_socket.recv(1024)
                    file_stream.write(recv_data)
                    has_recv_data_len += len(recv_data)
                    print('%s文件总大小为%d，已接受%d' %
                          (file_name, file_size, has_recv_data_len))
                print('文件已经接收完成，开始进行MD5校验>>>>')
            local_file_md5_val = md5_opration(file_name)
            print('local_file_md5_val', local_file_md5_val)
            print('file_md5_val', file_md5_val)
            if local_file_md5_val == file_md5_val:
                print('校验通过')
                print(os.path.abspath(file_name))
                conn_socket.send(b'200')
                conn_socket.close()
                break
            else:
                print('校验失败')
                conn_socket.send(b'201')
                os.remove(file_name)
                conn_socket.close()
                break

        # while True:
        #     with open('444.jpg', mode='ab') as file_stream:
        #         while True:
        #             rec_data_len = conn_socket.recv(
        #                 struct.calcsize('i'))  # return byet
        #             data_len = struct.unpack('i', rec_data_len)
        #             print(data_len[0])
        #             recv_data = conn_socket.recv(data_len[0])
        #             file_stream.write(recv_data)
    except Exception:
        break
