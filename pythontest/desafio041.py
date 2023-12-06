#encaixando em categorias
from datetime import date
nascimento = int(input('Em que ano você nasceu?'))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print('Você vai concorrer na categoria MIRIM!')
#não precisa colocar um intervalo na condição, pois eles já está implícito nas condições if e elif
elif idade <= 14:
    print('Você vai concorrer na categoria INFANTIL!')
elif idade <= 19:
    print('Você concorrerá na categoria JÚNIOR!')
elif idade <= 25:
    print('Você concorrerá na categoria SÊNIOR!')
else:
    print('Você concorrerá na categoria MASTER!')

