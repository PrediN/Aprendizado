# Cria uma lista vazia para armazenar os números
lista = []

# Loop para adicionar 6 números à lista
for i in range(6):  # Repetirá 6 vezes para capturar 6 números
    # Solicita um número ao usuário e adiciona à lista
    lista.append(int(input('Digite o número desejado: ')))

# Imprime a lista com os números digitados
print()

# Usa a os valores da lista para que eu possa imprimir como uma string e sem []
lista__str = ','.join(map(str, lista))
print('Aqui estão os números inseridos: {}'.format(lista__str))

# Inicializa a variável para armazenar a soma dos números pares
soma_par = 0
lista_par = []

# Loop para verificar cada número na lista
for c in lista:
    # Verifica se o número é par
    if c % 2 == 0:
        lista_par.append(c)
        # Adiciona o número par à soma
        soma_par += c
lista_par__str = ','.join(map(str, lista_par))

# Imprime a soma dos números pares
print()
print('Os números pares inseridos na lista foram: {}'.format(lista_par__str))
print('A soma dos números pares é igual a: {}'.format(soma_par))
