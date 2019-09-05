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
        '''get_all_fileAbsPath 通过递归获取path路径下的所有文件的绝对路径，并追加入一个列表中
        
        Arguments:
            path {str} -- 文件夹路径
        
        Returns:
            list -- path路径下所有文件的绝对路径列表
        '''
        file_lis = []
        if os.path.exists(path): #判断path路径是否存在
            while True:
                dir_lis = os.listdir(path) # get path 路径下的所有文件和文件夹的相对path的相对路径
                for item in dir_lis:
                    full_path = os.path.join(path, item) # 将拼接成绝对路径
                    if os.path.isfile(full_path):  #判断是否是文件，是文件则直接加入file_lis列表中，是文件夹则递归调用本方法
                        file_lis.append(full_path)
                    elif os.path.isdir(full_path):
                        file_lis.extend(
                            ServerHelp.get_all_fileAbsPath(full_path)) #递归返回的结果必须要用一个全局变量进行接s收(接收所有递归的结果)
                break
        return file_lis

    @staticmethod
    def md5_encry(value, value_type='value'):
        '''md5_encry 返回value的MD5哈希值
        
        Arguments:
            value {str or obj} -- 需要计算MD5值的对象
        
        Keyword Arguments:
            value_type {str} -- value or file_path--如果是值或者对象则默认参数，如果是file则需设置为file_path (default: {'value'})
        
        Returns:
            str -- 返回计算后的MD5值
        '''
        md5_obj = hashlib.md5() # 创建一个MD5对象
        if value_type == 'value': # 判断需要加密的对象是值还是文件
            md5_obj.update(value.encode(encoding='utf-8')) # update传入的参数必须是byte
            return md5_obj.hexdigest()
        elif value_type == 'file_path':
            with open(value, mode='rb') as file_stream: #直接打开文件读取byte字节
                for line in file_stream:
                    md5_obj.update(line) #分部分计算相当于一次性计算文件的MD5
                return md5_obj.hexdigest()

    @staticmethod
    def verify(user, pwd, userinfo_path):
        '''verify 将user和pwd 与userinfo_all列表中的userinfo进行对比验证
        
        Arguments:
            user {str} -- 用户名
            pwd {str} -- 密码
            userinfo_all {list} -- 用户(字典)列表
        
        Returns:
            integer -- 返回代码 0-验证通过 | 1-用户名错误 | 2-密码错误
        '''
        userinfo_all = ServerHelp.__get_all_userinfo(userinfo_path)
        for item in userinfo_all:
            if user == item['name']:
                if pwd == item['password']:
                    return 0
                else:
                    return 2
            else:
                continue
        return 1


    @classmethod
    def get_logger(cls):
        '''get_logger 创建并配置一个logger对象
        
        Returns:
            logger -- 经过配置的logger对象
        '''
        logger = logging.getLogger("tyb") # 为日志文件写入用户

        handler_file = logging.FileHandler(
            cls._logFile_abspath, mode='a+', encoding="utf-8") # 创建一个文件处理对象，将日志写入文件
        handler_stream = logging.StreamHandler() # 创建一个流处理对象，将日志写入流

        logger.setLevel(logging.DEBUG) # 设置logger允许写入最低日志级别 (该级别为当前logger能写入的起始级别，不管其他handler设置哪种级别，该logger只能写入Debug级别(含Debug)以上级别的日志)
        handler_file.setLevel(logging.INFO) #设置文件处理器能写入的最低日志级别
        handler_stream.setLevel(logging.DEBUG) #设置流处理器能写入的最低日志级别

        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(levelname)s %(message)s", datefmt="%d-%m-%Y %H:%M:%S") # 创建一个Formatter格式化器对象，并对其进行格式(日志表现出来的格式)初始化

        handler_file.setFormatter(formatter) #为两个handler处理器设置Formatter格式化器
        handler_stream.setFormatter(formatter)

        logger.addHandler(handler_file) # 将两个handler处理器加入logger
        logger.addHandler(handler_stream)
        return logger

    @staticmethod
    def __get_all_userinfo(userinfo_Abspath):
        '''__get_all_userinfo 获取指定用户文件中所有用户信息，组成字典后加入一个列表
        
        Arguments:
            userInfo_path {str} -- 存储用户文件的绝对路径
        
        Returns:
            [list] -- 用户字典列表
        '''
        userinfo_all = []
        with open(file=userinfo_Abspath, mode='rb') as file_stream:
            while True:
                try:
                    userInfo_dic = pickle.load(file_stream) # 使用pickle模块序列化为byte
                    userinfo_all.append(userInfo_dic)
                except EOFError:
                    break
        return userinfo_all

    @staticmethod
    def regiest(user, pwd, userinfo_Abspath):
        '''regiest 注册用户
        
        Arguments:
            user {str} -- 用户名
            pwd {str} -- 密码
            userinfo_path {str} -- 用户信息文件绝对路径
        '''
        if os.path.getsize(userinfo_Abspath) != 0: # 判断用户文件是否为空
            while True:
                userInfo_dic_all = ServerHelp.__get_all_userinfo(
                    userinfo_Abspath) #获取所有用户信息(字典)
                for item in userInfo_dic_all:
                    if item['name'] == user:
                        user = input('用户名重复，请重新输入>>>>')
                        continue #如果用户名重复则重新输入用户名，并继续循环判断
                userInfo_dic = {"name": user, "password": pwd} #如果没有重复用户名，则新构建一个用户字典信息
                userInfo_pickle = pickle.dumps(userInfo_dic) #序列化该用户信息
                with open(userinfo_Abspath, mode='ab') as file_stream:
                    file_stream.write(userInfo_pickle) #将序列化后的内容追加入用户信息文件
                break


class ServerHandler(socketserver.BaseRequestHandler):
    UserInfo_AbsPath = os.path.abspath('userInfo') # 用户信息文件的绝对路径
    server_mainPath = 'D:\\MyFtpServerPath' # Ftp服务端主目录
    logger = ServerHelp.get_logger() #创建一个logger对象
    _file_suffix = '.dmp' # 需要写入日志的文件后缀
    client_num = 0 # 连接的客户端数量

    def handle(self):
        ServerHandler.client_num += 1
        ServerHandler.logger.debug(
            '客户机：*%s*--已连接，端口号为：**%s**,当前客户机连接数为%d' % (self.client_address[0], self.client_address[1], ServerHandler.client_num))
        while True:
            try:
                head = self.recive_head() # 接收客户端head信息

                # 通过 head['action'] 值判断该执行的操作
                if head['action'] == 'login':  # 执行登陆验证操作
                    user = head['name']
                    pwd = head['password']
                    if ServerHelp.verify(user, pwd, ServerHandler.UserInfo_AbsPath) == 0: #login成功

                        self.send_head(action='return_code', code='0') #向客户端发送head信息，表示用户验证通过
                        self.user_mainpath = os.path.join(
                            ServerHandler.server_mainPath, user)  # login成功后拼接一个以用户名结束的目录名称
                        if not os.path.exists(self.user_mainpath):
                            os.makedirs(self.user_mainpath) # 如果用户主目录不存在则创建一个(第一次登陆肯定不存在用户目录)
                        continue
                    elif ServerHelp.verify(user, pwd, ServerHandler.UserInfo_AbsPath) == 1: # login不成功
                        self.send_head(action='return_code', code='1') #向客户端发送head信息，表示用户名错误
                        continue
                    elif ServerHelp.verify(user, pwd, ServerHandler.UserInfo_AbsPath) == 2: #login 不成功
                        self.send_head(action='return_code', code='2') # 向客户端发送head信息，表示密码错误
                        continue
                elif head['action'] == 'send_file': # 表示客户端要发送文件
                    self.recive_file(head) # 服务端接收文件
                    continue
                elif head['action'] == 'download_file': # 表示客户端要下载文件
                    file_path = head['file_path'] # 查看接收head中客户端需要下载的文件名
                    file_Abs_path = self.find_file(file_path) # 获取该文件的绝对路径
                    if file_Abs_path is None: #如果该文件不存在，则发送表示文件不存在的head头
                        self.send_head(action='return_code', code='404')
                    else:
                        self.send_file(file_Abs_path) #发送文件
                    continue
                elif head['action'] == 'return_code': #表示客户端返回的code代码
                    if head['code'] == '200': # 表示客户端文件接收成功
                        continue
                    elif head['code'] == '405': # 表示客户端重发了多次次都失败
                        continue
                elif head['action'] == 'dir_all_file': # 表示客户端需要查看FTP服务器中该用户目录下的所有文件
                    self.dir_user_mainpath()  #向客户端发送用户目录下的文件信息
                elif head['action'] == 'exit': # 表示客户端要断开连接
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
        file_size = head['file_size']
        file_md5_val = head['file_md5_val']
        last_dir = head['last_dir']
        local_file_Abspath = os.path.join(self.user_mainpath, last_dir)
        local_file_dir = os.path.dirname(local_file_Abspath)
        if not os.path.exists(local_file_dir):
            os.makedirs(local_file_dir)

        has_recv_data_len = 0
        with open(local_file_Abspath, mode='wb') as file_stream:
            while has_recv_data_len < file_size:
                recv_data = self.request.recv(1024)
                file_stream.write(recv_data)
                has_recv_data_len += len(recv_data)
                # print('%s文件总大小为%d，已接受%d' %
                #       (local_file_Abspath, file_size, has_recv_data_len))
            if has_recv_data_len == file_size:  # and has_recv_data_len == file_size
                self.logger.debug('%s文件接收已完成' % local_file_Abspath)
        local_file_md5_val = ServerHelp.md5_encry(
            local_file_Abspath, value_type='file_path')
        if local_file_md5_val == file_md5_val:
            self.logger.debug('%s文件校验已通过' % local_file_Abspath)
            # print(os.path.abspath(local_file_Abspath))
            self.send_head(action='return_code', code='200')
            # self.server.close_request(self.request)
            if os.path.splitext(local_file_Abspath)[1] == self._file_suffix:
                self.logger.info('%s文件正常完成copy' % local_file_Abspath)
                self.logger.debug('*' * 100)
        else:
            self.logger.debug('%s文件校验失败' % local_file_Abspath)
            self.logger.debug('*' * 100)
            self.send_head(action='return_code', code='201')
            os.remove(local_file_Abspath)

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
