# import json
# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor
# from urllib.request import urlopen
# from queue import Queue
#
#
# # def fetch_url(url):
# #     u = urllib.request.urlopen(url)
# #     data = u.read()
# #     return data
#
#
# def catch_data(suffix):
#     prefix = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
#     total_weight = 0.0
#     num = 0.0
#     u = urlopen(prefix + suffix)
#     data = json.load(u)
#     new_suffix = data['next']
#     lock.acquire()
#     global book
#     global queue
#     if new_suffix not in book:
#         queue.put(new_suffix)
#     else:
#         return
#     lock.release()
#
#     for item in data['objects']:
#         if item['category'] == 'Air Conditioners':
#             print(item['category'])
#             total_weight += float(item['size']['width']) * 0.01 * float(item['size']['length']) * 0.01 * float(
#                 item['size']['height']) * 0.01 * 250
#             print(total_weight)
#             num += 1
#     lock.acquire()
#     if suffix not in book and num!=0:
#         book[suffix] = (num, total_weight)
#     lock.release()
#
#
#
#
# if __name__ == '__main__':
#     start = time.time()
#     prefix = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
#     suffix = '/api/products/1'
#     total_num = 0.0
#     total_weight = 0.0
#     queue = Queue()
#     queue.put(suffix)
#     book = {}
#     lock = threading.Lock()
#
#     pool = ThreadPoolExecutor(2)
#     # Submit work to the pool
#     a = pool.submit(fetch_url, 'http://www.python.org')
#     b = pool.submit(fetch_url, 'http://www.pypy.org')
#
#     # Get the results back
#     x = a.result()
#     y = b.result()
#
#
#     while True:
#         suffix = queue.get()
#         if suffix == None:
#             break
#         worker1=pool
#
#
#
#
# # q=Queue()
# # q.put(1)
# #
# # test=[2,3,4,5,6,7,8,-1]
# #
# # while q:
# #     t = test.pop(0)
# #     if t ==-1:
# #         break
# #     print(q.get())
# #     q.put(t)