import socket
import pickle


def login(tup):
    socket_client = socket.socket()
    socket_client.connect(('127.0.0.1', 9000))
    data = pickle.dumps(tup)  # 将元祖序列化成byte字节
    socket_client.send(data)  # 将上面字节通过socket发送给服务器
    recv_data = socket_client.recv(1024).decode(
        encoding='utf-8')  # 将接收的byte字节使用"utf-8"编码
    if recv_data == 'pass':
        socket_client.close()  # 接收到服务端的返回数据后,关闭和服务器的连接(客户端和服务端只要有一端关闭了socket连接就行)
        return True
    else:
        socket_client.close()
        return False


user = input('请输入用户名>>>')
password = input('请输入密码>>>')
data = (user, password)
if login(data):
    print('%s欢迎进入系统' % data[0])
else:
    print('验证失败,请重新输入')
