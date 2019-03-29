#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

def solution1(change):
    coinValue=[64,16,4,1]
    if change in coinValue:
        return 1
    if not change:
        return 0
    res=0
    for i in range(4):
        temp=coinValue[i]
        num=1
        while temp<change:
            temp+=coinValue[i]
            num+=1
        if temp==change:
            res+=num
            break
        if temp>change:
            temp-=coinValue[i]
            change-=temp
            res=res+num-1
    return res

def solution2(checkList):
    if not checkList:
        return
    for eachWord in checkList:
        word=[i for i in eachWord]
        print(word)
        stack=['']
        index=0
        duplicate=0
        while index<len(word):
            if word[index]!=stack[-1]:
                duplicate = 0
                stack.append(word[index])
                index+=1
            else:
                duplicate+=1
                if duplicate>1 and



if __name__=='__main__':

    # n = sys.stdin.readline().strip()
    # checkList = []
    # while n:
    #     checkList.append(n)
    #     n = sys.stdin.readline().strip()
    # res = solution2(checkList)
    # if res:
    #     for i in res:
    #         print(i)

    # change=1024-int(sys.stdin)
    # print(solution(change))
