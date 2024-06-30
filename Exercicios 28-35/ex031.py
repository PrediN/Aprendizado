print('='*10, 'CALCULADORA DE VIAGEM', '='*10)
print()

# Inserção de variavel
distancia = int(input('Qual a distância da viagem em km? '))

# Estrutura condicional
if distancia>200:
    print('A distância total de viagem vão ser {}km.'.format(distancia))
    print('Nessa distância a tarifa é de R$0,45 por km.')
    print('O total a pagar pela viagem vai ser de R${:.2f}.'.format(distancia*0.45))
else:
    print('A distância total da viagem vão ser {}km'.format(distancia))
    print('Nessa distância a tarifa é de R$0,50 por km.')
    print('O total a pagar pela viagem vai ser de R${:.2f}'.format(distancia*0.5))