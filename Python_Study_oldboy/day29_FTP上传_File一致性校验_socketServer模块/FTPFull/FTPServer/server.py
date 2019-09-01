import socketserver
import hashlib
import pickle
import struct
import os
import logging
# import subprocess

# {'action':'login','name':'user','password':'pwd'}
# {'action':'send_file',"file_path":'file_path','file_size':'file_size','file_md5_val':'file_md5_val'}
# {'action':'download_file','file_name':'file_name'}
# {'action':'return_code','code':'value'}
# 200:接受/发送 成功  201 校验失败  404 文件不存在 405 重发失败


class ServerHelp():
    _file_suffix = '.dmp'  # 输出到日志的文件后缀
    _logFile_abspath = 'D:\\log.txt'

    @staticmethod
    def get_all_fileAbsPath(path):
        file_lis = []
        if os.path.exists(path):
            while True:
                dir_lis = os.listdir(path)
                for item in dir_lis:
                    full_path = os.path.join(path, item)
                    if os.path.isfile(full_path):
                        file_lis.append(full_path)
                    elif os.path.isdir(full_path):
                        file_lis.extend(
                            ServerHelp.get_all_fileAbsPath(full_path))
                break
        return file_lis

    @staticmethod
    def md5_encry(value, value_type='value'):
        '''
        value_type default is "value",if the first argument is file that value_type will set "file_path"
        '''
        md5_obj = hashlib.md5()
        if value_type == 'value':
            md5_obj.update(value.encode(encoding='utf-8'))
            return md5_obj.hexdigest()
        elif value_type == 'file_path':
            with open(value, mode='rb') as file_stream:
                for line in file_stream:
                    md5_obj.update(line)
                return md5_obj.hexdigest()

    @staticmethod
    def verify(user, pwd, userinfo_all):
        '''
        return 0 为 验证成功；1 为用户名错误；2 为密码错误
        '''
        for item in userinfo_all:
            if user == item['name']:
                if pwd == item['password']:
                    return 0
                else:
                    return 2
            else:
                continue
        return 1
        # while True:
        #     try:
        #         user_dic = userinfo_all.__next__()
        #         if user == user_dic['name']:
        #             if pwd == user_dic['password']:
        #                 return 0
        #             else:
        #                 return 2
        #         else:
        #             continue
        #     except StopIteration:
        #         return 1
        #         break

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
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%m-%Y %H:%M:%S")

        handler_file.setFormatter(formatter)
        handler_stream.setFormatter(formatter)

        logger.addHandler(handler_file)
        logger.addHandler(handler_stream)
        return logger

    @staticmethod
    def get_all_userinfo(userInfo_path):
        userinfo_all = []
        with open(file=userInfo_path, mode='rb') as file_stream:
            while True:
                try:
                    userInfo_dic = pickle.load(file_stream)
                    userinfo_all.append(userInfo_dic)
                except EOFError:
                    break
        return userinfo_all

    @staticmethod
    def regiest(user, pwd, userInfo_path):
        if os.path.getsize(userInfo_path) != 0:

            while True:
                userInfo_all = ServerHelp.get_all_userinfo(
                    userInfo_path)
                for item in userInfo_all:
                    if item['name'] == user:
                        user = input('用户名重复，请重新输入>>>>')
                        continue
                userInfo_dic = {"name": user, "password": pwd}
                userInfo_pickle = pickle.dumps(userInfo_dic)
                with open(userInfo_path, mode='ab') as file_stream:
                    file_stream.write(userInfo_pickle)
                break


class ServerHandler(socketserver.BaseRequestHandler):
    UserInfo_AbsPath = os.path.abspath('userInfo')
    server_mainPath = 'D:\\MyFtpServerPath'
    logger = ServerHelp.get_logger()
    _file_suffix = '.dmp'
    client_num = 0

    def handle(self):
        # userinfo_all = ServerHelp.get_all_userinfo(
        #     ServerHandler.UserInfo_AbsPath)
        ServerHandler.client_num += 1
        ServerHandler.logger.debug(
            '客户机：*%s*--已连接，端口号为：**%s**,当前客户机连接数为%d' % (self.client_address[0], self.client_address[1], ServerHandler.client_num))
        while True:
            try:
                head = self.recive_head()
                # action = head['action']
                if head['action'] == 'login':
                    userinfo_all = ServerHelp.get_all_userinfo(
                        ServerHandler.UserInfo_AbsPath)
                    user = head['name']
                    pwd = head['password']
                    if ServerHelp.verify(user, pwd, userinfo_all) == 0:
                        self.send_head(action='return_code', code='0')
                        self.user_mainpath = os.path.join(
                            ServerHandler.server_mainPath, user)  # login成功后拼接一个以用户名结束的目录名称
                        # # login成功后在server主目录下新建一个user目录
                        if not os.path.exists(self.user_mainpath):
                            os.makedirs(self.user_mainpath)
                        continue
                    elif ServerHelp.verify(user, pwd, userinfo_all) == 1:
                        self.send_head(action='return_code', code='1')
                        continue
                    elif ServerHelp.verify(user, pwd, userinfo_all) == 2:
                        self.send_head(action='return_code', code='2')
                        continue
                elif head['action'] == 'send_file':
                    self.recive_file(head)
                    continue
                elif head['action'] == 'download_file':
                    file_path = head['file_path']
                    file_Abs_path = self.find_file(file_path)
                    if file_Abs_path is None:
                        self.send_head(action='return_code', code='404')
                    else:
                        self.send_file(file_Abs_path)
                    continue
                elif head['action'] == 'return_code':
                    if head['code'] == '200':
                        continue
                    elif head['code'] == '405':
                        continue
                elif head['action'] == 'dir_all_file':
                    self.dir_user_mainpath()
                elif head['action'] == 'exit':
                    self.server.close_request(self.request)
                    ServerHandler.client_num -= 1
                    ServerHandler.logger.debug('客户机：*%s*--正常断开连接,当前客户机连接数为%d' %
                                               (self.client_address[0], ServerHandler.client_num))
                    break
            except Exception:
                ServerHandler.logger.exception('tyb')
                self.server.close_request(self.request)
                ServerHandler.client_num -= 1
                ServerHandler.logger.debug('客户机：*%s*--异常断开连接,当前客户机连接数为%d' %
                                           (self.client_address[0], ServerHandler.client_num))
                break

    def recive_file(self, head):
        file_path = head['file_path']
        file_name = os.path.basename(file_path)
        local_file_path = os.path.join(self.user_mainpath, file_name)
        file_size = head['file_size']
        file_md5_val = head['file_md5_val']
        self.recive_data(local_file_path, file_size, file_md5_val)

    def recive_data(self, file_path, file_size, file_md5_val):
        has_recv_data_len = 0
        with open(file_path, mode='wb') as file_stream:
            while has_recv_data_len < file_size:
                recv_data = self.request.recv(1024)
                file_stream.write(recv_data)
                has_recv_data_len += len(recv_data)
                # print('%s文件总大小为%d，已接受%d' %
                #       (file_path, file_size, has_recv_data_len))
            if has_recv_data_len == file_size:  # and has_recv_data_len == file_size
                self.logger.debug('%s文件接收已完成' % file_path)
        local_file_md5_val = ServerHelp.md5_encry(
            file_path, value_type='file_path')
        if local_file_md5_val == file_md5_val:
            self.logger.debug('%s文件校验已通过' % file_path)
            # print(os.path.abspath(file_path))
            self.send_head(action='return_code', code='200')
            # self.server.close_request(self.request)
            if os.path.splitext(file_path)[1] == self._file_suffix:
                self.logger.info('%s文件正常完成copy' % file_path)
                self.logger.debug('*' * 100)
        else:
            self.logger.debug('%s文件校验失败' % file_path)
            self.logger.debug('*' * 100)
            self.send_head(action='return_code', code='201')
            os.remove(file_path)

    def recive_head(self):
        recv_head_len = self.request.recv(struct.calcsize('i'))  # return byet
        head_len = struct.unpack('i', recv_head_len)

        recv_head = self.request.recv(head_len[0])
        head = pickle.loads(recv_head)
        return head

    def send_head(self, *arg, **args):
        if len(arg) != 0:
            head_pickle = pickle.dumps(arg[0])
            head_pickle_len = len(head_pickle)
            head_byte = struct.pack(
                'i%ds' % head_pickle_len, head_pickle_len, head_pickle)
            self.request.send(head_byte)
        elif len(args) != 0:
            head_dic = {}
            for k, v in args.items():
                head_dic[k] = v
            head_dic_pickle = pickle.dumps(head_dic)
            head_dic_pickle_len = len(head_dic_pickle)
            head_byte = struct.pack(
                'i%ds' % head_dic_pickle_len, head_dic_pickle_len, head_dic_pickle)
            self.request.send(head_byte)

    @classmethod
    def get_all_fileAbsPath(cls, path):
        file_lis = []
        if os.path.exists(path):
            while True:
                dir_lis = os.listdir(path)
                for item in dir_lis:
                    full_path = os.path.join(path, item)
                    if os.path.isfile(full_path):
                        file_lis.append(full_path)
                    elif os.path.isdir(full_path):
                        file_lis.extend(cls.get_all_fileAbsPath(full_path))
                break
        return file_lis

    def send_file_isdir_or_isfile(self, path):
        if os.path.isdir(path):
            all_fileAbsPath_lis = self.get_all_fileAbsPath(path)
            for item in all_fileAbsPath_lis:
                self.send_file(item)
        elif os.path.isfile(path):
            self.send_file(path)

    def send_file(self, file_path):
        times = 0
        while True:
            file_total_size = os.path.getsize(file_path)
            md5_val = ServerHelp.md5_encry(file_path, value_type='file_path')
            self.send_head(action='send_file', file_path=file_path, file_size=file_total_size,
                           file_md5_val=md5_val)
            with open(file_path, mode='rb') as file_stream:
                for line in file_stream:
                    self.request.send(line)
            head = self.recive_head()
            if head['action'] == 'return_code':
                # recv = self.request.recv(1024).decode('gbk')
                if head['code'] == '200':
                    self.send_head(action='return_code', code='200')
                    break
                elif head['code'] == '201':
                    times += 1
                    if times < 6:
                        self.logger.debug('文件**%s**重发 %d 次。' %
                                          (file_path, times))
                        continue
                    else:
                        self.logger.info(
                            '文件**%s**重发次数超过5次，停止发送' % file_path)
                        self.send_head(action='return_code', code='405')
                        break

    def find_file(self, file_path):
        file_base_name = os.path.basename(file_path)
        file_Abs_Path_lis = ServerHelp.get_all_fileAbsPath(self.user_mainpath)
        for item in file_Abs_Path_lis:
            item_base_name = os.path.basename(item)
            if file_base_name == item_base_name:
                return item
        return None

    def dir_user_mainpath(self):
        os.chdir(self.user_mainpath)
        lis_dic = []
        lis = os.listdir()
        for item in lis:
            if os.path.isfile(item):
                lis_dic.append({"file_name": os.path.basename(
                    item), "file_size": os.path.getsize(item)})
        self.send_head(lis_dic)

        # 先更改执行路径
        # subprocess.run(cmd)


socketserver = socketserver.ThreadingTCPServer(
    ("127.0.0.1", 8888), ServerHandler)
socketserver.serve_forever()


# ServerHelp.regiest('admin', 'admin1', 'userInfo')

# user = ServerHelp.get_all_userinfo("userInfo")
# for item in user:
#     print(item)


# def send_head(*arg, **args):
#     if len(arg) != 0:
#         print(arg)
#         head_pickle = pickle.dumps(arg)
#         head_pickle_len = len(head_pickle)
#         head_byte = struct.pack(
#             'i%ds' % head_pickle_len, head_pickle_len, head_pickle)
#         # self.request.send(head_byte)
#     elif len(args) != 0:
#         print(args)
#         head_dic = {}
#         for k, v in args.items():
#             head_dic[k] = v
#         head_dic_pickle = pickle.dumps(head_dic)
#         head_dic_pickle_len = len(head_dic_pickle)
#         head_byte = struct.pack(
#             'i%ds' % head_dic_pickle_len, head_dic_pickle_len, head_dic_pickle)
#         # self.request.send(head_byte)


# send_head([1, 2, 3])
