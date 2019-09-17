from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import time

def task(arg):
    process = multiprocessing.current_process()
    process.name = '进程%s'%arg
    print(arg,process.name)

if __name__ == "__main__":
    pool = ProcessPoolExecutor(5) # 创建5个进程的进程池
    for i in range(1,11):
        pool.submit(task,i)
    time.sleep(5)