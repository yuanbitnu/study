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


socket_server = socket.socket()
socket_server.bind(('127.0.0.1', 9000))
socket_server.listen(5)
new_socket, ipadd = socket_server.accept()

logger.debug(str(ipadd))

rec_data = new_socket.recv(1024).decode(encoding='utf-8')
logger.debug(rec_data)
new_socket.close()
socket_server.close()
