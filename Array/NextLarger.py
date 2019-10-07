def nextlarger(array, s):
    new = list()
    for i in range(s):
        for j in range(i + 1, s):
            if array[j] > array[i]:
                new[i] = array[j]
                break
            else:
                break
        new[i] = -1
    print(new)


t = int(input())
for i in range(t):
    s = int(input())
    array = list(map(int, input().split()))
    nextlarger(array, s)
