num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')









'''n = int(input('Digite um número:'))
fazer um loop que divida esse número até ele -1
7 : n%1==0 and n%2!=0 n%3!=0 n%4!=0 n%5!=0 n%6!=0 
6: n%1==0 n%2==0 n%3==0 n%4!=0 n%5!=0
count = 0
for c in range(2,int(n**0.5) +1):
    if n % c == 0:
        count += 1
if count == 1:
    print('É primo')
else:
    print('Não É primo')'''


