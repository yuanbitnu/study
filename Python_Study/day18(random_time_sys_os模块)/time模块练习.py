import time
# 1.查看一下2000000000时间戳表示的年月日(时间戳时间转格式化时间)
# struct_time = time.localtime(2000000000)
# format_time = time.strftime('%Y-%m-%d %H:%M:%S', struct_time)
# print(format_time)

# # 2.将2008-8-8转为时间戳时间
# struct_time = time.strptime("2008-8-8", '%Y-%m-%d')
# stamp_time = time.mktime(struct_time)
# print(stamp_time)

# 3.定义一个函数,取出某月1号的时间戳时间

# now_struct_time = time.localtime()  # 获取当前结构化时间

# struct_time = time.strptime(
#     '%s-%s-1' % (now_struct_time.tm_year, now_struct_time.tm_mon), '%Y-%m-%d')  # 通过上条语句结果获得当前具体的年、月，以便组成指定条件的格式化时间，并将其转为结构化时间


# stamp_time = time.mktime(struct_time)  # 将结构化时间转为时间戳时间

# print(stamp_time)


# 4.计算2018-8-19 22:10:08  2018-8-20 11:07:03的时间差(经过了多少时多少分多少秒)

struct_time_one = time.strptime('2018-8-19 22:10:08', '%Y-%m-%d %H:%M:%S')

struct_time_two = time.strptime('2018-8-23 23:10:08', '%Y-%m-%d %H:%M:%S')

sub_time = time.mktime(struct_time_two) - time.mktime(struct_time_one)

st = time.gmtime(sub_time) #gmtime()获取伦敦时间

print('时间过去了%s月%s天%s时%s分%s秒' %
      (st.tm_mon - 1, st.tm_mday - 1, st.tm_hour, st.tm_min, st.tm_sec))

# lis_one = []
# for i  j in struct_time_one,struct_time_two:
