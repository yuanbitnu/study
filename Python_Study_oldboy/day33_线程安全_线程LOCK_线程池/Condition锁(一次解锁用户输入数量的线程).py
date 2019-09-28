import threading
import time


# ############## 方式一 ##############
""" lis = []
lock = threading.Condition()  ## 一次解锁三个线程
print('主线程开始位置')
def fun(item):
    current_thread = threading.current_thread()
    # lock.acquire() ## 方式一的加锁
    with lock:  ## 方式二
        lock.wait()
        print('线程**%s**开始执行'%current_thread.getName())
        lis.append(item)
        time.sleep(1)
        value = lis[-1]
        print(item,value,'---')
        print('线程**%s**执行结束'%current_thread.getName())
    # lock.release() ## 方式一的解锁

for i in range(1,11):
    thread = threading.Thread(target=fun,args=(i,),name=str(i))
    thread.start()

def input_fun():
    while True:
        num = int(input('输入数量>>>>'))  ## 输入用户想要解锁的数量
        lock.acquire()
        lock.notify(num)  # notify--通知
        lock.release()

thread_input = threading.Thread(target=input_fun)
thread_input.start()

print('主线程代码结束位置')
 """


# ############## 方式二 ##############

lis = []
lock = threading.Condition()  ## 一次解锁三个线程
print('主线程开始位置')

def input_fun():
    num = int(input('输入数量>>>>')) ## 输入用户想要解锁的数量
    while True:
        if num > 0:
            num -= 1
            return True
        else:
            return False

def fun(item):
    current_thread = threading.current_thread()
    lock.wait_for(input_fun)
    print('线程**%s**开始执行'%current_thread.getName())
    lis.append(item)
    time.sleep(1)
    value = lis[-1]
    print(item,value,'---')
    print('线程**%s**执行结束'%current_thread.getName())


for i in range(1,11):
    thread = threading.Thread(target=fun,args=(i,),name=str(i))
    thread.start()




# thread_input = threading.Thread(target=input_fun)
# thread_input.start()

print('主线程代码结束位置')
