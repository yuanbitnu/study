import os


def file_recursive(path, n):
    dir_list = os.listdir(path)
    # print(dir_list)
    for item in dir_list:
        file_path = os.path.join(path, item)
        if os.path.isdir(file_path):
            print('\t' * n, item)
            file_recursive(file_path, n + 1)
        else:
            print('\t' * n, item)


file_recursive('G:\\老男孩python全栈开发15期\\1-40\\day16', 0)
