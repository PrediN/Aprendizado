print('='*10, 'PAR OU IMPAR?', '='*10)

# Inserção de varivel
num = int(input('Digite um número: '))

# Contas para resolução do problema
resultado = num%2

# Estrutura condicional
if resultado==0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))
    