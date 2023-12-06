n = input('Digite algo:')
if n.isnumeric():
    print('É um \033[1;31mnúmero\033[m!')
elif n.isalpha():
    print('É uma \033[1;34mletra\033[m!')
elif n.isalnum():
    print('É alfanumérico!')
