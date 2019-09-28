## 方式一:使用multiprocessing模块创建
# import multiprocessing

# def fun(arg):
#     process = multiprocessing.current_process()  # 获取执行本方法的进程
#     process.name = '进程%s'%arg  # 为进程重新设置名称
#     print(arg,arg+10,process.name)

# if __name__ == "__main__":
#     for i in range(1,11):
#         print(i)
#         process = multiprocessing.Process(target=fun,args=(i,))
#         process.start()
#         process.join()  # 阻塞主进程,只有当执行join的进程执行完后才会执行主进程,for循环属于主线程,因此每进行一次for循环就会停一次等待当                     前for循环的子进程执行完
        


## 方式二:使用面向对象方式创建多进程
import multiprocessing
class MyProcess(multiprocessing.Process):
    def run(self):
        print(multiprocessing.current_process().name)


if __name__ == "__main__":
    for i in range(1,11):
        myprocess = MyProcess()
        myprocess.start()  ## 调用父类中的start()方法,父类中的start()方法会调用run方法,此时MyProces中有run方法,则会调用MyProces类中                             方法