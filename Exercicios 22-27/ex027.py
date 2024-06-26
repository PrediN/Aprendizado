print('='*10, 'MOSTRADOR DE NOME', '='*10)

# Inserção de variavel
nome  = str(input('Digite seu nome: '))

# Separação do bloco de nomes
primeiro = nome.split(' ', 1)
ultimo = nome.rsplit(' ', 1)

# Impressão de resultados
print('Seu primeiro nome é: {}.'.format(primeiro[0]))
print('O seu último nome é: {}.'.format(ultimo[1]))