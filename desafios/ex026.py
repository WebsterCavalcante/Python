# Faça um programa que leia uma frase e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela última vez
nome = str(input('Digite um frase: ')).strip().lower()
total = nome.count('a')
pri = nome.find('a')
ult = nome.rfind('a')
print(f'\033[1;36mA letra A aparece {total} vezes')
print(f'\033[1;35ma letra A aparece pela primeira vez no index: {pri}')
print(f'\033[1;32ma letra A aparece pela ultima vez no index: {ult}')
