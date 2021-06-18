print(20*'*')
print('AUMENTOS MULTIPLOS')
print(20*'*')
salario = float(input('qual o valor de seu salario ? '))
if salario > 1250:
    print('seu salario teve um aumento de 10% e o valor atual fica de {:.2f}'.format(salario+(salario*10/100)))
else:
    print('seu salario teve um aumento de 15% e o valor atual fica de {:.2f}'.format(salario+(salario*15/100)))
