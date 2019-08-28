import socketserver
import hashlib
import logging
import struct
import pickle
import os


class Server_handler(socketserver.BaseRequestHandler):

    _file_suffix = '.dmp'  # 输出到日志的文件后缀
    _logFile_abspath = 'D:\\log.txt'

    def handle(self):
        logger = self.get_logger()
        while True:
            try:
                logger.debug('%s:主机连接成功，开始传送>>>' %
                             self.server.server_address[0])
                while True:
                    rec_fileInfo_len = self.request.recv(
                        struct.calcsize('i'))  # return byet
                    fileInfo_len = struct.unpack('i', rec_fileInfo_len)

                    rec_fileInfo_dic = self.request.recv(fileInfo_len[0])
                    fileInfo_dic = pickle.loads(rec_fileInfo_dic)

                    file_name = fileInfo_dic['file_name']
                    file_size = fileInfo_dic['file_size']
                    file_md5_val = fileInfo_dic['file_md5_val']

                    if not os.path.exists(os.path.dirname(file_name)):
                        os.makedirs(os.path.dirname(file_name))
                        has_recv_data_len = 0
                        with open(file_name, mode='wb') as file_stream:
                            while has_recv_data_len < file_size:
                                recv_data = self.request.recv(1024)
                                file_stream.write(recv_data)
                                has_recv_data_len += len(recv_data)
                                # print('%s文件总大小为%d，已接受%d' %
                                #       (file_name, file_size, has_recv_data_len))
                            if has_recv_data_len == file_size:  # and has_recv_data_len == file_size
                                logger.debug('%s文件接收已完成' % file_name)
                        local_file_md5_val = self.md5_opration(file_name)
                        if local_file_md5_val == file_md5_val:
                            logger.debug('%s文件校验已通过' % file_name)
                            # print(os.path.abspath(file_name))
                            self.request.send(b'200')
                            self.server.close_request(self.request)
                            if os.path.splitext(file_name)[1] == self._file_suffix:
                                logger.info('%s文件正常完成copy' % file_name)
                                logger.debug('*' * 100)
                            break
                        else:
                            logger.debug('%s文件校验失败' % file_name)
                            logger.debug('*' * 100)
                            self.request.send(b'201')
                            os.remove(file_name)
                            continue
                    else:
                        has_recv_data_len = 0
                        with open(file_name, mode='wb') as file_stream:
                            while has_recv_data_len < file_size:
                                recv_data = self.request.recv(1024)
                                file_stream.write(recv_data)
                                has_recv_data_len += len(recv_data)
                                # print('%s文件总大小为%d，已接受%d' %
                                #       (file_name, file_size, has_recv_data_len))
                            if has_recv_data_len == file_size:
                                logger.debug('%s文件接收已完成' % file_name)
                        local_file_md5_val = self.md5_opration(file_name)

                        if local_file_md5_val == file_md5_val:
                            logger.debug('%s文件校验已通过' % file_name)
                            logger.debug('*' * 40)
                            self.request.send(b'200')
                            self.server.close_request(self.request)
                            if os.path.splitext(file_name)[1] == self._file_suffix:
                                logger.info('%s文件正常完成copy' % file_name)
                                logger.debug('*' * 100)
                            break
                        else:
                            logger.debug('%s文件校验失败' % file_name)
                            logger.debug('*' * 100)
                            self.request.send(b'201')
                            os.remove(file_name)
                            continue

                    # while True:
                    #     with open('444.jpg', mode='ab') as file_stream:
                    #         while True:
                    #             rec_data_len = conn_socket.recv(
                    #                 struct.calcsize('i'))  # return byet
                    #             data_len = struct.unpack('i', rec_data_len)
                    #             print(data_len[0])
                    #             recv_data = conn_socket.recv(data_len[0])
                    #             file_stream.write(recv_data)

            except Exception:
                logger.exception('连接异常')
                break

    @staticmethod
    def md5_opration(file_name):
        md5_obj = hashlib.md5()
        with open(file_name, mode='rb') as file_stream:
            for line in file_stream:
                md5_obj.update(line)
            return md5_obj.hexdigest()

    @classmethod
    def get_logger(cls):
        logger = logging.getLogger("tyb")

        handler_file = logging.FileHandler(
            cls._logFile_abspath, mode='a+', encoding="utf-8")
        handler_stream = logging.StreamHandler()

        logger.setLevel(logging.DEBUG)
        handler_file.setLevel(logging.INFO)
        handler_stream.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%M-%Y %H:%M:%S")

        handler_file.setFormatter(formatter)
        handler_stream.setFormatter(formatter)

        logger.addHandler(handler_file)
        logger.addHandler(handler_stream)
        return logger


IP_PPRT = ('127.0.0.1', 8888)
server = socketserver.ThreadingTCPServer(IP_PPRT, Server_handler)
server.serve_forever()
