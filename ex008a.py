print(20*'=')
print('CONVERSOR DE MEDIDAS')
print(20*'=')
n = float(input('digite um valor em metros: '))
print('a conversão de {}m em outras medidas fica:\n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(n, (n/1000), (n/100), (n/10),
                                                                                  (n*10), (n*100), n*1000))