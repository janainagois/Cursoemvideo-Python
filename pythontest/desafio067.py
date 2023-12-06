n = 0
c = 0
while True:
        n = int(input('Digite um número para ver sua tabuada, e um número negativo para parar: '))
        if n < 0:
                break
        print('--'*6)
        for c in range(1, 11):
                print(f'{n} * {c} = {n * c}')
        print('--'*6)

print('O programa tabuada foi encerrado!')

