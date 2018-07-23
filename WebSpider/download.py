import asyncio
import threading

import requests

# IMAGE_URL='https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'

# r=requests.get(IMAGE_URL)
# with open ('./test_image.png','wb') as f:
#     f.write(r.content)

# r=requests.get(IMAGE_URL, stream=True)
# with open('./test_image2.png','wb') as f:
#     for chunk in r.iter_content(chunk_size=32):
#         f.write(chunk)


#yield again
# import time
#
# def yield_test(n):
#     print('This is yield_test:')
#     for i in range(n):
#         print('i=',i)
#         yield call(i)
#         time.sleep(2)
#         print('====================')
#     print('Do something!')
#     print('end!')
# def call(i):
#     return 'This is CALL,i =='+str(i+1)
#
# for i in yield_test(5):
#     print(i,',')

# 异步IO例子：适配Python3.5，使用async和await关键字
async def hello(index):       # 通过关键字async定义协程
    print('Hello world! index=%s, thread=%s' % (index, threading.currentThread()))
    await asyncio.sleep(1)     # 模拟IO任务
    print('Hello again! index=%s, thread=%s' % (index, threading.currentThread()))

loop = asyncio.get_event_loop()     # 得到一个事件循环模型
tasks = [hello(1)]        # 初始化任务列表
loop.run_until_complete(asyncio.wait(tasks))    # 执行任务
loop.close()