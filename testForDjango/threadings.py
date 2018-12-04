import threading
import time
import queue

condition = threading.Condition()
products = queue.Queue(10)
count = 20


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products, count
        while count > 0:
            if condition.acquire():
                if not products.full():
                    products.put(1)
                    print('Producer {} deliver one! now products: {}'.format(self.name, products.qsize()))
                    condition.notify()
                    count -= 1
                else:
                    print('Producer {}: already 10, stop deliver. now products: {}'.format(self.name, products.qsize()))
                    condition.wait()
                condition.release()
                time.sleep(0.5)
        print('Producer Stop! Producer Stop! Producer Stop! Producer Stop!')


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, products

        while True:
            if condition.acquire():
                if not products.empty():
                    n = products.get()
                    time.sleep(1)
                    print('Consumer {}: consum one, now products: {}'.format(self.name, n))
                    condition.notify()
                else:
                    print('Consumer {}: only 0, stop consume!'.format(self.name))
                    condition.wait(2)
                    break
                condition.release()
                time.sleep(1)
        condition.release()

        print('break consumer!')


# threads = []
#
# for p in range(1):
#     p = Producer()
#     p.start()
#     threads.append(p)
#
# for c in range(2):
#     c = Consumer()
#     c.start()
#     threads.append(c)
# for t in threads:
#     t.join(5)
# print('end main! ')