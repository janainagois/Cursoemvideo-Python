'''n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1'''
n = s = q = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    q += 1
    s += n

print(f'A soma vale {s}.')
