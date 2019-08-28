import socketserver


class MyTCpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('开始处理链接请求')
        print(self.server, type(self.server))
        ret = self.server.address_family
        print(ret)


IP_PPRT = ('127.0.0.1', 8888)
server = socketserver.ThreadingTCPServer(IP_PPRT, MyTCpHandler)
server.serve_forever()
