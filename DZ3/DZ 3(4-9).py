# -- coding: utf-8 --
#a = int(input())
#b = int(input())
#L = int(input())
#N = int(input())
#print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)

#max-min
#a1 = int(input("First Num: "))
#b1 = int(input("Second Num: "))
#c1 = int(input("Third Num: "))
#if b1 >= a1 <= c1:
#    print(a1)
#elif a1 >= b1 <= c1:
#    print(b1)
#else:
#    print(c1)

#Шахматы 
#d= int(input())
#a= int(input())
#b= int(input())
#c= int(input())
#if (a+b+c+d) % 2 == 0:
#    print('YES')
#else:
#    print('NO')

#Years
#year = int(input())
#if year % 4 == 0 and year % 100 != 0  and year % 400 == 0:
#    print("YES") 
#else: print("NO")

#Совпадение чисел
#n1 = int(input())
#n2 = int(input())
#3 = int(input())
#if n1 == n2 == n3:
#    print(3)
#elif n1 == n2 or n2 == n3 or n1 == n3:
#    print(2)
#else: print(0)

#Шоколадка
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')