import sys

class A():
    def __init__(self):
        print('object id: ',str(id(self)))

def func():
    while True:
        c1=A()
        del c1

def func1(c):
    print('object refcount: ',sys.getrefcount(c))



class Demo:
    a=1
    @classmethod
    def classprint(cls):
        print('ClassMethod!',cls.a)
        cls.a+=1
    @staticmethod
    def staticprint():
        print('StaticPrint!')
    @property
    def propertyprint(self):
        print('property Print!',self.a)
        return self.a
if __name__=='__main__':
    a=A()
    func1(a)


    # b=a
    # func1(a)
    # obj1=Demo()
    # obj1.classprint()
    # Demo.classprint()
    # obj2=Demo()
    # obj2.classprint()
    # print(Demo.a)
    # Demo.propertyprint

    import time
    from functools import wraps

    def timethis(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            print('test!!',args)
            print('test!!kwargs',kwargs)
            result = func(*args, **kwargs)
            print('The result is ',result)
            end = time.time()
            print(func.__name__, end-start)
            return result
        return wrapper


    def record_time(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start=time.time()
            result=func(args,**kwargs)
            total=time.time()-start
            print(func.__name__, total)
            return result
        return wrapper

    @timethis
    def countdown(a,b,c):
        time.sleep(1)
        print(a)
        time.sleep(1)
        print(b)
        time.sleep(1)
        print(c)
        return 'result!'

    print(countdown(1,2,[1,2,3]))