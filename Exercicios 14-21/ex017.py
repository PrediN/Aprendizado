import math

print('='*10, 'CALCULADORA DE HIPOTENUSA', '='*10)

# Inserção dos dados

catOpo = float(input('Insira aqui o valor do cateto oposto (use ponto no lugar da vírgula): '))
catAdj = float(input('Insira aqui o valor do cateto adjacente (useponto no lugar da vírgula):'))

# Calculos para apresentação de resultados

# Outra forma de resolver o esta conta é usando a função math.hypot(catOpo, catAdj)
hip = math.sqrt((catOpo**2)+(catAdj**2))

print('O seu resultado com o triangulo de lados {} e {} é igual a {}'.format(catOpo, catAdj, hip))
