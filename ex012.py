print(20*'=')
print('PROGRAMA DE DESCONTO')
print(20*'=')
n = float(input('digite um valor: R$'))
p = n*5/100
print('R${:.2f} com 5% de desconto fica R${:.2f}'.format(n, (n-p)))
