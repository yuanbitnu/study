import socket
import json
import pickle
'''
客户端发送用户名和密码交由服务端进行验证
服务端接受用户传递的数据后读取文件或数据库进行数据校验,并将校验结果返回给客户端
客户端针对服务端返回的数据进行验证登录是否通过
'''

def authentication(tup):
    with open('userInfo', mode='r', encoding='utf-8') as file_stream:
        for line in file_stream:
            userInfo = json.loads(line)  # 将从文件读入内存的字符串反序列化成python对象
            if tup[0] == userInfo['user']:
                if tup[1] == userInfo['pwd']:
                    return 0
                else:
                    return 2
            else:
                return 1


socket_server = socket.socket()

socket_server.bind(('127.0.0.1', 9000))

socket_server.listen(6)

while True:
    new_socke, ipaddr = socket_server.accept()
    while True:
        recv_data = new_socke.recv(1024)
        user_data = pickle.loads(recv_data)  # 将从socket接受的二进制字符串反序列化成python对象
        result = authentication(user_data)
        if result == 0:
            new_socke.send('pass'.encode(encoding='utf-8'))
            # new_socke.close() #  如果客户端已经关闭了socket连接,则服务端不需要再重复关闭
            break
        elif result == 1:
            new_socke.send('用户名错误'.encode(encoding='utf-8'))
            # new_socke.close()
            break
        elif result == 2:
            new_socke.send('密码错误'.encode(encoding='utf-8'))
            # new_socke.close()
            break
