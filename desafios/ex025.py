# crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" em qualquer parte do nome
nome = str(input('Digite seu nome: ')).strip()
nome = nome.upper()
if 'SILVA' in nome:
    print('tem \033[1;33msilva\033[m no nome')
else:
    print('Não tem \033[1;33msilva\033[m no nome')