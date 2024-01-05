# criar um programa que leia um número inteiro e mostre na tela se é par ou impar.
n = int(input('Digite um numero: '))
if n % 2 == 0:
    print(f'o número {n} é \033[1;35mpar\033[m.')
else:
    print(f'O número {n} é \033[1;32mimpar\033[m.')
