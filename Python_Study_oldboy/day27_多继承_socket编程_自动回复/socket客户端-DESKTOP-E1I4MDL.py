import socket

socket_client = socket.socket()

socket_client.connect(('127.0.0.1', 9000))

socket_client.send('你好'.encode('utf-8'))
