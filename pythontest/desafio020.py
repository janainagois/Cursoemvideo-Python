#sortenado uma sequência de nomes
import random
'''a = input('Digite o nome do aluno(a) 1:')
b = input('Digite o nome do aluno(a) 2:')
c = input('Digite o nome do aluno(a) 3:')
d = input('Digite o nome do aluno(a) 4:')
alunos = a, b, c, d
quantidade = 4
sequência = random.sample(alunos, quantidade)
print(f'A sequência da apresentação será: {sequência}')'''

#outra forma de fazer
#dá pra fazer este programa utilizando from random import shuffle
a = input('Digite o nome do aluno(a) 1:')
b = input('Digite o nome do aluno(a) 2:')
c = input('Digite o nome do aluno(a) 3:')
d = input('Digite o nome do aluno(a) 4:')
lista = [a, b, c, d]
random.shuffle(lista)
print(f'A ordem de apresentação será')
print(lista)

