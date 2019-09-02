import threading
import time

lis = []
def add(item):
    current_thread = threading.current_thread()
    # print('线程**%s**开始执行'%current_thread.getName())
    lis.append(item)
    time.sleep(1)
    print(item,lis[-1],'---')
    # print('线程**%s**执行结束'%current_thread.getName())

for i in range(1,11):
    thread = threading.Thread(target=add,args=(i,),name=str(i))
    thread.start()
