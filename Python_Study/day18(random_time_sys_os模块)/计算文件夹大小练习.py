import os

# 文件夹遍历递归版


def fn(path):
    size_count = 0
    lis_dir = os.listdir(path)
    for item in lis_dir:
        abs_path = os.path.join(path, item)
        if os.path.isdir(abs_path):
            # print("\t" * n, abs_path)
            size = fn(abs_path)
            size_count += size
        else:
            # print("\t" * n, abs_path)
            size_count += os.path.getsize(abs_path)
    return size_count


# ret = fn('H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发\\')
# print(ret)

# 文件夹遍历递归版


def fn1(path, n):
    while True:
        lis_dir = os.listdir(path)
        for item in lis_dir:
            abs_path = os.path.join(path, item)
            if os.path.isdir(abs_path):
                print("\t" * n, abs_path)
                fn1(abs_path, n + 1)
            else:
                print("\t" * n, abs_path)
        break


# fn1('H:\\BaiduNetdiskDownload\\OneDrive\\PythonCode\\老男孩Python全栈开发\\', 0)


# 文件夹遍历循环班

def fn2(path_):
    lis = [path_]
    while lis:
        path_inner = lis.pop()
        lis_inner = os.listdir(path_inner)
        for item in lis_inner:
            abs_path = os.path.join(path_inner, item)
            if os.path.isfile(abs_path):
                print(abs_path)
            else:
                lis.append(abs_path)


# abs_path = os.path.abspath('计算文件夹大小练习.py')
# print(abs_path)
# dir_name = os.path.dirname(abs_path)
# print(dir_name)
# last_dir = os.path.split(dir_name)[0]
# print(last_dir)
# fn2(last_dir)
