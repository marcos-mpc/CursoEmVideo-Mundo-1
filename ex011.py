print(13*'=')
print('PINTAR PAREDE')
print(13*'=')
la = float(input('largura: '))
al = float(input('altura: '))
ar = la*al
print('vc precisara de {:.2f} litros de tinta para pintar sua parede que tem uma area de {:.2f}m²'.format((ar/2), ar))
