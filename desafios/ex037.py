# Escreva um programa que leia um número interio qualquer e peça para o usuario
# escolher a base de converção
# 1 para binario
# 2 para Octal
# 3 para Hexadecimal
n = int(input('Digite um número inteiro: '))
print("""Escolha uma opção: 
[1] Binario
[2] Octal
[3] Hexadecimal""")
escolha = eval(input('Digite: '))
if escolha == 1:
    print(f'O número {n} em Binario é {bin(n)[2:]}')
elif escolha == 2:
    print(f'O número {n} em Octal é {oct(n)[2:]}')
elif escolha == 3:
    print(f'O número {n} em Hexadecimal é {hex(n)[2:]}')
else:
    print('\33[1:31mERRO: O valor digitado não corresponde a nenhuma das três opções.')
