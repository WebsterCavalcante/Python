"""
Escrva um programa que leia dois numeros inteiros e compare-os mostrando na tela:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais.
"""
n1 = int(input('1ª Valor: '))
n2 = int(input('2º Valor: '))
if n1 > n2:
    print(f'O número {n1} é maior que o númro {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}')
else:
    print('Não existe valor maior, ambos são iguais')


