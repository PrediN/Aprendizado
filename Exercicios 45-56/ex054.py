from datetime import date

# Impressão de cabeçalho
print('-=-'*10)
print(f"{'QUEM É MAIS VELHO':^30}")
print('-=-'*10)

# Criação da lista vazia para inserção de dados
lista = []

# Iteração para adicionar os valores dentro da lista
for i in range(7):
    lista.append(int(input('Insira o ano de nascimento: ')))
print('Anos de nascimento: ', lista)

# Adquirindo a data atual
ano_atual = date.today().year

# Lista com maiores de idade
maior = []
menor = []

# Iteração para adicionar nos maiores de 21 para dentro da nova lista
for ano in lista:
    if ano_atual-ano >=21:
        maior.append(ano)
    else:
        menor.append(ano)



# Impressão de resultados
print()
print('-=-'*10)
print(f'{"Os maiores de idade são":^30}')
print(f"{'os nacidos em:':^30}")
print(maior)
print(f"{'O menosres de idade são':^30}")
print(f"{'os nacidos em:':^30}")
print(menor)
print('-=-'*10)