def f():
    from random import random as r
    n,k=map(int,input('n k > ').split())
    k-=1; b=range(n)
    a=[[r() for j in b] for i in b]; print(a)
    for j in b: a[k][j]/=a[k][k]
    print(a)
f()

#def f():
#   n = int(input())
#   a =[list(map(int, input().split())) for i in range(n)]
#   for i in range(n):
#        for j in range(n):
#            a[j].append(a[i][j])
#   for k in range(n):
#        for i in range(n):
#            a[i].pop(0)
#   for i in range(len(a)):
#        print(*a[i])
#f()