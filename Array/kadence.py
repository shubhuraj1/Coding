def maxsum(arr,size):
    curmax = arr[0]
    gmax = arr[0]
    for i in range(1,size):
        curmax = max(arr[i],arr[i]+curmax)
        gmax = max(curmax,gmax)
    return gmax

t = int(input())
while t > 0:
    n = int(input())
    ar = list(map(int,input().split()))
    print(maxsum(ar,n))
    t=t-1