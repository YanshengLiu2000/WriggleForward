

def test(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            n1=str(numbers[i])
            n2=str(numbers[j])
            if n1+n2>n2+n1:
                numbers[i],numbers[j]=numbers[j],numbers[i]
    res=''
    for i in numbers:
        res+=str(i)
    return res
print(test([3,32,321]))
