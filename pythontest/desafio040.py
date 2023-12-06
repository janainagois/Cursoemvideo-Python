#calculando média
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2)/2
if m < 5:
    print('Infelizmente você foi reprovado.')
elif (7 >m >=5):#solução matemática a forma de expressar em python é usando 'and'
    print('Você vai pra recuperação!')
else:
    print('Parabéns! Você foi aprovado.')

