from random import choice
a = input('Digite o nome do aluno(a) 1:')
b = input('Digite o nome do aluno(a) 2:')
c = input('Digite o nome do aluno(a) 3:')
d = input('Digite o nome do aluno(a) 4:')
alunos = a, b, c, d
aluno_sorteado = choice(alunos)
print(f'O aluno sorteado foi: {aluno_sorteado}!')




