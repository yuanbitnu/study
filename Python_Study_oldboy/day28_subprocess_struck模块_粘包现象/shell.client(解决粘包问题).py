import socket
import struct


IP_PORT = ('127.0.0.1', 65445)

conn_socket = socket.socket()  # 创建一个socket对象
conn_socket.connect(IP_PORT)  # 连接服务器
while True:
    cmd = input('请输入命令>>>')
    conn_socket.send(cmd.encode(encoding='utf-8'))  # 向服务器发送数据

    byte_size = struct.calcsize('i')  # 计算'i'格式所占的字节长度
    recv_len_data = conn_socket.recv(byte_size)  # 按照byte_size字节长度接受特定字节数据
    len_data = struct.unpack('i', recv_len_data)  # 按照"i"格式通过unpack()方法还原出原始数据，返回值是一个元组
    # 以上三条语句，从接受到的字节数据中获取到了服务端传递过来的关于数据总长度的数据

    recv_total_len = 0
    recv_total_data = b''
    while recv_total_len < len_data[0]: # 将已接受数据的字节数跟数据总字节数进行循环比较，决定是否继续从服务端接受数据
        recv_data = conn_socket.recv(1024) # 从服务端接受缓存中还未被(开始只接收了'i'格式所占的字节数)接收的字节数据
        recv_total_data += recv_data  # 将每次从服务端循环接受的字节数据拼接到一个变量中
        recv_total_len += len(recv_data)  # 将每次从服务器循环接受的数据的总的字节数累加
    print(len_data[0])
    print(recv_total_data.decode('gbk'))
