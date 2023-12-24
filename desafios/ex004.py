# faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as
# informações possíveis sore ele.
n = input('Digite algo: ')
print('\033[35m=' * 30)
print(f'\033[1;33m{n}\033[m')
print('\033[35m=' * 30)
print(f'\033[mtipo primitivo \033[1;32m{type(n)}')
print(f'\033[msó tem espaços? \033[1;32m{n.isspace()}')
print(f'\033[mé um número? \033[1;32m{n.isnumeric()}')
print(f'\033[mé alfaetico? \033[1;32m{n.isalpha()}')
print(f'\033[mé alfa-númerico? \033[1;32m{n.isalnum()}')
print(f'\033[mesta em maiusculas? \033[1;32m{n.isupper()}')
print(f'\033[mesta em minusculas? \033[1;32m{n.islower()}')
