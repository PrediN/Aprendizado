# Impressão de cabeçalho
print('-=-' * 10)
print(f"{'COMPARADOR DE GRUPO':^30}")
print('-=-' * 10)
print()

# Criação de listas
nome = []
idade = []
sexo = []

# Iteração para preencher os dados nas listas
for i in range(4):
    nome.append(str(input('Qual o seu nome? ').strip().title()))
    idade.append(int(input('Qual sua idade? ')))
    sexo.append(str(input('Qual seu sexo?(M/F) ').strip().upper()))
    print()

print(nome)
print(idade)
print(sexo)

# Iteração para cálculo de idade média do grupo
media_idade = int(sum(idade) / len(idade))
print('A idade média do grupo é: {}'.format(media_idade))

# Criação do dicionário
pessoas = {}
for nomeDi, idadeDi, sexoDi in zip(nome, idade, sexo):
    pessoas[nomeDi] = {'idade': idadeDi, 'sexo': sexoDi}

# Encontrar o homem mais velho e contar as mulheres com menos de 20 anos
homem_mais_velho = None
idade_homem_mais_velho = -1
mulheres_menos_20 = 0

for nome, detalhes in pessoas.items():
    if detalhes['sexo'] == 'M' and detalhes['idade'] > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = detalhes['idade']
    if detalhes['sexo'] == 'F' and detalhes['idade'] < 20:
        mulheres_menos_20 += 1

# Impressão dos resultados
if homem_mais_velho:
    print(f'O homem mais velho é: {homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')

print(f'A quantidade de mulheres com menos de 20 anos é: {mulheres_menos_20}')
