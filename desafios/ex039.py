"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar
- se tá na hora de se alistar
- se já se passou do tempo de si alistar

também tem que mostra o tempo que falta ou que passou do prazo
"""
from datetime import date
idade = int(input('Digite sua data de nascimento: '))
atual = date.today().year
idade = atual - idade
if idade < 18:
    print(f'Sua idade é {idade}')
    print('\33[1:33mAinda vai se alistar.')
elif idade < 42:
    print(f'Sua idade é {idade}')
    print('\33[1:32mtá na hora de se alistar.')
elif idade >= 42:
    print(f'Sua idade é {idade}')
    print('\33[1:31mJá passou do tempo de se alistar.')
