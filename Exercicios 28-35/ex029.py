from emoji import emojize


print('='*10, 'RADAR', '='*10)
print()

# Inserção da variavel
velocidade = int(input('Insira a velocidade do carro: '))

# Estrutura condicional
if velocidade<80:
    print(emojize('Dentro do limite de velocidade! :check_mark_button:'))
else:
    print(emojize('Acima do limite de velocidade! :cross_mark:'))
    multa = velocidade-80
    print('Você foi multado! Deverá pagar uma multa no valor de R${:.2f}. Por passar a {}km/h além do permitido'.format((multa*7), multa))