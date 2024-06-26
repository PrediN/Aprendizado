print('='*10, 'CONTADOR DE LETRAS', '='*10)
print('')

# Inserção de variavel
nome = str(input('Qual o seu nome completo? ')).strip()

# Metodo Upper para que o nome seja colocado em caixa alta
print('Seu nome com todas as letras maisculas: {}'.format(nome.upper()))

# Metodo Lower para que o nome seja colocado em caixa baixa
print('Seu nome com todas as letras minusculas: {}'.format(nome.lower()))

# Como contar todos os caracateres preenchidos no nome
semEspaco = nome.replace(' ', '')
print('O total de caracteres do seu nome é: {}'.format(len(semEspaco)))

# Como contar todos os caracteres preenchidos no nome "corrigido"
print('correção | O total de letras do seu nome é: {}'.format(len(nome)-nome.count(' ')))

# Caracteres do primeiro nome
arrayNome = nome.split()
print('O total de letras do seu primeiro nome é: {}'.format(len(arrayNome[0])))

#Caracateres primeiro nome "corrigido"
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
