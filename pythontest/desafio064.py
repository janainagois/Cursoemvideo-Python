#considerando 999 como ponto de parada e somando os valores desconsiderando o flog
n = cont = soma = 0
n = int(input('Digite um número inteiro e 999 para parar:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro e 999 para parar:'))
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')

print()



