i = s = ci = csm = csf20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Digite a idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if i >= 18:
        ci += 1
    if s == 'M':
        csm += 1
    if s == 'F' and i < 20:
        csf20 += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar [S/N]?')).upper().strip()[0]
    if c == 'N':
        break
print(f'Total de pesoas com mais de 18 anos: {ci}')
print(f'Foram cadastrados {csm} homens.')
print(f'Foram registradas {csf20} mulheres com menos de 20 anos.')




