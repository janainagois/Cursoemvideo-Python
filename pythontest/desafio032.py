#calculando anos bissextos
from datetime import date
ano = int(input('Digite um ano qualquer.\nSe quizer analisar o ano atual, digite 0:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')



