# Conversor de números

# Impressão de cabeçalho
print('-=-'*10)
print(f"{'CONVERSOR DE NÚMEROS':^30}")
print('-=-'*10)

# Legenda
print()
num = int(input('Insira o número a ser convertido: '))
print()
print('-=-'*10)
print(f"{'[ 1 ] - Conversão Binário':<30}")
print(f"{'[ 2 ] - Conversão Octal':<30}")
print(f"{'[ 3 ] - Conversão Hexadecimal':<30}")
print('-=-'*10)
print()

# Inserção e variavel
cond = int(input('Qual será a conversão: '))
if cond in [1, 2, 3]:
    # Estrutura de condição
    if cond == 1:
        print('Seu número: \033[31m{}\033[m convertido em binário ficou \033[31m{}\033[m.'.format(num, bin(num)[2:]))
    elif cond == 2:
        print('Seu número: \033[31m{}\033[m convertido em octal ficou \033[31m{}\033[m.'.format(num, oct(num)[2:]))
    else:
        print('Seu número: \033[31m{}\033[m convertido em hexadecimal ficou \033[31m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Não é um valor de conversão válido!')