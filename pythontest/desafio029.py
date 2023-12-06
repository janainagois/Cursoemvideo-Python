
#multa por excesso de velocidade

#qual a velocidade do seu carro?
vel = float(input('Você está dirigindo seu carro em quantos km/h?'))
#se a velocidade for maior que 80km/h mostre uma mensagem dizendo que ele foi multado
if vel > 80:
    print('Você está acima da velocidade permitida de 80km/h.\nVocê foi multado!')
#calcular o valor da multa
    multa = (vel - 80) * 7
    print(f'Você deve pagar R${multa} de multa!')
print('Tenha um bom dia! Dirija com segurança!')
'''from random import randint
#o computador vai "escolher" uma velocidade
vel = randint(60,120)
print(f'o computador vai a {vel} km/h')
if vel > 80:
    print('A máquina foi multada!')
#calcular o valor da multa
    multa = (vel - 80) * 7
    print(f'Ela deve pagar R${multa} de multa!')'''


