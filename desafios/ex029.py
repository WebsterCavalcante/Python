# Escreva um programa que leia a velocidade de um carro.
# Se ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
velocidade = eval(input('Digite a velocidade: '))
if velocidade > 80:
    print(f'você foi multado em \033[1;31mR${(velocidade - 80) * 7:.2f}\033[m')
print(f'sua velocidade foi de {velocidade}Km/h')
