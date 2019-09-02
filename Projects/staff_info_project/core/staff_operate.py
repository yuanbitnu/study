import sys
import os
# sys.path.append(
#     r'C:\Users\17711\OneDrive\PythonCode\Projects\staff_info_project')
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# sys.path.append(
#     r'H:\BaiduNetdiskDownload\OneDrive\PythonCode\Projects\staff_info_project')
from lib import general


def update_staff(*staff):
    staff_info_path = general.get_staff_info_path()
    with open(staff_info_path, mode='a+', encoding='utf-8') as file_stream:
        name, age, phone, job = staff
        age = str(age)
        file_stream.seek(0)
        lines = file_stream.readlines()
        # print(lines)
        last_line = lines[len(lines) - 1]
        items = last_line.split(',')
        last_num = items[0].strip()
        new_staff_tuple = (str(int(last_num) + 1), name, age, phone, job)
        new_staff = ','.join(new_staff_tuple)
        file_stream.write('\n' + new_staff)


def delete_staff(num):
    staff_info_path = general.get_staff_info_path()
    new_staff_info_path = os.path.join(
        os.path.dirname(staff_info_path), 'staff_info_copy')
    # new_staff_info_path = os.path.dirname(staff_info_path) + 'staff_info_copy'
    with open(staff_info_path, mode='r', encoding='utf-8') as file_stream_r,\
            open(new_staff_info_path, mode='a', encoding='utf-8') as file_stream_a:
        for line in file_stream_r:
            items = line.strip().split(',')
            if items[0] != str(num) and items[0] != '':
                file_stream_a.write(line)
    os.remove(staff_info_path)
    os.rename(new_staff_info_path, staff_info_path)


def select_staff(str_):
    staff_info_path = general.get_staff_info_path()
    with open(staff_info_path, mode='r', encoding='utf-8') as file_stream_r:
        first_line = file_stream_r.readline().strip()
        items = first_line.split(',')  # 第一行key数组
        # print(items)
        str_split = str_.strip().split('where')
        # print(str_split[1].strip().split('='))
        where_index = []  # where语句中key的index
        # print(where_index, id(where_index))
        where_value = ''  # where 语句中key的value
        # print(where_value, id(where_value))
        select_index_list = []
        # print(select_index_list, id(select_index_list))
        where_exp = ''
        # print(where_exp)
        # 对where表达式的key和值进行筛选判断
        if len(str_split[1].strip().split('=')) > 1:
            where_exp = '='
            where_items = str_split[1].strip().split('=')
            # print(where_items)
            where_key = where_items[0].strip()
            # print(where_key)
            # print(items.index(where_key))
            where_index.append(items.index(where_key))
            where_value = where_items[1].strip()
            # print(where_value, id(where_value))
        elif len(str_split[1].strip().split('>')) > 1:
            where_exp = '>'
            where_items = str_split[1].strip().split('>')
            where_key = where_items[0].strip()
            where_index.append(items.index(where_key))
            where_value = where_items[1].strip()
        elif len(str_split[1].strip().split('<')) > 1:
            where_exp = '<'
            where_items = str_split[1].strip().split('<')
            where_key = where_items[0].strip()
            where_index.append(items.index(where_key))
            where_value = where_items[1].strip()
        elif len(str_split[1].strip().split('like')) > 1:
            where_exp = 'like'
            where_items = str_split[1].strip().split('like')
            where_key = where_items[0].strip()
            where_index.append(items.index(where_key))
            where_value = where_items[1].strip()

        # 对select项进行筛选
        if str_split[0].replace('select', '').strip() == '*':  # 显示所有项
            select_index_list = list(range(0, len(items)))
        elif len(str_split[0].replace('select', '').strip().split(',')) > 0:  # 具体项显示
            selects = str_split[0].replace('select', '').strip().split(',')
            for item in selects:
                index = items.index(item.strip())
                select_index_list.append(index)

        # 打印处理
        lines = file_stream_r.readlines()  # 函数开始调用了一次readline,因此此处从第二行作为光标的起始开始读取
        if where_exp == "=":
            for index in range(0, len(lines)):
                content_items = lines[index].strip().split(',')
                # print(content_items)
                if content_items[where_index[0]].strip() == where_value:
                    select_lis_print = []
                    for select_item in select_index_list:
                        select_lis_print.append(content_items[select_item])
                    print(select_lis_print)
        elif where_exp == 'like':
            for index in range(0, len(lines)):
                content_items = lines[index].strip().split(',')
                # print(content_items)
                if content_items[where_index[0]].strip() == where_value:
                    select_lis_print = []
                    for select_item in select_index_list:
                        select_lis_print.append(content_items[select_item])
                    print(select_lis_print)
        elif where_index[0] in [0, 2] and (where_exp == '>' or where_exp == '<'):
            for index in range(0, len(lines)):
                content_items = lines[index].strip().split(',')
                full_where_exp = str_split[1].strip()
                real_where_exp = full_where_exp.replace(
                    items[where_index[0]], content_items[where_index[0]].strip())
                if eval(real_where_exp):
                    select_lis_print = []
                    for select_item in select_index_list:
                        select_lis_print.append(content_items[select_item])
                    print(select_lis_print)


def set_staff(str_):
    staff_info_path = general.get_staff_info_path()
    new_staff_info_path = os.path.join(
        os.path.dirname(staff_info_path), 'staff_info_copy')
    with open(staff_info_path, mode='r', encoding='utf-8') as file_stream_r,\
            open(new_staff_info_path, mode='a+', encoding='utf-8') as file_stream_a:
        first_line = file_stream_r.readline().strip()
        first_line_items = first_line.split(',')
        print(first_line_items)
        str_split = str_.strip().split('where')
        where_key_index = []
        where_value = ''
        set_key_index = []
        set_value = ''
        where_exp = ''
        if len(str_split[1].strip().split('=')) > 1:
            where_exp = '='
            where_items = str_split[1].strip().split('=')
            # print(where_items)
            where_key = where_items[0].strip()
            # print(where_key)
            # print(items.index(where_key))
            where_key_index.append(first_line_items.index(where_key))
            where_value = where_items[1].strip()
            # print(where_value, id(where_value))
        elif len(str_split[1].strip().split('>')) > 1:
            where_exp = '>'
            where_items = str_split[1].strip().split('>')
            where_key = where_items[0].strip()
            where_key_index.append(first_line_items.index(where_key))
            where_value = where_items[1].strip()
        elif len(str_split[1].strip().split('<')) > 1:
            where_exp = '<'
            where_items = str_split[1].strip().split('<')
            where_key = where_items[0].strip()
            where_key_index.append(first_line_items.index(where_key))
            where_value = where_items[1].strip()
        elif len(str_split[1].strip().split('like')) > 1:
            where_exp = 'like'
            where_items = str_split[1].strip().split('like')
            where_key = where_items[0].strip()
            where_key_index.append(first_line_items.index(where_key))
            where_value = where_items[1].strip()

        # 对set项的key value进行筛选
        if len(str_split[0].replace('set', '').strip().split('=')) > 0:  # 具体项显示
            sets = str_split[0].replace('set', '').strip().split('=')
            set_key = sets[0].strip()
            set_key_index.append(first_line_items.index(set_key))
            set_value = sets[1].strip()

        # set处理
        lines = file_stream_r.readlines()  # 函数开始调用了一次readline,因此此处从第二行作为光标的起始开始读取
        file_stream_a.write(first_line + '\n')
        if where_exp == "=":
            for index in range(0, len(lines)):
                content_items = lines[index].strip().split(',')
                # print(content_items)
                if content_items[where_key_index[0]].strip() != where_value:
                    file_stream_a.write(lines[index])
                else:
                    content_items[set_key_index[0]] = set_value
                    new_set_line = ','.join(content_items)
                    file_stream_a.write(new_set_line + '\n')

        # elif where_exp == 'like':
        #     for index in range(0, len(lines)):
        #         content_items = lines[index].strip().split(',')
        #         # print(content_items)
        #         if content_items[where_index[0]].strip() == where_value:
        #             select_lis_print = []
        #             for select_item in select_index_list:
        #                 select_lis_print.append(content_items[select_item])
        #             print(select_lis_print)
        elif where_key_index[0] in [0, 2] and (where_exp == '>' or where_exp == '<'):
            for index in range(0, len(lines)):
                content_items = lines[index].strip().split(',')
                full_where_exp = str_split[1].strip()
                real_where_exp = full_where_exp.replace(
                    first_line_items[where_key_index[0]], content_items[where_key_index[0]].strip())
                if eval(real_where_exp):
                    content_items[set_key_index[0]] = set_value
                    new_set_line = ','.join(content_items)
                    file_stream_a.write(new_set_line + '\n')
                else:
                    file_stream_a.write(lines[index])
    os.remove(staff_info_path)
    os.rename(new_staff_info_path, staff_info_path)


def display_staff():
    staff_info_path = general.get_staff_info_path()
    with open(staff_info_path, mode='r', encoding='utf-8') as file_stream_r:
        file_stream_r.readline()
        for line in file_stream_r:
            print(line)


if __name__ == "__main__":
    # update_staff('Wang',54,'15523112524','Worker')
    # delete_staff(6)
    # select_staff('select phone where age < 23')
    # set_staff('set age = 31 where name = thfo')
    display_staff()
