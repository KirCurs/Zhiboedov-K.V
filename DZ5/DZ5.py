#--coding: utf-8 --
#1
#def f(): 
#    n = int(input())
#    i = 1
#    while i ** 2 <= n:
#        print(i ** 2)
#        i += 1
#f()

#2
#def f():
#    n = int(input())
#    i = 2
#    while n % i != 0:
#        i += 1
#    print(i)
#f()

#3
#def f():
#    num = int(input())
#    cnt = 1
#    while 2**cnt <= num:
#        cnt += 1
#    print(cnt-1, 2**(cnt-1))
#f()

#4
#def f():
#    n1 = int(input())
#    n2 = int(input())
#    cnt = 1
#    while n1 < n2:
#        n1 *= 1.1
#        cnt += 1
#    print(cnt)
#f()

#5
#def f():
#    cnt = 0
#    while True:
#        n = int(input())
#        if n == 0:
#            break
#        cnt += 1
#    print(cnt)
#f()

#6
#def f():
#    n1 = 0
#    n2 = -1
#    while True:
#        num = int(input())
#        n1 = n1 + num
#        n2 = n2 + 1
#        if num == 0:
#            break
#    print(n1/n2)
#f()

#7
def f ():
    n = -1
    m = -1
    b = -1
    while n != 0:
        n = int(input())
        if n > m:  
            b += 1 
        m = n      
    print(b)
f()