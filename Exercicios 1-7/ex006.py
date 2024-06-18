print('=+'*10, 'BEM VINDO A DUPLICADOR, TRIPLICADOR E RAIZ QUADRADOR DE NÚMEROS', '+='*10)

n = int(input('Insira o número desejado:'))

d = int(n*2)
t = int(n*3)
rq = float(n**(1/2))

print('Os resultados da nossa máquina de calculo foram: \n O dobro de {} é {}. \n O triplo é {}. \n E sua raiz quadrada é {:.3f}.'.format(n, d, t, rq))
