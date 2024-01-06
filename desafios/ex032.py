# faça um programa que leia um ano e diga se ele é bissexto.
from datetime import date
print('\033[1;35mdigite o ano que quer analisar ou coloque 0 para usar o ano atual\033[m')
ano = eval(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano \033[1;35m{ano}\033[m é bissexto')
else:
    print(f'o ano \033[1;33m{ano}\033[m não é bissexto')
