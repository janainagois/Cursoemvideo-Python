#colorindo o terminal
'''print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[0;30;42mTeste')
print('\033[mTeste')
print('\033[7;40mTeste')
print('\033[7;33;44mOlá, Mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}')'''
nome = 'Ian'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretobranco': '\033[7;30m'}
print('Te amo {}{} \033[1;37;41mS2\033[m!'.format(cores['amarelo'], nome))