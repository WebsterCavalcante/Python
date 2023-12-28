# Crie um algoritmo que leia o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
n = eval(input('Digite Seu Salario: '))
print(f'Seu salario é \033[1;32mR${n:.2f}\033[m, com o aumento de \033[1;34m15%\033[m é \033[1;32mR${(n / 100 * 15) + n:.2f}')
