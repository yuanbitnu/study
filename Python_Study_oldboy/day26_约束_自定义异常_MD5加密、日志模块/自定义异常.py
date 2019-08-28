
import os

# 处理异常错误的方式一,认为构建返回


def open_file(path, prve):
    response = {'code': 1000, 'err_message': '正常'}
    try:
        if not os.path.exists(path):
            response['code'] = 1001
            response['err_message'] = '路径不存在'
            return response
        if not prve:
            response['code'] = 1002
            response['err_message'] = '前缀不存在'
            return response
    except Exception:
        response['code'] = 1003
        response['err_message'] = '未知错误'
        return response


# 处理异常错误的方式二，自定义异常，通过抓取相应异常并进行相应处理
class PathExistsError(Exception):   # 自定义一个路径不存在的异常类
    def __init__(self, code, err_message):  # 自定义该异常所需要传递的异常信息
        self._code = code
        self._err_message = err_message

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def err_message(self):
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        self._err_message = err_message


class PrveError(Exception):   # 自定义一个前缀不存在的异常类
    def __init__(self, code, err_message):  # 自定义该异常所需要传递的异常信息
        self._code = code
        self._err_message = err_message

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def err_message(self):
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        self._err_message = err_message


def new_open_file(path, prve):
    try:
        if not os.path.exists(path):
            raise PathExistsError(1001, '文件不存在')
        if not prve:
            raise PrveError(1002, '前缀不存在')
    except PathExistsError as e:
        return {e.code: e.err_message}
    except PrveError as e:
        return {e.code: e.err_message}
    except Exception:
        return {1003: '未知异常'}


ret = new_open_file('111.txt', None)
print(ret)  # resutl = {1001: '文件不存在'}


ret2 = new_open_file('约束.py', None)
print(ret2)  # resutl = {1002: '前缀不存在'}
