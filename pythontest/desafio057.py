#verificando sexo feminino e masculino
'''while True:
    sexo = str(input('Digite o sexo[M/F]:')).strip().upper()[0]
    if sexo == "M" or sexo == "F":
        print(sexo)
    else:
        print('Alternativa inválida. Digite apenas "M" ou "F".')'''
#forma Gunabara
sexo = str(input('Digite o sexo [M/F]:'))
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]:')).strip().upper()[0]
print(f'Sexo {sexo} informado com sucesso!')
