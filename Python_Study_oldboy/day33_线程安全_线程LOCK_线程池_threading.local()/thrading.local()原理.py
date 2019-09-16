import time
import threading

##一、简单原理

# loacl = {}  #{thread_id:{'num':arg}}  ##{22364: {'num': 1}, 9600: {'num': 2}, 20788: {'num': 3}, 904: {'num': 4}}
# lock = threading.RLock()

# def fun(arg):
#     with lock:
#         thread_id = threading.get_ident()  ## 内部通过使用每个线程ID做Key,其他属性和值组成一个dict做值,实现为每个线程thread单独存储
#         loacl[thread_id] = {}
#         loacl[thread_id]['num'] = arg
#         print(loacl[thread_id]['num'],arg)

# for i in range(1,11):
#     thread = threading.Thread(target=fun,args=(i,))
#     thread.start()

# print(loacl)


##二、真正原理

INFO_DIC = {}
class Local():
    def __setattr__(self,key,value):
        thread_id = threading.get_ident()
        if thread_id in INFO_DIC:
            INFO_DIC[thread_id][key] = value
        else:
            INFO_DIC[thread_id] = {key:value}

    def __getattr__(self,item):
        thread_id = threading.get_ident()
        return INFO_DIC[thread_id][item]


obj = Local()
lock = threading.RLock()

def fun_two(arg):
    with lock:
        obj.num = arg
        print(obj.num,arg)


for i in range(1,11):
    thread = threading.Thread(target= fun_two,args=(i,))
    thread.start()