# номер 4 блок А

def rec_sum(n, s = 0):
    a, b = divmod(n, 10)
    s += b
    if a == 0:
        return print(s)
    rec_sum(a, s)

rec_sum(int(input()))

# номер 1 блок В

def maximum():
    a = int(input('Введите число a: '))
    if a == 0:
        return 0
    else:
        return max(a, maximum())

print(maximum())
