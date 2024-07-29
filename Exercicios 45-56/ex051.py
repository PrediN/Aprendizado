# Impressão do cabeçalho
print('-=-'*10)
print(f"{'GERADOR DE PA':^30}")
print('-=-'*10)

# Inserção de variaveis
primeiro_termo = int(input('Insira o primeiro termo: '))
razao  = int(input('Insira a razão da PA: '))

# Criação da Lista para armazenar os termos da Progreção
lista = []
lista.append(primeiro_termo)

# Loop para adicionar os termos a lista
for pa in range(9):
    primeiro_termo+=razao
    lista.append(primeiro_termo)

lista_str = ','.join(map(str, lista))
print('A sua PA tem os seguintes termos:')
print(lista_str)