# 进程是计算机资源分配的最小单元
# 线程是CPU计算的最小单元
# 进程间的数据是不共享的,但是可以通过 multiprocessing.queues.Queue()以及multiprocessing.Manager()创建的对象进行数据的共享
# Windows环境下多进程的执行必须在 main入口下才能正常执行  -- if __name__ == if __name__ == "__main__"
