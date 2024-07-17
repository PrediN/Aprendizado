# Categoria natação

# Impressão de cabeçalho
print('-=-'*10)
print(f'{'CATEGORIA NATAÇÃO':^30}')
print('-=-'*10)

# Iserção de variavel
idade = int(input('Insira sua idade: '))

# Estrutura condicional
if idade <= 9:
    print(f'Você ainda tem \033[31m{idade}\033[m. Sua categoria é \033[31mMIRIM\033[m!')
elif idade > 9 and idade <= 14:
    print(f'Você tem \033[31m{idade}\033[m. Sua categoria é \033[31mINFANTIL\033[m!')
elif idade > 14 and idade <= 19:
    print(f'Você tem \033[31m{idade}\033[m. Sua categoria é \033[31mJUNIOR\033[m!')
elif idade == 20:
    print(f'Você tem \033[31m{idade}\033[m . Sua categoria é \033[31mSÊNIOR\033[m!')
else:
    print(f'Você tem \033[31m{idade}\033[m. Sua categoria é \033[31mMASTER\033[m!')