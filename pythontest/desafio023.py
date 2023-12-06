#fazendo separação entre unidade, dezena, centena e milhar
'''num = str(input('Digite um número de 0 a 9999:'))
num = num.zfill(4)
uni = num[3]
dez = num[2]
cen = num[1]
mil = num[0]
print(f'Este número tem:\n{uni} unidade\n{dez} dezenas\n{cen} centena\n{mil} milhar')'''
#outra forma de resolver
num = int(input('Informe um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(u)
print(d)
print(c)
print(m)
