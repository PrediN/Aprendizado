# Impressão do cabeçalho
print('-=-'*10)
print('MAIOR E MENOR PESO')
print('-=-'*10)

# Inserção de dados por iteração
pesos = []
for i in range(5):
    pesos.append(int(input('Insira o seu peso aqui: ')))

# Aquisição do maior e menos valor da lista
maior_valor = max(pesos)
menor_valor = min(pesos)

# Impressão dos resultados
print()
print('Dos valores inseridos')
print('O maior valor é: {}Kg'.format(maior_valor))
print('E o menor valor é: {}Kg'.format(menor_valor))