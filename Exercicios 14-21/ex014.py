print('='*10, 'CONVERSOR DE C° PARA F°', '='*10)

# Inserção das variaveis

c = float(input('Insira a temperatura em C°: (Use ponto para separar os decimais) '))

# Conversão de C° para F°

f = (c*(9/5))+32

# Apresentação de resultados

print('A representação de {}c° em Fahrenheit é: {}f°'.format(c, f))
