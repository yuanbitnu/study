import socket

client = socket.socket()
client.connect(('127.0.0.1', 8888))
client.recv(1024)
