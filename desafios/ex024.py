# crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "SANTO".
nome = str(input('nome da cidade: ')).strip()
nome = nome.upper()
nome = nome.split()
if 'SANTO' in nome[0]:
    print('Tem \033[1;36mSanto\033[m no nome.')
else:
    print('não tem \033[1;36mSanto\033[m no nome')
