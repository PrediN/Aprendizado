# Imrpessão do cabeçalho
print('-=-'*10)
print(f"{'GERADOR DE TABUADA':^30}")
print('-=-'*10)

# Input dos valores da tabuada
n = int(input('De qual número será a tabuada? '))
quantidade = int(input('Quantas linhas quer na tabuada? '))

# Laço de repetição baseado na quantidade de linhas desejadas
for i in range(0, quantidade+1):
    resultado = '{}x{}={}'.format(n, i, (n*i))
    print(resultado)
