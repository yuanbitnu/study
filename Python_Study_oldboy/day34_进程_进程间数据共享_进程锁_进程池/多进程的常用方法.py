import multiprocessing
import time

##########多进程常用方法join()################
# def task(arg):
#     process = multiprocessing.current_process()
#     process.name = '进程%s'%arg
#     print(arg,process.name)


# if __name__ == "__main__":
#     for i in range(1,11):
#         process = multiprocessing.Process(target=task,args=(i,))
#         process.start()
#         process.join() ## 阻塞主进程,只有当执行了join方法的子进程执行完了以后主进程的循环才能继续进行下去


##########多进程常用方法daemon属性################
def task(arg):
    process = multiprocessing.current_process()
    process.name = '进程%s'%arg
    time.sleep(1)
    print(arg,process.name)


if __name__ == "__main__":
    for i in range(1,11):
        process = multiprocessing.Process(target=task,args=(i,))
        process.daemon = True  ## 守护进程setDaemon 默认都为非守护进程,表示该进程很重要, 在start()之前执行，决定主进程是否要等该子进程                               执行完以后才能关闭,子进程会继承父线程的Daemon属性，python主进程会在等待所有的非守护进程结束后才                                会结束,
        process.daemon = False ## False为非守护进程, True为守护进程
        process.start()
        process.join()