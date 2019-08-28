import socket
import logging

logger = logging.getLogger('tyb')

handler = logging.StreamHandler()

logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)

formatter_one = logging.Formatter(
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%M-%Y %H:%M:%S")

handler.setFormatter(formatter_one)

logger.addHandler(handler)

#  1.创建一个socket对象，开启socket服务
socket_server = socket.socket()

#  2.为socket对象绑定IP地址和端口号
socket_server.bind(('127.0.0.1', 9000))

#  3.开启socket监听，参数为可排队客户端数量
socket_server.listen(5)

#  4.等待接受socket客户端的连接，连接成功则返回一个和该客户端进行通信的socket对象(该方法会阻塞程序以等待客户端的连接)
new_socket, ipadd = socket_server.accept()
logger.debug(str(ipadd))

#  5.通过通信socket对象和客户端进行数据通信(接受或发送数据，接受和发送的数据都是字符)
rec_data = new_socket.recv(1024).decode(encoding='utf-8')
new_socket.send('我很好！！'.encode('utf-8'))
logger.debug(rec_data)

#  6.关闭负责通信的socket
new_socket.close()

#  7.关闭整个socket服务
socket_server.close()
