print('='*50)

# Inserção de variaveis
salario = float(input('Digite seu salário: R$'))

# Estrutura condicional
if salario >= 1250.00:
    aumento = salario*0.1
    print('='*50)
    print('Seu salário foi de R${:.2f}.'.format(salario))
    print('Para R${:.2f}. O seu aumento foi R${:.2f}.'.format((salario+aumento), aumento))

else:
    aumento = salario*0.15
    print('='*50)
    print('Seu salário foi de R${:.2f}.'.format(salario))
    print('Para R${:.2f}. O seu auemtno foi R${:.2f}.'.format((salario+aumento), aumento))
print('='*50)