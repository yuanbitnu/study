import socket

#  1.创建一个socket对象，开启socket服务
socket_client = socket.socket()

#  2.向指定的服务端socket对象发去连接
socket_client.connect(('127.0.0.1', 9000))

#  3.和服务端的通信socket进行通信，（发送或接受数据，数据必须是字符形式)
socket_client.send('你好'.encode('utf-8'))
data_recv = socket_client.recv(1024).decode(encoding='utf-8')
print(data_recv)
