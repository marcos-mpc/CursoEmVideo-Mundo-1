print(30*'*')
print('BUSCADOR DA PALAVRA SANTO')
print(30*'*')
nome = input('digite o nome de uma cidade: ')
separar = nome.upper().split()
primeira = separar[0]
print('a primeira palavra nesse nome é santo ? {}'.format('SANTO' in primeira))
