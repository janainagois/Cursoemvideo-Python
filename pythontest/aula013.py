'''i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Pula:'))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''
s = 0
for c in range(0, 4):
    n = int(input('Digite um número:'))
# s = s + n é
    s += n
print(f'O somatório de todos os valores foi {s}')


