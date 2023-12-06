#executando operações com dois números dados
from time import sleep
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Diigite o segundo valor:'))
menu = 0
while menu != 5:
    print('''========== MENU ===========
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    menu = int(input('Digite a sua opção:'))
    if menu == 1:
        soma = n1 + n2
        print(f'A soma dos números digitados é {soma}.')
    elif menu == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores digitados é {mult}.')
    elif menu == 3:
        maior = max(n1, n2)
        print(f'O maior valor digitado é {maior}.')
    elif menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif menu == 5:
        print('Encerrando o programa...')
    else:
        print('Operação inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Volte sempre!')
