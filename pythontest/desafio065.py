c = 'S'
soma = quant = maior = menor = média = 0
while c in 'S':
    n = int(input('Digite um número:'))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Quer continuar [S/N]?')).upper().strip()[0]

média = soma/quant

print(f'Você digitou {quant} números e a média foi {média:.2f}')
print(f'O maior valor digitado foi {maior} e o menor valor digitado foi {menor}')
