line = f.readlines()
l = [element.replace ("\n", "").split() for element in line]
n = len(l)
m = len(l[0])
a = l
for i in range(n):
    for k in range(m):
        a[i][k] = int(a[i][k])
    print()

p = n
k = int(input(f'Выберите номер строки из {p} '))
k -= 1
b=range(n)
for j in b:
    a[k][j]/=a[k][k]

with open('ZhiboedovKV_u224_vivod.txt', 'w') as f2:
    for i in range(n):
        for k in range(m):
            f2.write(str(a[i][k]))
            f2.write(' ')
        f2.write('\n')

with open('ZhiboedovKV_u224_vvod.txt', 'r+') as f:
    line = f.readlines()
    l = [element.replace ("\n", "").split() for element in line]
n = len(l)
m = len(l[0])
a = l
for i in range(n):
    for k in range(m):
        a[i][k] = int(a[i][k])
    print()

res=[]
for j in range(m):
    tmp=[]
    for i in range(n):
        tmp=tmp+[a[i][j]]
    res=res+[tmp]

with open('ZhiboedovKV_u224_vivod.txt', 'a+') as f2:
    f2.write('\n')
    for i in range(n):
        for k in range(m):
            f2.write(str(res[i][k]))
            f2.write(' ')
        f2.write('\n')