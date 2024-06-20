import random

print('='*10, 'SORTEADOR DE ORDEM', '='*10)
print('')

# Inserção das variaveis com nomes

n1 = input('Qual o nome do primero aluno? ')
n2 = input('Qual o nome do segundo aluno? ')
n3 = input('Qual o nome do terceiro aluno? ')
n4 = input('Qual o nome do quarto aluno? ')

# Organização em Arrays

lista_nome1 = [n1, n2, n3, n4]

# Artigo para embaralhar a array anterior

random.shuffle(lista_nome1)

# Impressão da lista embaralhada

print('A ordem da apresentção será a seguinte ordem\n{}'.format(lista_nome1))