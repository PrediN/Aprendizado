import random

print('='*10,'SORTEADOR DE NOMES', '='*10)
print('')

# Inserção de nomes

n1 = input('Insira o nome do primeiro aluno: ')
n2 = input('Insira o nome do segundo aluno: ')
n3 = input('Insira o nome do terceiro aluno: ')
n4 = input('Insira o nome do quarto aluno: ')

# Função de sorteio

x = random.randint(1, 4)

# Correção do guanabara
lista = [n1, n2,n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

# Estruturas criada por mim para escolha de impressão de resultado

if x == 1:
    print('{} irá apagar a lousa'.format(n1))
if x == 2:
    print('{} irá apagar a lousa'.format(n2))
if x == 3:
    print('{} irá apagar lousa'.format(n3))
if x == 4:
    print('{} irá apagar a lousa'.format(n4))


