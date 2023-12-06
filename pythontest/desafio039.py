#alistamento militar
nascimento = int(input('Digite o ano do seu nascimento:'))
from datetime import date
anoalistamento = nascimento + 18
anoatual = date.today().year
if anoalistamento == anoatual:
    print('Este ano você deve se alistar nas Forças Armadas!')
elif anoalistamento > anoatual:
    print(f'''Faltam {anoalistamento - anoatual} anos para você se alistar nas Forças Armadas!'
Seu alistamento será em {anoalistamento}.''')
else:
    print(f'''Você deveria ter se alistado há {anoatual - anoalistamento} anos.
Regularize sua situação!
Você deveria ter se alisado em {anoalistamento}.''')