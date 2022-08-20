# 4- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

from datetime import date

ano = int(input('Informe um ano (caso deseja saber se o ano atual é bissexto, digite 0): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')