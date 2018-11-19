import json
import threading
from queue import Queue
from urllib.request import urlopen

prefix = 'http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
suffix = '/api/products/1'

queue = Queue()
queue.put(suffix)  # use to record tasks
book = {}  # use to save (num,weight) in some pages which contains AC
lock = threading.Lock()
threads = []  # record all used threads


class myThread(threading.Thread):
    """
    This thread is used to count all ACs (both num and weight)in each page.
    """

    def __init__(self, suffix):
        threading.Thread.__init__(self)
        # suffix of the url
        self.suffix = suffix

    def run(self):
        # pass the url to the function which can record useful data
        catch_data(self.suffix)


def catch_data(suffix):
    """
    :param suffix:
    :return: None

    Use both prefix and suffix to build a valid url and record AC number and weight.
    the data will be record in a dictionary called book
    book[suffix]=(number, weight)
    """
    weight = 0.0  # initialize AC weight in this page
    num = 0.0  # initialize AC number in this page, just in case it they may out of range, use float instead of int
    u = urlopen(prefix + suffix)  # open url
    data = json.load(u)  # load json
    new_suffix = data['next']
    global book
    global queue
    lock.acquire()  # get the lock
    if new_suffix not in book:  # if the 'next page' is not be record, add the suffix into queue.
        queue.put(new_suffix)
    else:
        return  # This means this page has already been checked, stop this thread.
    lock.release()  # release the lock.

    for item in data['objects']:  # check objects one by one
        if item['category'] == 'Air Conditioners':
            weight += float(item['size']['width']) * 0.01 * float(item['size']['length']) * 0.01 * float(
                item['size']['height']) * 0.01 * 250
            num += 1  # count num and calculate weight
    lock.acquire()
    if suffix not in book and num != 0:  # check the suffix again, just in case.
        book[suffix] = (num, weight)  # if this suffix not in book and this page has ACs, record (num,weight)
    lock.release()


def get_result():
    while True:
        suffix = queue.get()
        if suffix == None:  # at the end of all these tasks, stop the loop.
            break
        thread = myThread(suffix)
        thread.start()  # start a new task
        threads.append(thread)  # record the task
    for t in threads:
        t.join()  # in case there are a lot of info in a page(a million AC in a page?), kill all rasks at the end of all thread completes.
    # Main script will not continue until all tasks complete their jobs.
    #This part may cases stack overflow.
    total_num = 0
    total_weight = 0  # initialize all AC number and weight in this page
    for page in book:
        num, weight = book[page]
        total_num += num
        total_weight += weight
    avg = total_weight / total_num * 1000  # calculate avg
    return avg


if __name__ == '__main__':
    print("The average weight of all ACs is {0:.3f} grams.".format(get_result()))
