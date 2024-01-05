# Desenvolva um programa que leia a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km
# e R$0,45 para viagens mais longas
dist = eval(input('Digite a distancia de uma viagem: '))
if dist <= 200:
    print(f'\033[1mo preço da passagem é \033[1;33mR${dist * 0.50}')
else:
    print(f'\033[1mo preço da passagem é \033[1;33mR${dist * 0.45}')
