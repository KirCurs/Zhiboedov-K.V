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

def pr(mas):
    p = n
    k = int(input(f'Выберите номер строки из {p} '))
    k -= 1
    b=range(n)
    for j in b:
        mas[k][j]/=mas[k][k]
    return mas

with open('ZhiboedovKV_u224_vivod.txt', 'w') as f2:
    f2.write(str(pr(a)))
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
def transponse(matr):
    res=[]
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[matr[i][j]]
        res=res+[tmp]
    return res

with open('ZhiboedovKV_u224_vivod.txt', 'a+') as f2:
    f2.write('\n')
    f2.write(str(transponse(a)))
    f2.write('\n')