"""
A confederação de natação precisa de um programa que leia o ano de nascimento
 de um atleta e mostre sua categoria conforme sua a idade.
 - Até 9 anos: Mirim
 - até 14 anos: Infantil
 - até 19 anos: Junior
 - até 20 anos: Sênior
 - Acima: Master
"""
from datetime import date
ano = eval(input('data de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Idade: {idade}')
    print('Categoria: Mirim')
elif idade <= 14:
    print(f'Idade: {idade}')
    print('Categoria: Infantil')
elif idade <= 19:
    print(f'Idade: {idade}')
    print('Categoria: Junior')
elif idade == 20:
    print(f'Idade: {idade}')
    print('Categoria: Senior')
else:
    print(f'Idade: {idade}')
    print('Categoria: Master')
