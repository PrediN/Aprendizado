print('='*40, 'CONVERSOR DE MEDIDAS', '='*40)

# Coleta de variaveis

medida = float(input('Insira a medida que deseja converter (caso seja uma medida com vírgula utilize ponto no lugar):'))

# Conversão das medidas

cent = medida*100
mili = cent*10

# Apresentação dos resultados coletados

print('A medida inicial foi: {} \n Sseu tamanho em centímetros é: {}. \n Seu tamanho em milímetros é: {}'.format(medida, cent, mili))