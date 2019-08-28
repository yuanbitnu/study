import socket
import struct
import subprocess

IP_PORT = ('127.0.0.1', 65445)

socket_ser = socket.socket()  # 创建socket 对象
socket_ser.bind(IP_PORT)  # 为socket对象绑定ip和端口号
socket_ser.listen(5)  # 设置侦听排队数量

while True:
    new_socket, ipaddr = socket_ser.accept()  # 此处会阻塞，等待客户端连接
    while True:
        recv_data = new_socket.recv(1024).decode(
            encoding='utf-8')  # 此处会阻塞，接受客户端发送的数据
        if recv_data == 'exit':
            new_socket.close()  # 关闭通信socket
            break
        else:
            # 创建一个子进程执行从客户端接收到的shell命令
            com_pro = subprocess.run(recv_data, capture_output=True)
            stdout = com_pro.stdout  # 获取正确结果的输出
            stderr = com_pro.stderr  # 获取错误结果的输出
            if stdout is not None:
                length = len(stdout)  # 计算出数据(字节)的总长度
                print(length)
                # 将数据总长度以及数据 通过相应的格式，通过pack()方法编码组合成一个"字节字符串"
                head = struct.pack('i%ds' % length, length, stdout)
                # head = struct.pack('i', length) # 将一个int类型的参数按照格式“i”(4个字节)进行编码，返回一个字节字符串
                new_socket.send(head)  # 发送数据给客户端
            elif stderr is not None:
                length = len(stderr)
                head = struct.pack('i%ds' % length, length, stderr)
    new_socket.close()
