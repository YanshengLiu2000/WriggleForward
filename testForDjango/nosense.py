import multiprocessing

def func(data):
    result=data*data
    return result

if __name__=='__main__':
    inputs=[i for i in range(100)]
    pool=multiprocessing.Pool(processes=4)
    pool_outputs=pool.map(func, inputs)
    pool.close()
    pool.join()
    print('Pool     : ',pool_outputs)