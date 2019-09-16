from concurrent.futures import ThreadPoolExecutor
import threading
import time

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

local = Local()
lock = threading.RLock()

def fun_one(arg):
    with lock:
        local.num = arg
        print(local.num,arg)

pool = ThreadPoolExecutor(5)
for i in range(1,10):
    pool.submit(fun_one,i)

time.sleep(5)

print(INFO_DIC)  ## 值仅有最后5个线程的值
