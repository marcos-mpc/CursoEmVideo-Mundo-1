import datetime, time
ano = int(input('digite um ano ou digite 0 para ser o ano atual. '))
print('ANALISANDO...')
time.sleep(3)
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bisexto!'.format(ano))
else:
    print('o ano {} nao é bisexto!'.format(ano))