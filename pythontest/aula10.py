#condições if e else
'''tempo = int(input('Quantos anos tem seu carro?')
if <= 3:
    print('carro novo)
else:
    print('carro velho')'''
#outra forma de fazer tipo operador ternário em outras linguagens

'''tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')'''

#estrutura condicional simples
'''nome = str(input('Qual seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print(f'Bom dia, {nome}')'''

#estrutura condicional composta
'''nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')'''

#exibindo média com mensagem
'''n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')'''
#condição simplificada
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
print('PARABÉNS!' if m >= 6 else 'ESTUDE MAIS')

