print('='*10, 'MEDIDOR DE PAREDE E BALDES', '='*10)

# Inserção de variaveis

alt = float(input('Qual a altura da parede em metros? (Use ponto se for medida quebrada)'))
larg = float(input('Qual a largura da parede em metros? (Use ponto se for medida quebrada)'))

# Calculos de área da parede e litro de tinta

area = alt*larg
pintado = area/2

print('Para uma parede de área {:.2f}, serão necessarios: {:.2f} litros de tinta.'.format(area, pintado))