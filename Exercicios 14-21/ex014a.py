print('='*10, 'CONVERSOR DE F° PARA C°', '='*10)

# Inserção de variaveis

f = float(input('Insira a temperatura em F°: (Use ponto para separar os decimais) '))

# Calculos de conversão

c = (f - 32)*(5/9)

# Apresentação dos resultados

print('Fizemos a conversão da temperatura. Você inseriu {}f°\nE nós calculamos {:.2f}c°'.format(f, c))
