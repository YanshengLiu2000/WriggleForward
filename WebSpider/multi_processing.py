import multiprocessing as mp
import threading as td
import os
import time
import random

def job(queue,process_name,sleep_time):
    print('{} is running!{}'.format(process_name,os.getppid()))
    time.sleep(sleep_time)
    queue.put(process_name)

if __name__=='__main__':
    q=mp.Queue()
    p1=mp.Process(target=job, args=(q, 'P1', 2))
    p2=mp.Process(target=job, args=(q, 'P2', 1))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1=q.get()
    res2=q.get()
    print('res1=={} and res2=={}'.format(res1,res2))
