print(20*'-')
print('CUSTO DA VIAGEM')
print(20*'-')
distancia = float(input('qual a distancia de sua viagem ? '))
if distancia > 200:
    print('o valor cobrado sera de R$0.45 por kilometro\no valor cobrado sera de {:.2f}'.format(distancia * 0.45))
else:
    print('o valor cobrado sera de R$0.50\no valor total sera de R${:.2f}'.format(distancia * 0.50))
