import socket

socket_client = socket.socket()

socket_client.connect(('127.0.0.1', 10000))

while True:
    data = input('>>>')
    if data != 'exit':
        socket_client.send(data.encode(encoding='utf-8'))
        recv_data = socket_client.recv(1024).decode(encoding='utf-8')
        print(recv_data)
    else:
        socket_client.close()
        break
