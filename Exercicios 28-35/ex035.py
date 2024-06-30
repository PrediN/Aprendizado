print('='*10, 'FORMA TRIANGULO?', '='*10)
print('')

# Inserção de variaveis
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('')

# Estrutura condicional
if a+b>c and a+c>b and b+c>a:
    print('='*15)
    print('É um triangulo!')
    print('='*15)
else:
    print('='*19)
    print('Não é um triangulo!')
    print('='*19)