#empréstimo bancário
valor = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você paragará a casa?'))
#calculando o valor da prestação mensal
parcela = valor / (anos * 12)
if parcela >= (salário * (30/100)):
    print('Infelizmente seu empréstimo foi negado!')
else:
    print(f'A parcela do seu empréstimo é R${parcela:.2f}')