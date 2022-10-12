#1
#def f():
#    a = int(input())
#    b = int(input())
#    for i in range(a, b + 1):
#        print(i)
#f()

 
#2
#def f():
#    a = int(input("Enter num 1: "))
#    b = int(input("Enter num 2: "))
#    if b > a:    
#        for i in range(a, b+1):
#            print(i)
#    else:
#        for i in range (b, a+1):
#            print(i)
#f()
 
#3
#def f():
#    a = int(input())
#    b = int(input())
#    for i in range (a - (a + 1) % 2, b - b % 2, - 2):
#        print(i)
#f()
 
#5
#def f ():
#    sum = 0
#    n = int(input())
#    for i in range(1, n + 1):
#        sum = sum + (i ** 3)
#    print(sum)
 
#4
#def f():
#    quantity = int(input())
#    sum = 0
#    for i in range(quantity):
#        n = int(input())
#        sum = sum + n
#    print(sum)
#f()

#6
#def f ():
#    n = int(input())
#    fac = 1
#    for i in range(1, n+1):
#        fac = fac*i
#    print(fac)
#f()

#7
#def f():
#    n = int(input())
#    fac = 1
#    sum = 0
#    for i in range(1, n + 1):
#        fac = fac * i
#        sum = sum + fac
#    print(sum)
#f()

#8
#def f():
#    n = int(input())
#    for i in range(n):
#        for j in range(1, i+2):
#            print(j, end ="")
#        print()
#f()

#9 Может подтормаживать из за рекурсии, не понимаю как сделать ее менее нагруженной
n=int(input("Enter num of Fib: "))
def Fib(n):
   if n==1 or n==2:
       return 1
   else:
       return Fib(n-2)+ Fib(n-1)
print(Fib(n+2)-1)