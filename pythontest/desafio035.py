#formando triângulos
la = float(input('Digite o valor da reta a:'))
lb = float(input('Digite o valor da reta b:'))
lc = float(input('Digite o valor da reta c:'))
'''if la + lb > lc:
    if la + lc > lb:
        if lb + lc > la:
            print('Estas retas formam um triângulo!')
else:
    print('Estas retas não formam um triângulo!')'''
#outra forma de fazer
if la < lb + lc and lb < la + lc and lc < la + lb:
    print('Estas retas formam um triângulo!')
else:
    print('Estas retas não formam um triângulo!')
