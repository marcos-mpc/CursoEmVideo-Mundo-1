print(20*'*')
print('RADAR ELETRONICO')
print(20*'*')
velocidade = float(input('qual a velocidade do carro ? '))
if velocidade > 80:
    print('velocidade acima do limite. vc foi multado.')
    print('valor da multa é de: R${:.2f}'.format(7*(velocidade - 80)))
