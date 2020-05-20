t=int(input())
while(t>0):
    n=int(input())
    arr=[]
    for i in range(n):
        num=int(input())
        if(num>0):
            arr.append(num)
    print(arr)
    t=t-1
