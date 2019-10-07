def missingno(c, n):
    sum1 = (n * (n + 1)) / 2
    sum2 = 0
    for i in range(len(c)):
        sum2 += c[i]
    print(int(sum1 - sum2))


t = int(input())
while t > 0:
    n = int(input())
    c = list(map(int, input().split()))
    missingno(c, n)
    t = t - 1
