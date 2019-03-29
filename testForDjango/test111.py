def bubbleSort(input):
    L=input[:]
    for i in range(len(L)-1):
        for j in range(i,len(L)):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L

def selectSort(input):
    L=input[:]
    for i in range(len(L)):
        minIndex=i
        for j in range(i,len(L)):
            if L[minIndex]>L[j]:
                minIndex=j
        L[minIndex],L[i]=L[i],L[minIndex]
    return L

def insertSort(input):
    L=input[:]
    res=[0]# 这里需要注意一下, 为什么是0呢, 因为如果res这里是L[0]的话, 进入j循环的第一个元素会报错.
    for i in range(len(L)):
        for j in range(len(res)):
            if L[i]<res[j]:
                break
        res.insert(j,L[i])
    return res[:-1]

def poilSort(L):
    book=[0 for i in range(101)]
    for i in L:
        book[i]+=1
    res=[]
    for i in range(len(book)):
        while book[i]:
            res.append(i)
            book[i]-=1
    return res
def quickSort(input):
    """
    最好的时间复杂度和平均时间复杂度是nlogn,无序状态
    有序状数组,最坏时间复杂度o(n**2)
    因为每次都只能移动一个元素
    """
    L=input[:]
    left=0
    right=len(L)-1
    _qs(L,left,right)
    return L
def _qs(L,left,right):
    leftPointer=left
    rightPointer=right
    standard=left
    if left>=right:
        return
    while left<right:
        while right>left and L[standard]<=L[right]:#记得要加上等于号
            right-=1
        while right>left and L[standard]>L[left]:
            left+=1
        L[left],L[right]=L[right],L[left]
    L[standard],L[left]=L[left],L[standard]
    _qs(L,leftPointer,left-1)
    _qs(L,right+1,rightPointer)

def mergeSort(L):
    """
    并归排序是一种时间复杂度很稳定的排序方法, O(nlogn),空间复杂度是O(n)
    """
    if len(L)<=1:#记得需要加这个!!否则会一直循环的! 边界条件!
        return L
    mid=len(L)//2
    left=mergeSort(L[:mid])
    right=mergeSort(L[mid:])
    return _merge(left,right)

def _merge(leftList, rightList):
    res=[]
    leftPointer=rightPointer=0
    while leftPointer<len(leftList) and rightPointer<len(rightList):
        if leftList[leftPointer]<rightList[rightPointer]:
            res.append(leftList[leftPointer])
            leftPointer+=1
        else:
            res.append(rightList[rightPointer])
            rightPointer+=1
    if leftPointer<len(leftList):
        res+=leftList[leftPointer:]
    if rightPointer<len(rightList):
        res+=rightList[rightPointer:]
    return res

def heapSort(input):
    """
    heapAdjust函数时间复杂度是O(logN)
    建堆过程时间复杂度是O(N)
    具体证明:
    https://blog.csdn.net/qq_34228570/article/details/80024306
    https://www.zhihu.com/question/20729324
    之后排序重建堆的时候:
    每次建堆时间复杂度之和为O(log(N!))==O(Nlog(N))

    """
    L=[0]+input[:]
    firstSortNode=len(input)//2
    for i in range(firstSortNode,0,-1):
        _heapAdjust(L,i,len(L)-1)
    print('test in heapSort',L)#最大堆
    # print('test in heap sort',L)
    for i in range(len(L)-1,0,-1):#注意这里的len(l)-1 , 直接用len(l)会out of index
        L[1],L[i]=L[i],L[1]
        _heapAdjust(L,1,i-1)# 最后一个点每次往前挪一个~ 这就是为什么需要i-1
    return L[1:]#注意这里返回的不是l本身,而是l[1:]

def _heapAdjust(L,head,tail):
    root=L[head]
    child=head*2
    while child<=tail:#这里需要一个小于等于
        if child<tail and L[child]<L[child+1]:#这里需要一个判断child<tail 因为上面有等号
            child+=1
        if root<L[child]:
            L[head]=L[child]
            head=child
            child=head*2
        else:
            break
    L[head]=root#最后这个L[head]其实是child, root保存的是之前的父节点, 因为在之前的步骤中head=child, 所以这里是子节点

def shellSort(input):#http://www.cnblogs.com/qlshine/p/6052223.html
    l=input
    step=len(l)//2
    while step>0:
        for i in range(step,len(l)):
            while i>=step and l[i-step]>l[i]:#记得这个, 是需要不停向前检索的
                l[i],l[i-step]=l[i-step],l[i]
                i-=step#别忘了这个, 逐级往前传递!
        step//=2
    return l

if __name__=='__main__':
    import random

    testCase=[random.randint(0,100) for i in range(10)]
    # testCase=[27, 86, 45, 16, 51, 81, 39, 90, 2, 11]
    testCase=[27, 86, 45, 16, 51, 81, 39, 90, 2, 11]
    print('This is test case:',testCase)
    bubbleRes=bubbleSort(testCase)
    print('This is bubble result:',bubbleRes==sorted(testCase))
    selectRes=selectSort(testCase)
    # print(selectRes)
    print('This is select result: ', selectRes==sorted(testCase))
    insertRes=insertSort(testCase)
    # print(insertRes)
    print('This is insert result: ', insertRes==sorted(testCase))
    poilRes=poilSort(testCase)
    # print(poilRes)
    print('This is poil result: ',poilRes==sorted(testCase))
    quickRes=quickSort(testCase)
    # print(quickRes)
    print('This is quick result: ',quickRes==sorted(testCase))
    mergeRes=mergeSort(testCase)
    print(mergeRes)
    print('This is Merge Res: ', mergeRes==sorted(testCase))
    heapRes=heapSort(testCase)
    print(heapRes)
    print('This is heap result: ',heapRes==sorted(testCase))