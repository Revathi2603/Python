#to get the sum of the largest number of the list among the other lists within the list.
n=int(input())
a=[map(int,input().split()) for i in range(n)]
m=0
for i in a:
    s = sum(i)
    if s>m:
        m=s
        ind = a.index(i)
print(ind)