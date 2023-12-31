# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome em maiúsculas
# o nome em minúsculas
# # Quantas letras ao todo(sem espaço)
# quantas letras tem o 1º nome
nome = input('Digite seu nome completo: ')
print(f'seu nome em maiúsculas: \033[1;33m{nome.upper()}')
print(f'\033[mSeu nome em minusculas: \033[1;33m{nome.lower()}')
nome_uni = nome.replace(' ', '')
nome_div = nome.split()
print(f'\033[mSeu nome tem \033[1;32m{len(nome_uni)} letras')
print(f'\033[mSeu primeiro nome tem \033[1;32m{len(nome_div[0])} letras')

# Resposta: total de caracteres menos total de espaços
# len(nome) - nome.count(' ')
