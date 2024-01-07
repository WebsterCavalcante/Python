# desenvolva um programa que leia o comprimento de 3 retas e diga se podem ou não fazer um triangulo.
# a < b+c
n1 = eval(input('Primeiro Seguimento: '))
n2 = eval(input('Segundo Seguimento: '))
n3 = eval(input('Terceiro Seguimento: '))
if n2 + n3 > n1 and n1 + n2 > n3 and n3 + n1 > n2:
    print('\033[1;32mé possível')
else:
    print('\033[1;31mnão é possível')
