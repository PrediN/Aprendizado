print('='*10, 'VOCÊ TEM SILVA NO NOME?', '='*10)
print()

# Inserção de variaveis
nome = str(input('Digite o seu nome compelto: ')).strip().title()
primNome = nome.split()

# Analise de busca do Silva no nome da pessoa
if nome.find('Silva') > -1:
    print('Prazer {}, você tem Silva no seu nome!'.format(primNome[0]))
else:
    print('Prazer {}, você não tem Silva no seu nome que pena!'.format(primNome[0]))
