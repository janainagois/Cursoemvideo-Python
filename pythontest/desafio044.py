#calculando preços e condições
'''preço = float(input('Digite o valor do produto:'))
forma = float(input('Digite 1 se for pagar no dinheiro ou cheque.\nDigite 2 se for pagar no cartão:'))
if forma == 1:
    print(f'Você pagará R${preço - (preço * 10/100)} ')
if forma == 2:
    parcela = int(input('Em quantas vezes você vai pagar?'))
    if parcela == 1:
        print(f'Você pagará R${preço - (preço * 5/100)}')
    elif parcela == 2:
        print(f'Você pagará R${preço}')
    else:
        print(f'Você pagará {preço + (preço * 20/100)}')'''
#forma Guanabara
print('{:=^40}'.format(' LOJA DA JANA '))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[ 1 ] à vista no dinheiro ou cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} sem juros')
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print(f'Sua compra será parcela em {totparc}x de R${parcela:.2f} com juros')
else:
    total = preço
    print('Operação inválida! Tente novamente.')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')




