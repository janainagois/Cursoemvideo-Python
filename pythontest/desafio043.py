#calculando IMC
peso = float(input('Digite o seu peso (Kg):'))
altura = float(input('Digite sua altura (m):'))
IMC = peso/altura**2
if IMC < 18.5:
    print(f'Seu IMC é {IMC:.1f}, você está abaixo do peso!')
elif IMC <= 25:
    print(f'Seu IMC é {IMC:.1f}, você está no seu peso ideal!')
elif IMC <= 30:
    print(f'Seu IMC é {IMC:.1f}, você está com sobrepeso!')
elif IMC <= 40:
    print(f'Seu IMC é {IMC:.1f}, você está com obesidade!')
else:
    print(f'Seu IMC é {IMC:.1f}, você está com obesidade mórbida!')
