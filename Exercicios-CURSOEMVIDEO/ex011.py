#ler largura e altura de uma parede, calcular a area e a quantidade de tinta necessaria para
#pintá-la sabendo que cada litro de tinta pinta 2m^2
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar*alt
tinta = area/2
print('Serão necessários {} litros de tinta para pintar a parede'.format(tinta))
