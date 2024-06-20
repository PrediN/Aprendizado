import math

# Inserção de dados

x = int(input('Insira um número em grau: '))

# Calculos de conversão de graus para radianos

# Outra forma de converter graus para radianos é usando o math.radians
rad = x*(math.pi/180)

# Impressão de radianos

print('Aqui está a conversão de {}° para {:.4f} radianos.'.format(x, rad))
print('')

# Calculo de radianos para seno, cosseno e tangente

print('O seno de {}° é igual a {:.4f}'.format(x, math.sin(rad)))
print('O cosseno de {}° é igual a {:.4f}'.format(x, math.cos(rad)))
print('E a tangente de {}° é igual a {:.4f}'.format(x, math.tan(rad)))