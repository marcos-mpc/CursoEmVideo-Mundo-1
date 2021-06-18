print(20*'*')
print('ANALISANDO TRIANGULOS')
print(20*'*')
print('digite o tamanho de 3 retas')
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 + r2 > r3 and r3 + r2 > r1 and r1 + r3 > r2:
    print('essas retas formam um triangulo!')
else:
    print('essas retas nao formam um triangulo!')
