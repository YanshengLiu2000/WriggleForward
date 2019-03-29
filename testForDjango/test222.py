#!/usr/bin/python3


import random
from functools import wraps, partial

def quickSort(input):
    l=input
    left=0
    right=len(l)-1
    _qs(l,left,right)
    return l

def _qs(l,left,right):
    if left>=right:
        return
    lb,rb=left,right
    std=left
    while left<right:
        while left<right and l[right]>=l[std]:
            right-=1
        while left<right and l[left]<l[std]:
            left+=1
        l[left],l[right]=l[right],l[left]
    l[std],l[left]=l[left],l[std]
    _qs(l,lb,left-1)
    _qs(l,right+1,rb)


def mergeSort(input):
    l=input
    if len(input)<=1:
        return l
    mid=len(input)//2
    left=mergeSort(l[:mid])
    right=mergeSort(l[mid:])
    return _ms(left,right)

def _ms(left,right):
    res=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r+=1
    if l<len(left):
        res+=left[l:]
    if r<len(right):
        res+=right[r:]
    return res

def heapSort(input):
    l=[0]+input
    firstRootIndex=len(input)//2
    for i in range(firstRootIndex,0,-1):
        heapAdjust(l,i,len(l)-1)

    for i in range(len(l)-1,0,-1):
        l[1],l[i]=l[i],l[1]
        heapAdjust(l,1,i-1)
    return l[1:]

def heapAdjust(l,head,tail):
    root=l[head]
    child=head*2
    while child<=tail:
        if child<tail and l[child]<l[child+1]:
            child+=1
        if root<l[child]:
            l[head]=l[child]
            head=child
            child=head*2
        else:
            break
    l[head]=root

def shellSort(input):
    l=input
    step=len(l)//2
    while step>0:
        for i in range(step,len(l)):
            while i>=step and l[i-step]>l[i]:
                l[i-step],l[i]=l[i],l[i-step]
                i-=step
        step//=2
    return l


def check_answer(sortFunc):
    import random
    print('===========================  {}  ================================='.format(sortFunc.__name__))
    all_correct=True
    for i in range(10):
        a=[random.randint(0,100) for _ in range(20)]
        if sortFunc(a)==sorted(a):
            print('Pass #{}__{}'.format(i,a))
        else:
            print('False to pass:')
            print('a=      ',a)
            print('ans=    ',sorted(a))
            print('ur res= ',sortFunc(a))
            all_correct=False
            break
    if all_correct:
        print('Complete! All Correct!')
    else:
        print('Plz, pay more attention to this sort method!')

# def check(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         import random
#         print('===========================  {}  ================================='.format(sortFunc.__name__))
#         all_correct = True
#         for i in range(10):
#             a = [random.randint(0, 100) for _ in range(20)]
#             if func(args) == sorted(args):
#                 print('Pass #{}__{}'.format(i, args))
#             else:
#                 print('False to pass:')
#                 print('a=  ', args)
#                 print('res=', func(args))
#                 all_correct = False
#                 break
#         if all_correct:
#             print('Complete! All Correct!')
#         else:
#             print('Plz, pay more attention to this sort method!')
#     return wrapper
#
# def check_check(input=None):
#     def decorate(func):
#         a= input if input else None
#         print('a= ',a)
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print('*args: ',*args)
#             print('**kwargs: ',**kwargs)
#             func(*args, **kwargs)
#             return
#         return wrapper
#     return decorate
#
# def check1(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('This is check1!')
#         func(*args, **kwargs)
#         return
#     return wrapper
#
# def check2(func=None,input=None):
#     if func is None:
#         return partial(check2,input=input)
#     test=input if input else None
#     print('check2: ',test)
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         func(*args, **kwargs)
#         return
#     return wrapper
if __name__=='__main__':

    # check_answer(quickSort)
    # check_answer(mergeSort)
    # check_answer(heapSort)
    check_answer(shellSort)
    # shellSort([8,9,1,7,2,3,5,4,6,0])
    # a = [random.randint(0, 100) for _ in range(20)]
    # t1=heapSort(a)
    # t2=sorted(a)
    # print(t1==t2)
