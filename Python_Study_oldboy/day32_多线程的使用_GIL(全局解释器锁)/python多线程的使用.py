import threading
import time

#### https://www.cnblogs.com/whatisfantasy/p/6440585.html

# 一、线程
        ## 线程是CPU执行的最小单元，一个程序默认是一个进程，一个进程默认是一个线程
        ## 多线程是在一个进程中创建多个线程去执行程序的任务，多个线程共享同一个进程中的数据资源

# 二、GIL锁 (全局解释器锁) 
        ## 在非python环境中，单核情况下，同时只能有一个任务执行。多核时可以支持多个线程同时执行。但是在python中，无论有多少核，同时只能执行一个线程。究其原因，这就是由于GIL的存在导致的。
        ## C# jave 多线程的执行 允许一个进程中的多个线程在同一个时间片内都能被CPU(多核)同时调度执行----(几核CPU就能在同一个时间片内调度同一个进程中几个线程)
        ## python 多线程的执行  python中因为有GIL锁，一个进程在一个时间片内只能有一个线程被CPU(多核)调度执行---(尽管CPU有4核，但是在同一个时间片内针对一个进程的多个线程也只能有一个线程被一个CPU调度执行)
        
# 三、进程
        ## 进程用来隔离不同程序之间的数据 进程在线程之上，一个进程可以包含一个或多个线程，多个线程使用同一个进程中的数据资源

# 四、创建线程的方法
        ## 1、通用创建方式

                # def fun(a,b):
                #     thread_name = threading.current_thread().getName()
                #     time.sleep(3)
                #     print('result = %d' %(a+b))
                #     print('线程--%s--执行完毕' % thread_name)


                # sub_thread_one = threading.Thread(target= fun,args=(2,3,),name='线程1')
                # sub_thread_one.start()

        ## 2、面向对象的创建方式

                ## threading.Thread 内部创建线程后通过线程调用run()方法

                # class MyThread(threading.Thread):
                    
                #     def __init__(self,*args,**kwargs):
                #         threading.Thread.__init__(self)
                #         self.args = args
                #         self.kwargs = kwargs
                #         self.name = kwargs['thread_name']
                    
                #     def run(self):   ## 重写 run() 方法
                #         result = 0
                #         for item in self.args:
                #             result += item
                #         print(result)
                #         thread_name = self.getName()
                #         print('线程--%s--执行完毕' % thread_name)

                # mythread_one = MyThread(5,5,thread_name = '线程1' )
                # mythread_one.start()

                # mythread_two = MyThread(5,5,6,7,8,thread_name = '线程2')
                # mythread_two.start()

# 五、threading.Thread 中常用方法

        ## 1、setName() and getName() 为设置或获取线程名字

                # def add(a,b):
                #     thread = threading.current_thread()
                #     thread_name = thread.getName()
                #     print('修改前的线程名%s'%thread_name)
                #     print('result = %d' %(a+b))
                #     thread.setName('线程2')
                #     print('线程--%s--执行完毕' % thread.getName())
                    

                # thread = threading.Thread(target= add,args=(5,9),name='线程1')
                # thread.start()

        ## 2、setDaemon(bool)  守护线程，默认都为非守护线程 在start()之前执行，决定主线程是否要等该线程执行完以后才能关闭整个进程,
                    ### 子线程会继承父线程的Daemon属性，python进程 会在等待所有的非守护线程结束后才会结束

                    ### 默认为False，该线程为非守护线程，表示该线程重要，主线程必须要等该非守护线程执行完后才能结束整个进程


                            #### 不设置Daemon 或者显示的设置为 False，该线程为非守护线程，是重要的，主线程必须要等该线程执行完才能结束整个进程
                            # def add(a,b):
                            #     thread = threading.current_thread()
                            #     print('result = %d' %(a+b))
                            #     time.sleep(5)
                            #     print('线程--%s--执行完毕' % thread.getName())
                                

                            # thread = threading.Thread(target= add,args=(5,9),name='线程1')
                            # thread.setDaemon(False)  ## 默认即为False，不显示的设置也为非守护线程
                            # thread.start()

                            # print('主线程已执行完毕。。。。')

                    ### 设置为True ，该线程为守护线程，表示该线程不重要，主线程不需要等待这个线程执行完

                            # def add(a,b):
                            #     thread = threading.current_thread()
                            #     print('result = %d' %(a+b))
                            #     time.sleep(5)
                            #     print('线程--%s--执行完毕' % thread.getName())
                                

                            # thread = threading.Thread(target= add,args=(5,9),name='线程1')
                            # thread.setDaemon(True)  ## 设置为True 该线程为守护线程，表示该线程不重要，在主线程内容执行完后，会直接将还未执行完的子线程回收并结束该进程
                            # thread.start()

                            # print('主线程已执行完毕。。。。')

        ## 3、jion(timeout) 阻塞主线程，默认主线程在将子线程start()后会直接继续执行主线程代码，但如果主线程需要在某子线程执行完毕后再执行，则可以在子线程start()后，调用子线程的join()方法，此时主线程的代码会等待子线程的代码执行完成后再执行
                ### timeout 不设置值表示主线程代码会一直等待子线程执行完后在执行，设置值时表示主线程只等待子线程执行设置的秒数后就会继续执行主线程代码
                    # def add(a,b):
                    #     thread = threading.current_thread()
                    #     print('result = %d' %(a+b))
                    #     for i in range(0,5):
                    #         time.sleep(1)
                    #         print('子线程睡眠%d秒'%(i+1))
                    #     print('线程--%s--执行完毕' % thread.getName())
                        

                    # thread = threading.Thread(target= add,args=(5,9),name='线程1')
                    # thread.start()
                    # thread.join()

                    # print('主线程已执行完毕。。。。')
        
        ## 4、threading.current_thread()  获取执行当前任务的线程

                    # thread = threading.current_thread()  ## 获取当前线程的名称，当前为主线程，name为MainThread
                    # print('修改前的主线程名--%s--'%thread.getName())  ## result = MainThread
                    # thread.setName('主线程1')
                    # print('修改后的主线程名--%s--'%thread.getName())  ## result = 主线程1