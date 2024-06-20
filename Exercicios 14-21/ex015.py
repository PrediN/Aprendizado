print('='*10, 'ALUGUEL DE CARROS', '='*10)
print('Olá seja bem vindo a calculadora de aluguel dos carros')
print("Aqui você poderá saber o valor do aluguel por dias e km's")
print('Agradecemos por utilizar os nossos serviços! :D')

# Inserção de valores

dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos quilometros você andou com ele? '))

# Calculos para saber o valor total

diarias = dias*60
distancia = km*0.15

total = diarias+distancia

# Impressão dos resultados

print('Você rodou {}km por {} dias.'.format(km, dias))
print('Aqui estão os valores das diarias R${}'.format(diarias))
print('Os valores pela distancia que rodou R${}'.format(distancia))
print('O valor total do aluguel ficou em: R${:.2f}'.format(total))