#forma Guanabara
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} --> {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'--> {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('--> FIM')
print('~'*30)







'''sequencia de fibonacci
n = int(input('Digite um número inteiro:'))
f_seq = []
a, b = 0, 1
while len(f_seq) < n:
    f_seq.append(a)
    a, b = b, a + b
return f_seq'''




