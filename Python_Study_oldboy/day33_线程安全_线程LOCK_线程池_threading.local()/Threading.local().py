import time
import threading

local_obj = threading.local()  # 创建一个全局的local()对象，供所有线程使用
lock = threading.RLock() # 创建一个RLock(递归锁--一次解锁一个线程)

def fun(arg):
    with lock:
        local_obj.my_index = arg # 将在locak对象中为当前线程的创建存储某个变量数据的空间
        # time.sleep(2)
        print(local_obj.my_index,arg)  # 从locak对象当前线程的数据空间中取出自己的值


for i in range(1,11):
    thread = threading.Thread(target=fun,args=(i,))
    thread.start()