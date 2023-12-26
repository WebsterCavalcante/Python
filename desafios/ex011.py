# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a
# quantidade de tinta para pinta-la, sabendo que cada litro de tinta, pinta uma adrea de 2m quadrados.
n1 = eval(input('\033[36mDigite a altura da parede: '))
n2 = eval(input('Digite a largura da parede:\033[m '))
r = n2 * n1
tinta = r / 2
print(f'a area da parede é \033[1;33m{r}m²\033[m e você precisa de \033[1;33m{tinta}L\033[m de tinta.')
