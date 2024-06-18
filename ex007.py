print('='*10, 'SEJA BEM-VINDO A CALCULADORA DE MÉDIAS', '='*10)

# Inserção das variaveis do aluno como notas e nome

nome = input('Qual o seu nome aluno? ')
n1 = float(input('Qual a sua nota de N1? (coloque os números com ponto não use vírgula)'))
n2 = float(input('Qual a sua nota de N2? (coloque os números com ponto não use vírgula)'))

# Calculos com as variaveis adquiridas acima

m1 = (n1+n2)/2

# Apresentação de resultados

print('Olá {}, suas notas foram: {} e {} correto? \n A sua média final foi {}!'.format(nome, n1, n2, m1))

# Estruturas condicionais para aprovação de aluno

if m1 >= 6:
    print ('Você foi aprovado!! Meus parabéns!')
elif m1 >=3:
    print('Você pegou exame mas eu acredito que você possa passar!')
else:
    print('Você reprovou ;-;')