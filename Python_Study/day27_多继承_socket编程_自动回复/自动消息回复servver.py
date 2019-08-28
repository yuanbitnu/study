import socket
import logging

logger = logging.getLogger("tyb")

handler = logging.FileHandler('log.txt', mode='a', encoding="utf-8")

logger.setLevel(logging.DEBUG)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%M-%Y %H:%M:%S")

handler.setFormatter(formatter)

logger.addHandler(handler)


socket_server = socket.socket()
socket_server.bind(('127.0.0.1', 10000))
socket_server.listen(5)

while True:
    new_socekt, ipaddr = socket_server.accept()
    # if new_socekt is not None:
    logger.debug('主机:%s通过端口号:%s连接' % (ipaddr[0], ipaddr[1]))
    while True:
        try:
            recv_data = new_socekt.recv(1024).decode(encoding='utf-8')
            if '你好' in recv_data:
                new_socekt.send('您好，有什么需要帮助？'.encode(encoding='utf-8'))
            elif '快递' in recv_data:
                new_socekt.send('快递单号是多少？'.encode(encoding='utf-8'))
            elif 'exit' in recv_data:
                new_socekt.close()
                break
            else:
                new_socekt.send('不清楚，请您再说一次'.encode(encoding='utf-8'))
        except Exception as e:
            break
