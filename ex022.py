print(20*'=')
print('MODIFICADOR DE NOMES')
print(20*'=')
nome = input('digite seu nome completo: ')
print('o nome {} com as seguintes modificações fica:'.format(nome))
n = nome.strip().split()
n1 = ' '.join(n)
n2 = ''.join(n)
print('maiusculo: ', n1.upper())
print('minuscula: ', n1.lower())
print('quantidade de letras: ', len(n2))
print('quantidade de letras do primeiro nome: ', len(n[0]))
