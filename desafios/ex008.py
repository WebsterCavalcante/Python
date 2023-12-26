# Escreva um programa que leia um número e o exiba convertido em 'cm' e 'mm'.
n = int(input('Digite um número: '))
print(f'\033[1;32m{n}m = {n / 1000}km')
print(f'\033[1;33m{n}{n}m = {n / 100}hm')
print(f'\033[1;34m{n}{n}m = {n / 10}dam')
print(f'\033[1;35m{n}{n}m = {n * 10}dm')
print(f'\033[1;36m{n}{n}m = {n * 100}mm')
print(f'\033[1;31m{n}{n}m = {n * 1000}cm')
