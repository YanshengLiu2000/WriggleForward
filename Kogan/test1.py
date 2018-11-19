import json
import time
from urllib.request import urlopen





def spend_time():
    def decorator(func):
        def wrapper(*args, **kw):
            start=time.time()
            func(*args, **kw)
            print('It spends: ',time.time()-start)
        return wrapper
    return decorator


@spend_time()
def solution():
    prefix='http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com'
    suffix='/api/products/1'
    num=0.0
    total_weight=0.0

    while suffix:
        u = urlopen(prefix+suffix)
        data=json.load(u)
        for item in data['objects']:
            if item['category'] == 'Air Conditioners':
                print(item['category'])
                total_weight+=float(item['size']['width'])*0.01*float(item['size']['length'])*0.01*float(item['size']['height'])*0.01*250
                print(total_weight)
                num+=1
        suffix=data['next']
        print("suffix",suffix)
    avg_weight=total_weight/num*1000
    print('The average weight of {} air conditioners is {}'.format(num, avg_weight))

if __name__ =='__main__':
    solution()