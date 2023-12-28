# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
# 95%
print('\033[34m=' * 41)
print('\033[1;33mcalcula 5% de desconto no valor digitado.')
print('\033[34m=\033[m' * 41)
n = eval(input('Digite o preço do produto: '))
print(f'O valor digitado foi \033[1;33mR${n}\033[m, com os 5% de desconto fica \033[1;32mR${n * 0.95:.2f}')
