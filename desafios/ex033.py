# crie um programa que leia 3 números e diga qual o maior e o menor.
a = eval(input('Digite um número: '))
b = eval(input('Digite um número: '))
c = eval(input('Digite um número: '))
# Testando Menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'Menor Número: \033[1;31m{menor}\033[m')
# Testando Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'Maior Número: \033[1;32m{maior}\033[m')
