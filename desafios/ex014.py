# 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
n = eval(input('Digite  um número: '))
print(f'\033[1;32m{n}°C\033[m convertido em Fahrenheit é \033[1;32m{n * 9 / 5 + 32}°F')
