print('$-'*10, 'NOVO SALARIO', '-$'*10)

# Inserção de variaveis

s = float(input('Qual o seu salario atual? '))

# Conta com 15% de aumento ao valor original

ns = s*1.15
va = ns-s

print('Seu salario terá um aumento de R${:.2f}, saindo de R${} e chegando em R${:.2f}'.format(va, s, ns))