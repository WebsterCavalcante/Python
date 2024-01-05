# faça um programa que leia o nome completo e mostre o primeiro e o ultimo nome.
nome = str(input('Digite o nome completo: ')).strip()
div = nome.split()
print(f'primeiro nome: \033[1;34m{div[0]}')
a = len(div)
print(f'\033[mUltimo nome: \033[1;35m{div[a-1]}')
