# Emprestimo de banco

# Impressão de topo
print('-=-'*10)
print(f"{'FINANCIAMENTO DE CASA':^30}")
print('-=-'*10)

# Inserção de variaveis
valorCasa = int(input('Insira o valor da casa: R$'))
salario = float(input('Insira o valor do salário: R$'))
anos = int(input('Insira a quantidade de anos do financiamento: '))

# Calculos do valor financiado
financiamento = float(valorCasa/(anos*12))

# Estrutura condicional
if financiamento <= salario*0.3:
    print('Seu financiamento foi aprovado! :)')
    print('O seu financiamento ficou com um total de {} parcelas.'.format(anos*12))
    print('O valores mensais das parcelas são R${:.2f}'.format(financiamento))
else:
    print('Seu financiamento foi negado! :(')