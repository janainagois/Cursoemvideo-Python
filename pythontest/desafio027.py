#lendo um nome completo, mostrando o primeiro e o último nome
nome = str(input('Digite seu nome completo:')).strip()
nome = nome.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')


