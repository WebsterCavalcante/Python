"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar:
o valor da casa
o salário do comprador
e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo sera negado

prestação mensal não pode ser 30% maior que salario
"""
casa = eval(input('Valor da casa: '))
salario = eval(input('Salario do comprador: '))
anos = eval(input('Em quantos anos para pagar: '))
prest = casa / (anos * 12)
r = (salario * 0.3) + salario
if prest <= r:
    print(f'Prestação: R${prest:.2f} por {anos} anos.')
else:
    print('Sinto muito, o banco negou seu pedido')
