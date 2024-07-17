print('-=-'*20)
print(f'{'TRIÂNGULO?':^60}')
print('-=-'*20)

# Inserção de variaveis
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
print('')

# Estrutura condicional
if a+b>c and a+c>b and b+c>a:
    print('-=-'*20)
    print(f'{'É um triângulo!':^60}')
    if a == b == c:
        print(f'`{'Seu triângulo é um triângulo equílatero':^60}')
    elif a == b or a == c or b == c:
        print(f'{'Seu triângulo é um triângulo isóceles':^60}')
    else:
        print(f'{'Seu triângulo é um triângulo escaleno':^60}')
    print('-=-'*20)
else:
    print('-=-'*20)
    print(f'{'Não é um triângulo!':^60}')
    print('-=-'*20)