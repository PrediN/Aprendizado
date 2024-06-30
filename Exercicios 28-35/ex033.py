# Faça um programa que leia três números intereiros e mostre qual é o maior e qual é o menor
print('='*10, 'COMPARADOR DE NÚMEROS', '='*10)
print()

# Inserção de variaveis
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

# Estrura condicional
# Encontrar o menor número
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

# Encontrar o maio número
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

print()
print('Dos números inserido tiramos que:')
print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))