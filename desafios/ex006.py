# Crie um algoritmo que leia um número e mostre seu dobro ,triplo e raiz quadrada
n = eval(input('Digite um número: '))
print(f'O Dobro de {n} = \033[1;32m{n * 2}')
print(f'\033[mO triplo de {n} = \033[1;33m{n * 3}')
print(f'\033[mA raiz quadrada de {n} = \033[1;35m{n ** (1 / 2):.2f}')
