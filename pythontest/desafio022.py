'''lendo o nome completo e mostrando ele todo maiúsculo,
todo minúsculo, contando todas as letras exceto os espaços,
 quantas letras tem o primeiro nome'''

nome = input('Digite seu nome completo:')
print(nome.upper())
print(nome.lower())
print(len(nome) - (nome.count(' ')))
print(len(nome.split()[0]))
#outra forma de contar o número de letras do primeiro número
#print(nome.find(' '))
print(nome.strip())



