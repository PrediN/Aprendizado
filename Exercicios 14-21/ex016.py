import math

print ('='*10,'Mostrador de parte inteira', '='*10)

# Inserção dos dados para analise

num = float(input('Digite um número qualquer com vírgula (Utilize o ponto no lugar da vírgula): '))

# Método de extração de dados

inteiro = math.trunc(num)

# Impressão do resultado

print('A parte inteira do número {} é {}.'.format(num, inteiro))
