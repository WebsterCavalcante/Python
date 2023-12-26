# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere: US$ 1,00 = R$ 3,27.
print('\033[33m-=-' * 13)
print('\033[1;34mDigite quanto dinheiro tem na carteira.\033[m')
print('\033[33m-=-\033[m' * 13)
n = float(input('Digite um valor: '))
n = round(n, 2)
r = round((n / 4.96), 2)
print(f'Você tem \033[1;32mR${n}\033[m na carteira, e pode comprar \033[1;35mUS${r}')
