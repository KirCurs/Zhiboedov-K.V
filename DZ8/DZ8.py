# -- coding: utf-8 --
#def f():
#    for i in range(int(input())):
#        for j in str(i):
#            res = int(j)
#            if res != 0 and res != 1 and i % res:
#                break
#        else:
#            print (i)
#f()

def func1(a):
    a[0], a[-1] = a[-1], a[0]
    return a
n = int(input('m = '))
a = list(map(int, input('в одну строку через пробел ').split(maxsplit = n)))
print(a)
print(func1(a))