print('='*10, 'CALCULADORA DE DESCONTO', '='*10)

# Inserção de variaveis

v1 = float(input('Qual o valor do produto? (Use ponto no lugar da virgula)'))

# Calculos de desconto do produto

v2 = v1*0.95

# Resultados impressos no sistema

print('O valor do produto foi de {} para {:.2f}'.format(v1, v2))