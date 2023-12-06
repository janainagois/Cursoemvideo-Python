#ler uma frase e dizer a quantidade de A
frase = str(input('Digite uma frase:')).upper().strip()
print(frase.count('A'))
print(frase.find('A') + 1)
print(frase.rfind('A') + 1)
