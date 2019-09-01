import sys
import os
import pickle
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib import general


def regist(user, pwd):
    user_info_path = general.get_user_info_path()
    last_id = get_last_id()
    with open(user_info_path, mode='ab') as file_stream_ab:
        if check_unique_user(user):
            dic = {'id': last_id + 1, 'user': user, 'pwd': pwd}
            pickle_ret = pickle.dump(dic, file_stream_ab)
            return True
        else:
            result = False


def check_unique_user(user):
    user_info_path = general.get_user_info_path()
    user_lis = []
    with open(user_info_path, mode='rb') as file_stream_rb:
        while True:
            try:
                ret = pickle.load(file_stream_rb)
                user_lis.append(ret['user'])
            except EOFError:
                break
    if user in user_lis:
        return False
    else:
        return True


def get_last_id():
    user_info_path = general.get_user_info_path()
    ret = None
    with open(user_info_path, mode='rb') as file_stream_rb:
        while True:
            try:
                ret = pickle.load(file_stream_rb)
            except EOFError:
                if ret is None:
                    return 0
                else:
                    return ret['id']


def login(user, pwd):
    user_info_path = general.get_user_info_path()
    ret = None
    with open(user_info_path, mode='rb') as file_stream_rb:
        while True:
            try:
                ret = pickle.load(file_stream_rb)
                if user == ret['user'] and pwd == ret['pwd']:
                    return True
                else:
                    False
            except EOFError:
                return False


if __name__ == '__main__':
    # regist('www1', 'www1')
    # print(get_last_id())
    # print(check_unique_user('www1'))
    print(login('www', 'www1'))
