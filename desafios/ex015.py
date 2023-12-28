# 15: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km/h rodado.
print('\033[1;35mQuantos km percorridos?\033[m')
km = eval(input('Digite: '))
print('\033[1;35mQuantos dias percorridos?\033[m')
dias = eval(input('Digite: '))
r = (km * 0.15) + (dias * 60)
print(f'os km percorridos foram \033[1;33m{km} \033[me os dias que se passaram foram \033[1;33m{dias}\033[m, dando um total = \033[1;32m{r}')
