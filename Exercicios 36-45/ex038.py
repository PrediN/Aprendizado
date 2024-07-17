# leitor e comparador de inteiros

# Impressão do cabeçalho:
print('-=-'*10)
print(f"{'COMPARADOR DE NÚMEROS':^30}")
print('-=-'*10)
print()

# Inserção de variaveis
num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

# Estrutura condicional
if num1 > num2:
    print(f'Dos números inseridos o número \033[31m{num1}\033[m é maior que \033[31m{num2}')
elif num1 == num2:
    print(f'Os dois valores \033[31m{num1}\033[m são iguais e não há um maior entre eles')
else:
    print(f'Dos número inseridos o número \033[31m{num2}\033[m é maior que \033[31m{num1}')