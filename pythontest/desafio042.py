#condições aninhadas
a = float(input('Digite o valor da reta a:'))
b = float(input('Digite o valor da reta b:'))
c = float(input('Digite o valor da reta c:'))
if a < b + c and b < a + c and c < a + b:
    print('Estas retas formam um triângulo', end='')
    if a == b == c:
        print(' equilátero!')
    elif a != b != c != a:
        print(' escaleno!')
    else:
        print(' isósceles!')
else:
    print('Estas retas não formam um triângulo!')
