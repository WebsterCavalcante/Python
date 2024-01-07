# crie um programa que pergunte o salario de um funcionario e calcule seu aumento.
# para selario acima de 1.250,00,calcule um almento de 10%
# para selario menores que isso,calcule um almento de 15%
salario = eval(input('Digite seu salario: '))
r1 = salario*0.10
r2 = salario*0.15
if salario > 1250:
    print(f'salario atual: \033[1;32mR${salario + r1:.2f}')
else:
    print(f'salario atual: \033[1;32mR${salario + r2:.2f}')
